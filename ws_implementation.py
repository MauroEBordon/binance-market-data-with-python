import asyncio
import time
import os
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

from enum import Enum
    
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
        self.symbol = f'{c1.name}{c2.name}'
        self.bid1 = 1
        self.bid2 = 1
        self.ask1 = 1
        self.ask2 = 1
        self.ratio1 = 1
        self.ratio2 = 1
        
    def data_handler(self, message):
        print(message)
        


        #print(bid)
        #print(ask)
        #print(self.bid1, self.bid2, self.ask1, self.ask2)

        #time.sleep(2)
        # print("Date/Time: ")
        #print("Exchange: Binance")
        #print(f"Ticker Cryptos: {self.symbol}")
        #os.sleep(2)
        #print(f"Ratio 2: {self.bid2:.6f}")
        
#         print(f'''-----------------------------------
# Date/Time:  
# Exchange: Binance
# Ticker Cryptos: {self.symbol}
# Ratio1: {self.bid1/self.ask2:.6f}
# Ratio2: {self.bid2/self.ask1:.6f}             
# ''')





if __name__ == '__main__':
    
    binance = Client(stream_url="wss://testnet.binance.vision")
    
    #Asking the user for this choice of coins
    c1 = Coins.coin_from_input()
    c2 = Coins.coin_from_input()

    #We create our ticker instace
    ticker = Ticker(c1, c2)
    
    binance.start()
    
    binance.ticker(
        symbol=ticker.symbol,
        id=1,
        callback=ticker.data_handler
    )

    binance.instant_subscribe(
    ticker.coins, callback=ticker.data_handler
)
    time.sleep(2000)
    
    binance.stop()
    


        
    
