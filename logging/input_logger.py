import json
import os.path
import time

# todo: pass variables as commandline arguments? look into airflow
# todo: find 'fee' percentage. 0.3%?
# todo: implement GDAX API
# todo: implement tkinter interface

product = input('enter product\n')
confirm = input('making transactions for {}? (y or n)\n'.format(product))
if confirm == 'y' or confirm == 'yes':

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

        size = input('enter size:\n')

        price = input('enter price:\n')

        fee = input('enter fee:\n')

        confirm = input('is this correct? (y or n)\n size: {}\n price: {}\n fee: {}\n'.format(size, price, fee))
        
        if confirm == 'y' or confirm == 'yes':
            gpu_dict = {'size': size, 'price': price, 'fee': fee}
            transactions.append(gpu_dict)
            f = open(FILE_NAME, 'w')
            print(json.dumps(transactions))
            f.write(json.dumps(transactions))
            f.close()
