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
    def __init__(self, name: Coins):
        self.name = name
        
    def __str__(self):
        return str.upper(self.name)

class Ticker:
    pass


if __name__ == '__main__':
    print(Coin("BTC"))
    pass
