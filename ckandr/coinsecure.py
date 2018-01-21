import requests
from terminaltables import DoubleTable

class Coinsecure(object):
    """Main Coinsecure class"""

    def __init__(self):
        self.URL = "https://api.coinsecure.in/v1/exchange/ticker"
        self.title = "\033[94mCoinsecure CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin"
        }

    def get_coinsecure_rates(self,  crypto_curr='ALL'):
        print("")
        if crypto_curr is None:
            crypto_curr = "ALL"
        try:
            response = requests.get(self.URL)
        except Exception as e:
            print(type(e).__name__)
        if response and response.status_code == 200:
            coinsecure_data = response.json()
            coinsecure_list = []
            coinsecure_list.append(['CryptoCurrency Name', 'Symbol', 'Buy Rate', 'Sell Rate'] )
            for curr in self.supported_cryptos:
                if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                    coinsecure_list.append([self.supported_cryptos[curr], curr, coinsecure_data['message']['bid'], coinsecure_data['message']['ask'] ])
            table = DoubleTable(coinsecure_list)
            table.title = self.title
            table.inner_row_border = True
            print (table.table)
