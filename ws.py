import asyncio
from datetime import datetime
from binance import AsyncClient, BinanceSocketManager

from enum import Enum
    

#desarrollar con legibilidad y simplicidad.
#pensarlo al revez, como alguien que no tiene el enunciado del problema
#para competencia de comprencion


class Coins(str, Enum):
    """Enumerated class to filter the selected cryptos in the exercice.
It has the advantage to use strings as the alphabet in the "enumeration".
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
        """Checks input until a valid coin is entered
Returns:
    the ticker name of a valid coin
        """
        coin = None
        while coin == None:
            try:
                coin = Coins(str.upper(input(
                    f"Enter a valid coin {[c.value for c in Coins]:}"
                )))
                break   
            except ValueError:
                print("not a valid crypto")  
                continue
        return coin

class Ticker:
    """This class handles the data extraction & the display of the asked information
    """
    def __init__(self, c1: Coins, c2: Coins):
        self.c1 = f'{str.lower(c1.name)}usdt@ticker'
        self.c2 = f'{str.lower(c2.name)}usdt@ticker'
        self.coins = [self.c1, self.c2]
        self.symbol = f'{c1.name}/{c2.name}'
        self.bid1 = 0
        self.bid2 = 0
        self.ask1 = 1
        self.ask2 = 1
        
    async def show_info(self, trade_socket):
        """Shows the info only when there has been a change on bid or ask price of any of it's coins
        """
        res = await trade_socket.recv()
        
        #translate the timestamp to an actual date
        now = datetime.fromtimestamp(res["data"]["E"]//1000) #this converts milliseconds to seconds
        
        bid = float(res["data"]["b"])
        ask = float(res["data"]["a"]) 
        
        #if the data is actually the same, we dont need to show anything
        if res["stream"] == self.c1 and self.bid1 == bid and self.ask1 == ask:
            return
        if res["stream"] == self.c2 and self.bid2 == bid and self.ask2 == ask:
            return

        #refresh price values
        if res["stream"] == self.c1:
            self.bid1 = bid
            self.ask1 = ask
        elif res["stream"] == self.c2:
            self.bid2 = bid
            self.ask2 = ask    
        
        #we wont show info until we can fetch data from both streams
        if self.bid1 == 0 or self.bid2 == 0:
                return
            
        print("\033[H\033[J", end="") #clears the console
        print(f'''-----------------------------------
Date/Time: {now}
Exchange: Binance
Ticker Cryptos: {self.symbol}
Ratio1: {self.bid1/self.ask2:.6f}
Ratio2: {self.bid2/self.ask1:.6f}      
-----------------------------------     
''')


async def main(loop):
    
    client = await AsyncClient.create()
    binance = BinanceSocketManager(client, user_timeout=10)
    
    #Asking the user for this choice of coins
    c1 = Coins.coin_from_input()
    c2 = Coins.coin_from_input()

    #We create our ticker instace
    ticker = Ticker(c1, c2)
    
    #create our socket
    trade_socket = binance.multiplex_socket(ticker.coins)
    
    async with trade_socket as tscm:
        while True:
            try:
                await ticker.show_info(tscm)
            except Exception as e:
                #print(f'exception error: {str(e)}')
                break 

    await client.close_connection()

if __name__ == '__main__':
    
    #we create an eventloop 
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(loop))