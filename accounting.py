import requests

ACCOUNT_FILE = 'account.json'  # todo: create file system for importing/exporting account data
CURRENCIES = 'usd', 'btc', 'eth'  # todo: allow for more currencies in database

r = requests.get('https://api.gdax.com/products/btc-usd/ticker')
btc_usd_val = round(float(r.json()['price']), 3)

r = requests.get('https://api.gdax.com/products/eth-usd/ticker')
eth_usd_val = round(float(r.json()['price']), 3)

r = requests.get('https://api.gdax.com/products/eth-btc/ticker')  # trading note- as btc increases and eth decreases, the difference between the two gets greater
eth_btc_val = round(float(r.json()['price']), 3)

print('1 BTC: $'+str(btc_usd_val))
print('1 ETH: $'+str(eth_usd_val))
print('1 BTC: '+str(eth_btc_val)+' ETH')


class Account:
    def __init__(self):
        self.balance = {}
        for c in CURRENCIES:
            self.balance[c] = 0

    def deposit(self, funds, currency):
        self.balance[currency] += funds

    def withdrawal(self, funds, currency):
        self.balance[currency] -= funds

# broken code
# transaction = {'pre_balance': , 'sent': , 'received': , }
