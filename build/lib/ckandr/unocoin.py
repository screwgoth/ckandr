import os
import requests
from terminaltables import DoubleTable

class Unocoin(object):
    """Main Unocoin Class"""

    def __init__(self):
        # The following Unocoin client id and secret only have access for prices
        self.client_id = "PXOHP8NOXL"
        self.client_secret = "1c1d44de-9323-491b-a01e-c1d021fc182a"
        self.URL = "https://www.unocoin.com/trade?all"
        self.prices_URL = "https://www.unocoin.com/api/v1/general/prices"
        self.auth_URL = "https://www.unocoin.com/oauth/token"
        self.title = "\033[94mUnocoin CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin"
        }


    def get_unocoin_rates(self, crypto_curr='ALL'):
        print("\033[37mWait for it ...\033[0m")
        access_token = self.get_unocoin_access_token()
        if crypto_curr is None:
            crypto_curr = "ALL"
        try:
            authorization = "Bearer {}".format(access_token)
            headers = {
                "Content-Type":"application/json",
                "Authorization": authorization
            }
            response = requests.post(self.prices_URL, headers=headers)
        except Exception as e:
            print(response.status_code, response.text, type(e).__name__)
            return
        if response and response.status_code == 200:
            unocoin_data = response.json()
            unocoin_list = []
            unocoin_list.append(['CryptoCurrency Name', 'Symbol', 'Buy Rate', 'Sell Rate'] )
            for curr in self.supported_cryptos:
                if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                    #unocoin_list.append([self.supported_cryptos[curr], curr, unocoin_data['buy'], unocoin_data['sell'] ])
                    unocoin_list.append([self.supported_cryptos[curr], curr, unocoin_data['buybtc'], unocoin_data['sellbtc'] ])
            table = DoubleTable(unocoin_list)
            table.title = self.title
            table.inner_row_border = True
            print (table.table)

    def get_unocoin_access_token(self):
        """Get Unocoin Access token"""
        payload = {
            "grant_type":"client_credentials",
            "access_lifetime":"30"
        }
        resp = requests.post(self.auth_URL, data=payload, auth=(self.client_id, self.client_secret))
        respj = resp.json()
        return respj['access_token']
