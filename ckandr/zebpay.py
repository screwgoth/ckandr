import os
import requests
from terminaltables import DoubleTable

class Zebpay(object):
    """Main Zebpay Class"""

    def __init__(self):
        self.URL = "https://www.zebapi.com/api/v1/market/ticker/btc/inr"
        self.title = "\033[94mZebpay CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin"
        }


    def get_zebpay_rates(self,  crypto_curr='ALL'):
        print("")
        if crypto_curr is None:
            crypto_curr = "ALL"
        try:
            response = requests.get(self.URL)
        except Exception as e:
            print(type(e).__name__)
        if response and response.status_code == 200:
            zebpay_data = response.json()
            zebpay_list = []
            zebpay_list.append(['CryptoCurrency Name', 'Symbol', 'Buy Rate', 'Sell Rate'] )
            for curr in self.supported_cryptos:
                if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                    zebpay_list.append([self.supported_cryptos[curr], curr, zebpay_data['buy'], zebpay_data['sell'] ])
            table = DoubleTable(zebpay_list)
            table.title = self.title
            table.inner_row_border = True
            print (table.table)
