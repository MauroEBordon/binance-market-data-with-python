import ccxt

from enum import Enum

class Coins(str, Enum):
    BTC = 'BTC'
    ETH = 'ETH'
    ADA = 'ADA'
    LINK = 'LINK'
    BCH = 'BCH'
    DOT = 'DOT'
    XRP = 'XRP'
    LTC = 'LTC'
    BNB = 'BNB'

class Coin:
    def __init__(self, name: Coins, exchange: ccxt.Exchange):
        self.name = name
        self.exchange = exchange
        
    def __str__(self):
        return str.upper(self.name)
    
    def get_bid_price(self):
        pass
    
    def get_ask_price(self):
        pass

class Ticker:
    pass

class Ratios:
    pass

if __name__ == '__main__':
    binance = ccxt.binance()
    print(Coin("BTC", binance))
    pass
