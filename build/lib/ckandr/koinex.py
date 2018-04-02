import os
import requests
from terminaltables import DoubleTable

class Koinex(object):
    """Main Koinex Class"""

    def __init__(self):
        self.URL = "https://koinex.in/api/ticker"
        self.title = "\033[94mKoinex CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin",
            "ETH": "Ethereum",
            "XRP": "Ripple",
            "BCH": "Bitcoin Cash",
            "LTC": "LiteCoin"
        }

    def call_exchange_api(self,crypto_curr='ALL'):
        try:
            response = requests.get(self.URL)
        except Exception as e:
            print(type(e).__name__)
        if response and response.status_code == 200:
            resp_data = response.json()
            return resp_data


    def get_koinex_table(self, crypto_curr='ALL'):
        os.system('clear')
        if crypto_curr is None:
            crypto_curr = "ALL"

        koinex_data = self.call_exchange_api()
        koinex_list = []
        koinex_list.append(['CryptoCurrency Name', 'Symbol', 'Price'] )
        for curr in self.supported_cryptos:
            if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                koinex_list.append([self.supported_cryptos[curr], curr, koinex_data['prices'][curr]])
        table = DoubleTable(koinex_list)
        table.title = self.title
        table.inner_row_border = True
        print (table.table)
