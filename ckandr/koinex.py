from . import utils


class Koinex(object):
    """
    Main Koinex Class
    """

    def __init__(self):
        self.URL = "https://koinex.in/api/ticker"
        self.title = "\033[94mKoinex CryptoCurrency Rates\033[0m"
        self.supported_cryptos = {
            "BTC": "BitCoin",
            "ETH": "Ethereum",
            "XRP": "Ripple",
            "BCH": "Bitcoin Cash",
            "LTC": "LiteCoin",
            "EOS": "EOS",
            "NEO": "NEO",
            "MIOTA": "IOTA",
            "TRX": "TRON",
            "OMG": "OmiseGO",
            "AE": "Aeternity",
            "ZRX": "0x",
            "GNT": "Golem",
            "BAT": "Basic Authentication Token",
            "GAS": "GAS",
            "REQ": "Request",
            "AION": "Aion",
            "NCASH": "Nucleus Vision",
            "XLM": "Stellar"
        }

    def get_koinex_table(self, crypto_curr='ALL'):
        if crypto_curr is None:
            crypto_curr = "ALL"

        koinex_data = utils.call_exchange_api(self.URL)
        koinex_list = []
        koinex_list.append(['CryptoCurrency Name', 'Symbol', 'Price'] )
        for curr in self.supported_cryptos:
            if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                koinex_list.append([self.supported_cryptos[curr], curr, koinex_data['prices'][curr]])
        utils.draw_table(self.title, koinex_list)
