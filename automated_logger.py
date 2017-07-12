import json
import os.path
import time
import argparse

# todo: pass variables as commandline arguments? look into airflow
# todo: find 'fee' percentage. 0.3%?
# todo: implement GDAX API
# todo: implement tkinter interface

parser = argparse.ArgumentParser(description="Utility to log transactions")

parser.add_argument("--product", required=True, help="Pass in the name of the product")

parser.add_argument("--size", required=True, help="Pass in the size")

parser.add_argument("--price", required=True, help="Pass in the price")

parser.add_argument("--fee", required=True, help="Pass in the price")

args = parser.parse_args()

product = args.product

FILE_NAME = '{}_transactions_{}.log'.format(product, time.strftime("%d-%m-%Y"))

transaction = {'product': None, 'size': None, 'price': None, 'fee': None}

if os.path.isfile(FILE_NAME):
    f = open(FILE_NAME, 'r')
    transactions = json.loads(f.read())
else:
    transactions = []

while True:
    if os.path.isfile(FILE_NAME):
        f = open(FILE_NAME, 'r')
        transactions = json.loads(f.read())

    size = args.size

    price = args.price

    fee = args.fee


    gpu_dict = {'size': size, 'price': price, 'fee': fee}
    transactions.append(gpu_dict)
    f = open(FILE_NAME, 'w')
    print(json.dumps(transactions))
    f.write(json.dumps(transactions))
    f.close()
