
# <img src="https://github.com/user-attachments/assets/4ef17269-8420-4a2a-92b3-3a020497ab91" width="40" /> Binance Futures Testnet Trading Bot

A robust and modular **Python CLI trading bot** for executing trades on the **Binance Futures Testnet (USDT-M)**.  
Supports multiple order types with validation, logging, and clean architecture.


## <img src="https://github.com/user-attachments/assets/dcdcffb4-c4e2-40ee-84cc-aca8612d257e" height="30px" style="vertical-align: text-bottom; margin-bottom:-3050px;"> Features

- ✅ Market Orders (Instant execution)
- ✅ Limit Orders (Custom price execution)
- ✅ Stop Orders (Trigger-based execution)
- ✅ BUY / SELL support
- ✅ Command-line interface using `argparse`
- ✅ Input validation for safer trades
- ✅ Structured logging to file
- ✅ Error handling & resilience
- ✅ Modular and scalable codebase

## <img src="https://github.com/user-attachments/assets/f3dcee8e-e008-457a-97fb-d3848b425713" height="30px" style="vertical-align:text-bottom;"> Project Structure
```bash
📂trading_bot/
│ 
├── 📂 bot/         
│   ├── client.py
│   ├── orders.py
│   ├── validators.pyt
│   └── logging_config.py
│
├── logs/
├── cli.py
├── requirements.txt
└── README.md            
```

## <img src="https://github.com/user-attachments/assets/6672ee8c-15ed-4fb5-9cd5-63c04ac747c1" height="24px" style="vertical-align: bottom; margin-right: 10px;"> Installation & Setup  

### 1️⃣ Clone the Repository   
```bash
git clone rutvikbarbhai/trading-bot
cd trading_bot
```
### 2️⃣ Create a virtual Environment 
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
## 🔐 Environment Configuration

- Use Binance Futures Testnet keys from
```bash
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key
```
👉 Get your API keys from Binance Futures Testnet:
https://testnet.binancefuture.com


## Usage

### ▶️ Market Buy Order
```bash
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### ▶️ Limit Sell Order
```bash
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 150000
```
### ▶️ Stop Buy Order
```bash
python3 cli.py --symbol BTCUSDT --side BUY --type STOP --qty 0.001 --price 120000
```


## 📄 Logs

All logs are stored in:
```bash
logs/app.log
```

## <img src="https://github.com/user-attachments/assets/612137fd-b2de-411c-acd7-f94c4811e9f2" height="25px" style="vertical-align:text-bottom;">Tech Stack

- **Python 3** 
- **python-binance**
- **python-dotenv**
- **argparse**
- **logging**


### Includes:

- Order execution details
- Errors and exceptions
- Debug information

### ⚠️ Disclaimer

This project is intended for educational and testing purposes only.
- It uses the Binance Futures Testnet, not real funds.
- Trading in live markets involves financial risk.


### 👤 Developers 
Shalmali Bichkar

### <img src="https://github.com/user-attachments/assets/1aafab50-1305-47c4-87ab-40a9d64f3067" alt="contribution gif" width="35"/> Contributing
@rutvik barbhai
