import asyncio
import ccxt.async_support as ccxt 
from enum import Enum
#from typing import List

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

class Ticker:
    def __init__(self, c1: Coins, c2: Coins):
        self.fst_coin = c1
        self.snd_coin = c2
        self.symbol = str(c1)+"/"+str(c2)
        
    def __str__(self):
        return str.upper(self.name)
    
    def get_bid_price(self):
        """
        get the bid price in USDT
        """
        
        pass
    
    def get_ask_price(self):
        """
        get the ask price in USDT
        """
        pass

class Ratios:
    pass

async def run(exchange: ccxt.Exchange, tkr: Ticker):
    while True:
        #print('--------------------------------------------------------------')
        #print(exchange.iso8601(exchange.milliseconds()), 'fetching', symbol, 'ticker from', exchange.name)
        # this can be any call instead of fetch_ticker, really
        try:
            ticker = await exchange.fetch_ticker(tkr.symbol)
            print(exchange.iso8601(exchange.milliseconds()), 'fetched', tkr.symbol, 'ticker from', exchange.name)
            print(ticker)
        except ccxt.RequestTimeout as e:
            print('[' + type(e).__name__ + ']')
            print(str(e)[0:200])
            # will retry
        except ccxt.DDoSProtection as e:
            print('[' + type(e).__name__ + ']')
            print(str(e.args)[0:200])
            # will retry
        except ccxt.ExchangeNotAvailable as e:
            print('[' + type(e).__name__ + ']')
            print(str(e.args)[0:200])
            # will retry
        except ccxt.ExchangeError as e:
            print('[' + type(e).__name__ + ']')
            print(str(e)[0:200])
            break  # won't retry
    
if __name__ == '__main__':
    binance = ccxt.binance({
        'enableRateLimit': True,  # this option enables the built-in rate limiter
    })
    usdt = 'USDT'
    coin1 = 'BTC'
    coin2 = 'ETC'
    tickers = [Ticker(coin1,coin2), Ticker(coin2,coin1), Ticker(coin1,usdt), Ticker(coin2,usdt)]
    for ticker in tickers:
        asyncio.get_event_loop().run_until_complete(run(binance, ticker))
    pass

    