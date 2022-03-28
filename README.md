# binance-market-data-with-python

Small project part of an interview process for Quanticko Technologies.

## Read Along




This implementation used the `asyncio` library to concurrently ask the bid & ask price of binance crypto exchange of two different cryptocurrencies. It was important to follow an Object Oriented Design so the following classes were created:

```python
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

    def coin_from_input():
    #
```

```python
class Ticker:
    async def run_loops(self, asyncio_loop: AbstractEventLoop):
        #
        
    async def exchange_loop(self, 
        #
           
    async def get_prices_loop(self, symbol: str):
        #
```


```python
from asyncio import gather, get_event_loop
    asyncio_loop = get_event_loop()
    asyncio_loop.run_until_complete(ticker.run_loops(asyncio_loop))
```

## Objects
* Coin
* Ticker

## Links Útiles

* https://github.com/ccxt/ccxt/blob/master/examples/py
    * async-fetch-many-orderbooks-continuously.py
    * https://github.com/ccxt/ccxt/blob/master/examples/py/async-binance-fetch-ticker-continuously.py
  