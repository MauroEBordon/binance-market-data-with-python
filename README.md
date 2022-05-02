# Binance market data with python

Small project part of an interview process.

## Requirements

* `Python 3.6` or newer
* `ccxt` 
* `asyncio`
* either `python-binance` or `binance-connector` (they can't coexist in the same enviroment)
* Internet Connection


## How to run

* Run this on the repo directory:
```bash
pip install -r requirements.txt
```

* the `ws.py` & `ws_binance.py` implementations have incompatible libraries.
To avoid this you should either run:
```bash
pip uninstall python-binance; pip install binance-connector
python3 ws_binance.py
```  

or
```bash
pip uninstall binance-connector; pip install python-binance
python3 ws.py
```  

## Implementations

## `reduction.py`
the simpler & most straight foward implementation

## `ws.py`
Asyncronic implementation using `BinanceSocketManager` to connect to binance streams.
It only refresh the displayed data when theres a change in a coin's price.

## `ws_binance.py`
Stright foward implementation using Binance's own connector module.

## Useful documentation 
  
* ### For the main websocket implementation `ws.py`:  
    * [python-binance module documentation](https://python-binance.readthedocs.io/en/latest/websockets.html#binancesocketmanager-websocket-usage)
    * [Binance API docs](https://binance-docs.github.io/apidocs/spot/en/#individual-symbol-ticker-streams)  

  
* ### For `ws_binance.py`:
    I started using the [Binance documentation for websockets](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md) but i stumbled uopen a library that works as a connector to the [Binance Public API](https://github.com/binance/binance-spot-api-docs):
    
    * [binance-connector module documentation](https://github.com/binance/binance-connector-python)
        * special mention to: [`examples/websocket/spot/symbol_ticker.py`](https://github.com/binance/binance-connector-python/blob/master/examples/websocket/spot/symbol_ticker.py)

* ### For `ccxtpro` I followed this:
    * Manual (https://github.com/ccxt/ccxt/wiki/ccxt.pro.manual#)
    * Watch ticker python example (https://github.com/ccxt/ccxt/blob/b9f5441a44e740579c9274f84487b6ba7da8e107/examples/ccxt.pro/py/binance-futures-watch-order-book.py)  
     
