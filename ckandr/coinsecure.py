from . import utils

class Coinsecure(object):
    """
    Main Coinsecure class
    """

    def __init__(self):
        self.URL = "https://api.coinsecure.in/v1/exchange/ticker"
        self.title = "\033[94mCoinsecure CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin"
        }

    def get_coinsecure_table(self,  crypto_curr='ALL'):
        print("")
        if crypto_curr is None:
            crypto_curr = "ALL"

        coinsecure_data = utils.call_exchange_api(self.URL)
        coinsecure_list = []
        coinsecure_list.append(['CryptoCurrency Name', 'Symbol', 'Buy Rate', 'Sell Rate'] )
        for curr in self.supported_cryptos:
            if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                coinsecure_list.append([self.supported_cryptos[curr], curr, coinsecure_data['message']['bid'], coinsecure_data['message']['ask'] ])
        utils.draw_table(self.title, coinsecure_list)
