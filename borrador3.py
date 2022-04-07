import asyncio
from binance import AsyncClient, BinanceSocketManager

async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client, user_timeout=60)
    # start any sockets here, i.e a trade socket
    ts = bm.multiplex_socket(['ethusdt@ticker', 'btcusdt@ticker'])
    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            info = res["data"]
            print(info["b"], info["a"])

    await client.close_connection()

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())