import ccxt 
from enum import Enum
from typing import List

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
        self.c1 = f'{c1.name}/USDT'
        self.c2 = f'{c2.name}/USDT'
        self.coins = [self.c1, self.c2]
        self.symbol = f'{c1.name}/{c2.name}'
        
    def show_info(self, exchange: ccxt.Exchange):
        """Shows the info asked by the exercice by fetching data from an exchange
        """
        asks = []
        bids = []
        now = None
        
        #this loop fetches the bid & ask price for each coin
        for coin in self.coins:
            try:
                info = exchange.fetch_ticker(coin)
                now = info["datetime"]
                asks += [info["ask"]] # sintax sugar for list appendation
                bids += [info["bid"]] 
            except Exception as e:
                print(f'Exception error: {str(e)}')
                return
        
        print("\033[H\033[J", end="") #clears the console
        print(f'''-----------------------------------
Date/Time: {now} 
Exchange: {str.upper(exchange.id)}
Ticker Cryptos: {self.symbol}
Ratio1: {bids[0]/asks[1]:.6f}
Ratio2: {bids[1]/asks[0]:.6f}             
''')
            
if __name__ == '__main__':
    
    #we instanciate the binance exchange client
    binance = ccxt.binance()
    
    #Asking the user for this choice of coins
    c1 = Coins.coin_from_input()
    c2 = Coins.coin_from_input()
    
    #We create our ticker instace
    ticker = Ticker(c1, c2)
    
    while True:
        #fetch & display the ratio between coins
        ticker.show_info(binance)

        
    
