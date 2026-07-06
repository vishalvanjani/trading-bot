import argparse
import logging
from bot.client import client
from bot.validators import *
import bot.logging_config

parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument('--side', choices=['BUY', 'SELL'], required=True)
parser.add_argument('--type', choices=['MARKET', 'LIMIT', 'STOP'], required=True)
parser.add_argument("--qty", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_side(args.side)
    validate_type(args.type)

    order_data = {
        "symbol": args.symbol,
        "side": args.side,
        "type": args.type,
        "quantity": args.qty
    }

    if args.type == "LIMIT":
        if not args.price:
            raise ValueError("Price required for LIMIT")
        order_data["price"] = args.price
        order_data["timeInForce"] = "GTC"

    print("Placing order...")
    logging.info(order_data)

    res = client.futures_create_order(**order_data)

    print("SUCCESS")
    print("Order ID:", res["orderId"])
    print("Status:", res["status"])
    print("Executed Qty:", res["executedQty"])

    logging.info(res)

except Exception as e:
    print("FAILED:", str(e))
    logging.error(str(e))