import asyncio
import ccxtpro

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
        self.c1 = f'{c1.name}/USDT'
        self.c2 = f'{c2.name}/USDT'
        self.coins = [self.c1, self.c2]
        self.symbol = f'{c1.name}{c2.name}'
        
    async def show_info(self, exchange: ccxtpro.Exchange):
        """Infinitely shows the info asked by the exercice by fetching data from an exchange
        """
        if not exchange.has['watchOrderBook']:
            print("este exchange no soporta websockets")
            return
        
        asks = []
        bids = []
        now = None
        
        #this loop fetches the bid & ask price for each coin
        async for coin in self.coins:
            try:
                info = await exchange.watch_order_book(coin)
                now = info["datetime"]
                asks += [info['asks'][0]]
                bids += [info['bids'][0]]
            except Exception as e:
                #print(f'exception error: {str(e)}')
                break 
        
        print(f'''                -----------------------------------
            Date/Time: {now} 
            Exchange: {str.upper(exchange.id)}
            Ticker Cryptos: {self.symbol}
            Ratio1: {bids[0]/asks[1]:.6f}
            Ratio2: {bids[1]/asks[0]:.6f}             
            ''')
        

async def main():
    
    #Instancing a binance ccxtpro.Exchange object 
    binance = ccxtpro.binance({
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future',
        },
    })
    
    #Asking the user for this choice of coins
    c1 = Coins.coin_from_input()
    c2 = Coins.coin_from_input()

    #We create our ticker instace
    ticker = Ticker(c1, c2)
    
    while True:
        try:
            await ticker.show_info(binance)
        except Exception as e:
            print(type(e).__name__, str(e))
            
    await binance.close()


if __name__ == '__main__':
    
    #we create an eventloop 
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    


        
    
