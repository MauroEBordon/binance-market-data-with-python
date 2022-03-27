import time
import ccxt.async_support as ccxt 
from asyncio import gather, get_event_loop, AbstractEventLoop
from enum import Enum
from typing import List


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
    def __init__(self, c1: Coins, c2: Coins, exchange_id='binance'):
        self.c1 = f'{c1}/USDT'
        self.c2 = f'{c2}/USDT'
        self.symbol = f'{c1}/{c2}'
        self.exchange = None
        self.exchange_id = exchange_id
        self.ticker = {}
        self.now = None
        self.bids = {}
        self.asks = {}
        
    async def run_loops(self, asyncio_loop: AbstractEventLoop):
        loops = [self.exchange_loop( asyncio_loop,
                               [self.c1, self.c2, self.symbol])]
        await gather(*loops)
        
    async def exchange_loop(self, asyncio_loop: AbstractEventLoop,  symbols: List[str]):
        self.exchange = getattr(ccxt, self.exchange_id)({
            'enableRateLimit': True,
            'asyncio_loop': asyncio_loop,
        })
        loops = [self.orderbook_loop(symbol) for symbol in symbols]
        await gather(*loops)
        await self.exchange.close()  
        
    async def orderbook_loop(self, symbol: str):
        while True:
            try:
                self.ticker = await self.exchange.fetch_ticker(symbol)
                
                self.now = self.ticker["datetime"]
                self.asks[symbol] = self.ticker['bid']
                self.bids[symbol] = self.ticker['ask']
                print(self)

            except Exception as e:
                print(str(e))
                # # raise e  # uncomment to break all loops in case of an error in any one of them
                break  # you can break just this one loop if it fails


    
    def __str__(self):
        return f'''-----
Date/Time: {self.now} 
Exchange: {str.upper(self.exchange.id)}
Ticker Cryptos: {self.symbol}
Ratio1: {self.bids[self.c1]/self.asks[self.c2]:.6f}
Ratio2: {self.bids[self.c2]/self.asks[self.c1]:.6f}
-----                
                '''


if __name__ == '__main__':
    #buscar que sea c1/c2 o c2/c1 es importante
    ticker = Ticker("ETH", "BTC")
    asyncio_loop = get_event_loop()
    asyncio_loop.run_until_complete(ticker.run_loops(asyncio_loop))
    
    
