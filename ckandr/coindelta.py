import requests
from terminaltables import DoubleTable

class Coindelta(object):
    """Main Coindelta class"""

    def __init__(self):
        self.URL = "https://coindelta.com/api/v1/public/getticker/"
        self.title = "\033[94mCoindelta CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin",
            "ETH": "Ethereum",
            "LTC": "LiteCoin",
            "OMG": "OmiseGO",
            "QTUM": "Qtum",
            "XRP": "Ripple",
            "BCH": "Bitcoin Cash"
        }

    def get_coindelta_rates(self, crypto_curr="ALL"):
        print ("")
        if crypto_curr is None:
            crypto_curr = "ALL"

        try:
            response = requests.get(self.URL)
        except Exception as e:
            print(type(e).__name__)
        if response and response.status_code == 200:
            coindelta_data = response.json()
            coindelta_list = []
            coindelta_list.append(['CryptoCurrency Name', 'Symbol', 'Buy Rate', 'Sell Rate'] )
            for curr in self.supported_cryptos:
                if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                    buyrate, sellrate = self.rates_from_response(curr, coindelta_data)
                    coindelta_list.append([self.supported_cryptos[curr], curr, buyrate, sellrate])
            table = DoubleTable(coindelta_list)
            table.title = self.title
            table.inner_row_border = True
            print (table.table)

    def rates_from_response(self, curr, coindelta_data):
        for cd_curr in coindelta_data:
            if curr.lower() in cd_curr['MarketName']:
                return cd_curr['Bid'], cd_curr['Ask']
