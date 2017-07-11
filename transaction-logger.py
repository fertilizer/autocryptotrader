import json
import os.path
import time

product = input('enter product\n')
confirm = input('making transactions for {}'.format(product))
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

        size = input('enter size of product bought:\n')

        price = input('enter price:\n')

        fee = input('enter fee:\n')

        confirm = input('is this correct?\n product: {}\n size: {}\n price: {}\n fee: {}\n'.format(product, size, price, fee))
        
        if confirm == 'y' or confirm == 'yes':
            gpu_dict = {'product': product, 'size': size, 'price': price, 'fee': fee}
            transactions.append(gpu_dict)
            f = open(FILE_NAME, 'w')
            print(json.dumps(transactions))
            f.write(json.dumps(transactions))
            f.close()
