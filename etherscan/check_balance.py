from etherscan import Etherscan
from datetime import datetime

apikey = "TC73QSQZQBVNN7UY18TSJA4TZKAYA8JSRV"
eth = Etherscan(apikey) # key in quotation marks
wei2ether = 1e18

address1 = "0x7193b82899461a6aC45B528d48d74355F54E7F56"  # A BAYC NFT buyer

# Get ether in the account
balance_ether = int(eth.get_eth_balance(address=address1))/wei2ether

price_usd = float(eth.get_eth_last_price()['ethusd'])
timestamp = int(eth.get_eth_last_price()['ethusd_timestamp'])
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)
print("A BAYC NFT buyer:\n Eth balance", balance_ether, ' ether.\n Fiat value: $', price_usd*balance_ether)