import gdax
import sys
import json

# todo: automate buying so the whole process can run with a single command

AUTH_FILENAME = 'auth.cfg'
GDAX_API_URL = 'https://api-public.sandbox.gdax.com'

# todo: define product, buy_price, size, profit_margin (take as command line argument)

# product to trade
product = 'eth/usd'

# currency being bought
currency_a = product.split('/')[0].upper()

# currency being sold
currency_b = product.split('/')[1].upper()

# price to buy product at (currency_b)
buy_price = 193

# size of purchase (currency_a)
size = 0.1
currency_a_size = size
currency_b_size = round(currency_a_size * buy_price, 2)

# decimal percentage of profit to be made from trade
profit_margin = 0.05
currency_b_profit = round(profit_margin*currency_b_size, 2)

# price to sell at
target_price = buy_price+profit_margin*buy_price

# total money out
currency_b_target_size = round(currency_a_size*target_price, 2)

print('Buying {} {} for {} {} at {} {}/{} for a profit of {}% ({} {})'.format(currency_a_size, currency_a, currency_b_size, currency_b, buy_price,
                                                                             currency_b, currency_a,  profit_margin, currency_b_profit, currency_b))

# load sensitive values from file
auth_file = open(AUTH_FILENAME, 'r')
auth_values = json.loads(auth_file.read())
# create gdax authenticated client
auth_client = gdax.AuthenticatedClient(auth_values['key'], auth_values['b64secret'], auth_values['passphrase'], GDAX_API_URL)
# create gdax public client
public_client = gdax.PublicClient()


# auto-update price
while True:
    if public_client.get_product_ticker(product_id='ETH-USD')['price']:  # make sure that price value is returned in ticker request to avoid error
        current_price = round(float(public_client.get_product_ticker(product_id='ETH-USD')['price']), 2)  # extract current price from ticker request
        if current_price >= target_price:
            print('Selling {} {} for {} {}'.format(currency_a_size, currency_a, currency_b_target_size, currency_b))
            # sell
            # todo: add later - auth_client.sell(current_price, size, product)
            print('SOLD!')
            break
        sys.stdout.write('\rprice: ${}/ETH'.format(str(current_price)))
        sys.stdout.flush()
