from . import utils


class Zebpay(object):
    """
    Main Zebpay Class
    """

    def __init__(self):
        self.URL = "https://www.zebapi.com/api/v1/market/ticker/btc/inr"
        self.title = "\033[94mZebpay CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin"
        }

    def get_zebpay_table(self,  crypto_curr='ALL'):
        if crypto_curr is None:
            crypto_curr = "ALL"

        zebpay_data = utils.call_exchange_api(self.URL)
        zebpay_list = []
        zebpay_list.append(['CryptoCurrency Name', 'Symbol', 'Buy Rate', 'Sell Rate'] )
        for curr in self.supported_cryptos:
            if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                zebpay_list.append([self.supported_cryptos[curr], curr, zebpay_data['buy'], zebpay_data['sell'] ])
        utils.draw_table(self.title, zebpay_list)
