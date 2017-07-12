import json
import os.path
import time
import argparse

# todo: find 'fee' percentage. 0.3%?
# todo: implement GDAX API
# todo: implement tkinter interface

parser = argparse.ArgumentParser(description="Utility to log trades")
parser.add_argument("--product", required=True, help="Pass in the name of the product")
parser.add_argument("--size", required=True, help="Pass in the size")
parser.add_argument("--price", required=True, help="Pass in the price")
parser.add_argument("--fee", required=True, help="Pass in the price")
args = parser.parse_args()

product = args.product
size = args.size
price = args.price
fee = args.fee

FILE_NAME = '{}_trades_{}.log'.format(product, time.strftime("%d-%m-%Y"))

if os.path.isfile(FILE_NAME):
    f = open(FILE_NAME, 'r')
    trades = json.loads(f.read())
else:
    trades = []

trade = {'size': size, 'price': price, 'fee': fee}
trades.append(trade)
f = open(FILE_NAME, 'w')
print(json.dumps(trades))
f.write(json.dumps(trades))
f.close()
