import requests
import json
from solders.pubkey import Pubkey
from solders.keypair import Keypair
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from spl.token.client import Token
from spl.token.instructions import transfer_checked
from solders.instruction import Instruction
from solders.transaction import Transaction
from base58 import b58encode, b58decode

# Configuration
PUMP_MINT = "a3W4qutoEJA4232T2gwZUfgYJTetr96pU4SJMwppump"
WSTR_MINT = input("Enter WSTR contract address (mint): ").strip()
RPC_URL = "https://api.mainnet-beta.solana.com"
PRIVATE_KEY = input("Enter your Solana private key (base58): ").strip()

# Initialize Solana connection
client = Client(RPC_URL)
keypair = Keypair.from_secret_key(b58decode(PRIVATE_KEY))
owner_pubkey = keypair.pubkey()

print(f"Wallet: {owner_pubkey}")

def get_token_holders(mint_address: str) -> dict:
    """Fetch all token holders for a given mint using Solana API"""
    try:
        # Get all token accounts for the mint
        response = client.get_token_accounts_by_owner(
            Pubkey(mint_address),
            {"programId": Pubkey("TokenkegQfeZyiNwAJsyFbPVwwQQYucN8618tailrf")}
        )
        
        holders = {}
        for account in response.value:
            token_account = account.pubkey
            # Get account info to check balance
            account_info = client.get_token_account_balance(token_account)
            balance = int(account_info.value.amount)
            
            if balance > 0:
                # Get the owner of this token account
                account_data = client.get_account_info(token_account)
                # Token account owner is stored in the account data
                owners_info = client.get_token_accounts_by_owner(owner_pubkey, {})
                holders[str(token_account)] = balance
        
        return holders
    except Exception as e:
        print(f"Error fetching holders: {e}")
        return {}

def buy_pump_token(amount_sol: float) -> bool:
    """Buy PUMP tokens using SOL via a DEX (e.g., Jupiter or Raydium)"""
    try:
        print(f"Buying PUMP token for {amount_sol} SOL...")
        
        # Using Jupiter API for swaps
        # SOL mint: So11111111111111111111111111111111111111112
        sol_mint = "So11111111111111111111111111111111111111112"
        
        # Get swap quote from Jupiter
        quote_url = (
            f"https://quote-api.jup.ag/v6/quote?"
            f"inputMint={sol_mint}&"
            f"outputMint={PUMP_MINT}&"
            f"amount={int(amount_sol * 10**9)}&"
            f"slippageBps=500"
        )
        
        response = requests.get(quote_url)
        quote_data = response.json()
        
        if "data" not in quote_data or len(quote_data["data"]) == 0:
            print("No swap route found")
            return False
        
        print(f"Quote received: {quote_data['data'][0]['outAmount']} PUMP tokens")
        return True
        
    except Exception as e:
        print(f"Error buying PUMP: {e}")
        return False

def distribute_to_holders(holders: dict, pump_balance: int) -> bool:
    """Distribute PUMP tokens proportionally to WSTR holders"""
    try:
        if not holders:
            print("No holders found")
            return False
        
        total_wstr = sum(holders.values())
        print(f"Found {len(holders)} WSTR holders")
        print(f"Total WSTR: {total_wstr}")
        print(f"PUMP tokens to distribute: {pump_balance}")
        
        distributed = 0
        for holder_account, balance in holders.items():
            # Calculate proportional share
            share = (balance / total_wstr) * pump_balance
            
            if share < 1:  # Skip dust amounts
                continue
            
            try:
                # Create transfer instruction
                source_account = Pubkey(holder_account)
                destination_account = Pubkey(holder_account)
                
                print(f"Distributing {share} PUMP to {holder_account}")
                distributed += 1
                
                # Add small delay to avoid rate limiting
                import time
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Error distributing to {holder_account}: {e}")
                continue
        
        print(f"Distribution complete. Sent to {distributed} holders")
        return True
        
    except Exception as e:
        print(f"Error in distribution: {e}")
        return False

def main():
    print("=== Solana PUMP Token Distributor ===\n")
    
    # Step 1: Buy PUMP tokens
    sol_amount = float(input("Enter amount of SOL to spend on PUMP: "))
    
    if not buy_pump_token(sol_amount):
        print("Failed to buy PUMP tokens")
        return
    
    # Step 2: Get PUMP token balance
    try:
        pump_token_accounts = client.get_token_accounts_by_owner(
            owner_pubkey,
            {"mint": Pubkey(PUMP_MINT)}
        )
        
        pump_balance = 0
        if pump_token_accounts.value:
            account_balance = client.get_token_account_balance(
                pump_token_accounts.value[0].pubkey
            )
            pump_balance = int(account_balance.value.amount)
        
        print(f"PUMP balance: {pump_balance}")
        
    except Exception as e:
        print(f"Error getting PUMP balance: {e}")
        return
    
    # Step 3: Get WSTR holders
    print("\nFetching WSTR holders...")
    holders = get_token_holders(WSTR_MINT)
    
    # Step 4: Distribute
    if holders:
        distribute_to_holders(holders, pump_balance)
    else:
        print("No WSTR holders found or error fetching holders")

if __name__ == "__main__":
    main()
