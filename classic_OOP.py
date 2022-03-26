import ccxt.async_support as ccxt 
from asyncio import gather, get_event_loop
from enum import Enum
#from typing import List


class Coins(str, Enum):
#TRANSFORMAR ESTO EN OOP BASICAMENTE
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


async def symbol_loop(exchange, symbol):
    print('Starting the', exchange.id, 'symbol loop with', symbol)
    while True:
        try:
            orderbook = await exchange.fetch_order_book(symbol)
            now = exchange.milliseconds()
            print(exchange.iso8601(now), exchange.id, symbol, orderbook['asks'][0], orderbook['bids'][0])

            # --------------------> DO YOUR LOGIC HERE <------------------

        except Exception as e:
            print(str(e))
            # raise e  # uncomment to break all loops in case of an error in any one of them
            break  # you can break just this one loop if it fails

async def exchange_loop(asyncio_loop, exchange_id, symbols):
    print('Starting the', exchange_id, 'exchange loop with', symbols)
    exchange = getattr(ccxt, exchange_id)({
        'enableRateLimit': True,
        'asyncio_loop': asyncio_loop,
    })
    loops = [symbol_loop(exchange, symbol) for symbol in symbols]
    await gather(*loops)
    await exchange.close()


async def main(asyncio_loop):
    exchanges = {
        'binance': ['BTC/USDT', 'ETH/USDT', 'ETH/BTC'],
    }
    loops = [exchange_loop(asyncio_loop, exchange_id, symbols) for exchange_id, symbols in exchanges.items()]
    await gather(*loops)


if __name__ == '__main__':
    asyncio_loop = get_event_loop()
asyncio_loop.run_until_complete(main(asyncio_loop))
    
# if __name__ == '__main__':
#     binance = ccxt.binance({
#         'enableRateLimit': True,  # this option enables the built-in rate limiter
#     })
#     usdt = 'USDT'
#     coin1 = 'BTC'
#     coin2 = 'ETC'
#     tickers = [Ticker(coin1,coin2), Ticker(coin2,coin1), Ticker(coin1,usdt), Ticker(coin2,usdt)]
#     for ticker in tickers:
#         asyncio.get_event_loop().run_until_complete(run(binance, ticker))
#     pass

