from datetime import datetime
import time
import logging


#desarrollar con legibilidad y simplicidad.
#pensarlo al revez, como alguien que no tiene el enunciado del problema
#para competencia de comprencion


from binance.lib.utils import config_logging
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
        self.symbol = f'{c1.name}/{c2.name}'
        self.bid1 = 0
        self.bid2 = 0
        self.ask1 = 1
        self.ask2 = 1

        
    def data_handler(self, res):
        
        try:
            now = datetime.fromtimestamp(res["data"]["E"]//1000)
            bid = float(res["data"]["b"])
            ask = float(res["data"]["a"])
            if res["stream"] == self.c1 and self.bid1 == bid and self.ask1 == ask:
                return
            if res["stream"] == self.c2 and self.bid2 == bid and self.ask2 == ask:
                return

            if res["stream"] == self.c1:
                self.bid1 = bid
                self.ask1 = ask

            elif res["stream"] == self.c2:
                self.bid2 = bid
                self.ask2 = ask    

            if self.bid1 == 0 or self.bid2 == 0:
                return
            
            print("\033[H\033[J", end="")
            print(f'''-----------------------------------
Date/Time: {now}
Exchange: Binance
Ticker Cryptos: {self.symbol}
Ratio1: {self.bid1/self.ask2:.6f}
Ratio2: {self.bid2/self.ask1:.6f}      
-----------------------------------     
''')
            
        except Exception as e:
            print(e)


if __name__ == '__main__':
    
    config_logging(logging, logging.DEBUG)
    
    binance = Client(stream_url="wss://testnet.binance.vision")
    
    #Asking the user for this choice of coins
    c1 = Coins.coin_from_input()
    c2 = Coins.coin_from_input()

    #We create our ticker instace
    ticker = Ticker(c1, c2)
    
    binance.start()
    
    
    binance.instant_subscribe(
    ticker.coins, callback=ticker.data_handler
)
    while True:
        pass
    
    binance.stop()
    


        
    
