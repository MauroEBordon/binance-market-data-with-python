# binance-market-data-with-python

Small project part of an interview process for Quanticko Technologies.

## Read Along

This implementation used the `asyncio` library to concurrently ask the bid & ask price of binance crypto exchange of two different cryptocurrencies. It was important to follow an Object Oriented Design so the following classes were created:


```python
class Coins(str, Enum):
    """
    "Enumerated" class to define the "domain" (the selected cryptos in the exercice)
    it has the advantage to use strings as the alphabet in the "enumeration".
    """
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
        """
        Asks for user input until it matches one of our cryptos
        """
```

```python
class Ticker:
    """
    From this class is that we extract & display the requested data.
    Much of its inner mechanisms are to handle concurrent requests to the binance exchange API.
    """
    async def run_loops(self, asyncio_loop: AbstractEventLoop):
        
    async def exchange_loop(self, 
           
    async def get_prices_loop(self, symbol: str):
```

## Requirements

* Python 3.6 or newer
* ccxt 
* asyncio
* Internet Connection


## Useful documentation
* https://github.com/ccxt/ccxt/blob/master/examples/py
    * async-fetch-many-orderbooks-continuously.py
    * async-binance-fetch-ticker-continuously.py
  