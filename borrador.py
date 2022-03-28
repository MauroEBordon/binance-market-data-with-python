import ccxt
import itertools

coins = ["BTC", "ETH", "ADA", "LINK", "BCH", "DOT", "XRP", "LTC", "BNB"]

#each combination of  different coins separated by a slash (e.g.: "BTC/ETC")

class Coin:
    def __init__(self, name: str):
        self.name = name
        
    def __str__(self):
        return str.upper(self.name)

    #price in BUSD

class Ticker:
    def __init__(self, c1: Coin, c2: Coin):
        
        self.c1 = c1
        self.c2 = c2
        
    def __str__(self):
        return str(self.c1)+"/"+str(self.c2)
    
#exchange object initiation
binance = ccxt.binance()

#binance.fetch_tickers().keys().filter(lambda x: x.contains(c for c in coins))

print(list(filter(lambda x: map(lambda c: c in x, coins), binance.fetch_tickers().keys())))


prices_dic = {}






#initial test
"""
bin_mkt = binance.load_markets()
print(binance.id, bin_mkt)


btc_etc_ticker = binance.fetch_ticker('ETH/BTC')
print(btc_etc_ticker['bid'])


#for tick in tickers[:5]:
    
    #get the Bid price
    #try:
    #    prices_dic[tick] = binance.fetch_ticker(tick)
    #except(ccxt.BadSymbol):
    #    pass
    #get the Ask price


    #calculate ratios between 2 coins


    #show date


    #show exchange name

    #show Ratios

#print(prices_dic)

"""