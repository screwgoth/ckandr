import os
import requests
from terminaltables import DoubleTable

class Unocoin(object):
    """Main Unocoin Class"""

    def __init__(self):
        self.URL = "https://www.unocoin.com/trade?all"
        self.title = "Unocoin CryptoCurrency Rates"
        self.cryptos = {
            "BTC": "BitCoin"
        }


    def get_unocoin_rates(self):
        print("")
        try:
            response = requests.get(self.URL)
        except Exception as e:
            print(type(e).__name__)
        if response and response.status_code == 200:
            unocoin_data = response.json()
            unocoin_list = []
            unocoin_list.append(['CryptoCurrency Name', 'Symbol', 'Buy Rate', 'Sell Rate'] )
            for curr in self.cryptos:
                unocoin_list.append([self.cryptos[curr], curr, unocoin_data['buy'], unocoin_data['sell'] ])
            table = DoubleTable(unocoin_list)
            table.title = self.title
            table.inner_row_border = True
            print (table.table)
