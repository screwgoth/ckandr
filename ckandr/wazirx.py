from . import utils


class Wazirx(object):
    """
    Main Wazirx Class
    """

    def __init__(self):
        self.URL = "https://api.wazirx.com/api/v2/tickers"
        self.title = "\033[94mWazirx CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin",
            "ETH": "Ethereum",
            "XRP": "Ripple",
            "BCH": "Bitcoin Cash",
            "LTC": "LiteCoin",
            "TRX": "TRON",
            "DASH": "Dash"
        }

    def get_wazirx_table(self, crypto_curr='ALL'):
        if crypto_curr is None:
            crypto_curr = "ALL"

        wazirx_data = utils.call_exchange_api(self.URL)
        wazirx_list = []
        wazirx_list.append(['CryptoCurrency Name', 'Symbol', 'Price'] )
        for curr in self.supported_cryptos:
            if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                buyrate, sellrate = self.rates_from_response(curr, wazirx_data)
                wazirx_list.append([self.supported_cryptos[curr], curr, buyrate, sellrate])
        utils.draw_table(self.title, wazirx_list)

    def rates_from_response(self, curr, wazirx_data):
        inr_str = curr.lower()+'inr'
        w_buy = wazirx_data[inr_str]['buy']
        w_sell = wazirx_data[inr_str]['sell']
        return w_buy, w_sell
