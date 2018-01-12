import os
import requests
from terminaltables import DoubleTable

class Koinex(object):
    """Main Koinex Class"""

    def __init__(self):
        self.URL = "https://koinex.in/api/ticker"
        self.title = "Koinex CryptoCurrency Rates"
        self.cryptos = {
            "BTC": "BitCoin",
            "ETH": "Ethereum",
            "XRP": "Ripple",
            "BCH": "Bitcoin Cash",
            "LTC": "LiteCoin"
        }


    def get_koinex_rates(self):
        print ("Getting data from Koinex")
        print (self.URL)
        os.system('clear')
        try:
            response = requests.get(self.URL)
        except Exception as e:
            print(type(e).__name__)
        if response and response.status_code == 200:
            koinex_data = response.json()
            koinex_list = []
            koinex_list.append(['CryptoCurrency Name', 'Symbol', 'Price'] )
            for curr in self.cryptos:
                koinex_list.append([self.cryptos[curr], curr, koinex_data['prices'][curr]])
            table = DoubleTable(koinex_list)
            table.title = self.title
            table.inner_row_border = True
            print (table.table)
