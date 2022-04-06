# import ccxtpro
# from asyncio import get_event_loop


# async def main():
#     exchange = ccxtpro.binance({
#         'enableRateLimit': True,
#         'options': {
#             'defaultType': 'future',
#         },
#     })
#     symbol = 'BTC/USDT'
#     while True:
#         try:
#             orderbook = await exchange.watch_order_book(symbol)
#             print(orderbook['bids'][0], orderbook['asks'][0])
#         except Exception as e:
#             print(type(e).__name__, str(e))
#     await exchange.close()


# loop = get_event_loop()
# loop.run_until_complete(main())

# import ccxt as ccxtpro
# import asyncio

# async def main():
#     exchange = ccxtpro.binance({'enableRateLimit': True})
#     while True:
#         orderbook = await exchange.watch_order_book('ETH/BTC')
#         print(orderbook['asks'][0], orderbook['bids'][0])

# asyncio.get_event_loop().run_until_complete(main())

import asyncio
from binance import AsyncClient, BinanceSocketManager


async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    ts = bm.trade_socket('BNBBTC')
    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            print(res)

    await client.close_connection()

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())