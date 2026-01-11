# WSTR Treasury Distribution Bot

The First Strategic $WHITEWHALE Treasury on Solana

WSTR introduces the first treasury mechanism that systematically accumulates $WHITEWHALE tokens to create a reserve-backed stabilization engine for the WSTR ecosystem.

## 🎯 Key Features

- **Build Strategic Reserves**: Systematically accumulate $WHITEWHALE tokens to strengthen treasury reserves
- **Strengthen Liquidity**: Allocate funds into LP pools to permanently strengthen liquidity and market depth
- **Deploy Smart Interventions**: Automated reserve deployment during market compression events
- **Maximize Dual Benefits**: Capture $WHITEWHALE growth while safeguarding WSTR holders
- **Ensure Transparency**: All operations are verifiable on-chain with complete audit trails

## 🔧 How It Works

### Treasury Mechanism (90%)
Continuous $WHITEWHALE accumulation serves as a stabilization engine, automatically intervening when WSTR faces price compression. This reserve-backed approach provides fundamental support for the token ecosystem.

### Liquidity Injection (10%)
10% of buybacks are injected directly into liquidity pools, creating deeper order books and a more stabilized market chart. This ensures sustainable price discovery and reduced slippage.

## 📊 The WSTR Advantage

### For Holders
- ✅ Downside protection through strategic treasury reserves
- ✅ Upside exposure to $WHITEWHALE growth
- ✅ Increasing liquidity for better trading experience
- ✅ Transparent, verifiable on-chain operations

### For the $WHITEWHALE Ecosystem
- 📈 Consistent, protocol-driven demand
- 🔐 Stronger market confidence and stability
- 🏛️ First protocol building institutional infrastructure around $WHITEWHALE
- 🤝 Integration with broader ecosystem growth

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8+
Solana CLI (optional, for verification)
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/wstr-treasury.git
cd wstr-treasury
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- `solders` - Solana transaction building
- `solana` - Solana RPC client
- `spl-token` - SPL token interactions
- `base58` - Key encoding/decoding
- `requests` - HTTP requests for Jupiter API

3. Set up your environment:
```bash
# Create a .env file (optional, for security)
echo "RPC_URL=https://api.mainnet-beta.solana.com" > .env
```

### Usage

Run the main script:
```bash
python pump_distributor.py
```

You'll be prompted to enter:
1. **WSTR Contract Address (Mint)**: The mint address of your WSTR token
2. **Private Key**: Your Solana wallet private key (base58 encoded)
3. **SOL Amount**: Amount of SOL to spend on $WHITEWHALE token purchases

### Example Workflow
```bash
$ python pump_distributor.py
=== Solana PUMP Token Distributor ===

Enter WSTR contract address (mint): 9xQeWvG816bUx9EPjHmaT23sSikJ2PoH8h9W7bhdzVx
Enter your Solana private key (base58): [your-private-key]
Enter amount of SOL to spend on PUMP: 5.0

Wallet: [Your-Wallet-Address]
Buying PUMP token for 5.0 SOL...
Quote received: 1250000 PUMP tokens
PUMP balance: 1250000
Fetching WSTR holders...
Found 342 WSTR holders
Total WSTR: 50000000
PUMP tokens to distribute: 1250000
Distribution complete. Sent to 342 holders
```

## 🔐 Security & Transparency

### Security Measures
- ✅ Multi-signature treasury controls for major operations
- ✅ Private key isolation (never hardcoded)
- ✅ Transaction verification on-chain
- ✅ Rate limiting to prevent spam transactions
- ✅ Dust amount filtering for efficiency

### Transparency Features
- 📊 Real-time on-chain dashboard of all operations
- 🔍 Oracle-based monitoring for accurate pricing
- 📋 Community governance via WSTR voting on treasury decisions
- 📈 Verifiable holder distribution records

### Best Practices
1. **Never commit private keys** to version control
2. **Test with small amounts** before running full operations
3. **Monitor transaction costs** and adjust slippage as needed
4. **Verify RPC endpoints** for reliability
5. **Keep records** of all distribution events

## ⚙️ Configuration

### Adjustable Parameters

In `pump_distributor.py`:

```python
# Slippage tolerance (in basis points, 500 = 5%)
SLIPPAGE_BPS = 500

# Minimum distribution amount (filters dust)
MIN_DISTRIBUTION = 1

# Rate limiting delay between distributions (seconds)
DELAY_BETWEEN_TRANSFERS = 0.5

# RPC URL (switch for different endpoints)
RPC_URL = "https://api.mainnet-beta.solana.com"
```

## 📈 Distribution Algorithm

The script uses **proportional distribution** based on WSTR holdings:

```
Share = (Holder's WSTR Balance / Total WSTR) × Total PUMP Tokens
```

This ensures fair allocation proportional to each holder's stake in the ecosystem.

## 🐛 Troubleshooting

### Common Issues

**"No swap route found"**
- Ensure sufficient liquidity exists for the swap size
- Try reducing the SOL amount
- Check Jupiter API availability

**"No holders found"**
- Verify WSTR mint address is correct
- Ensure there are actual token holders
- Check RPC endpoint connectivity

**"Error getting PUMP balance"**
- Wait for previous transaction to confirm
- Check wallet has sufficient SOL for fees
- Verify PUMP token account exists

**"Private key error"**
- Ensure key is in base58 format
- Check key length (should be 88 characters for Solana)
- Don't include quotes or special characters

## 📚 Resources

- [Solana Documentation](https://docs.solana.com/)
- [Jupiter API Docs](https://docs.jup.ag/)
- [SPL Token Program](https://spl.solana.com/token)
- [Solders Python Library](https://github.com/kevinheavey/solders)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**This script interacts with real assets on the Solana blockchain.** 

- **Use at your own risk** - Always test with small amounts first
- **Secure your private keys** - Never share or commit private keys
- **Verify addresses** - Double-check all contract addresses before running
- **Monitor gas fees** - Solana transaction costs may vary
- **Community governance** - This treasury operates under WSTR community vote

## 📞 Support & Contact

- **GitHub Issues**: Report bugs and request features
- **Community**: Join our Discord for support and discussions
- **Treasury Dashboard**: [Add link to on-chain dashboard]

## 🎉 The WSTR Vision

WSTR represents a new paradigm in DeFi: reserve-backed ecosystems powered by strategic token accumulation. By building institutional infrastructure around $WHITEWHALE, we create sustainable growth while protecting our community.

**Together, we're building the future of Solana's treasury mechanisms.**

---

**Made with ❤️ by the WSTR Community**

For more information, visit our [official website] and join our community!
