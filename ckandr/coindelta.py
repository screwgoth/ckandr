from . import utils


class Coindelta(object):
    """
    Main Coindelta class
    """

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
            "BCH": "Bitcoin Cash",
            "ZIL": "Zilliqa",
            "ZRX": "0x",
            "KNC": "KingN Coin",
            "EOS": "EOS",
            "ZEC": "ZCash",
            "NEO": "NEO",
            "GAS": "Gas",
            "TRX": "TRON",
            "GNT": "Golem",
            "BAT": "Basic Attention Token",
            "CVC": "Civic",
            "ENG": "Enigma",
            "MANA": "Decentraland",
            "SPANK": "SpankChain",
            "ICX": "ICON",
            "CND": "Cindicator",
            "AION": "Aion"
        }

    def get_coindelta_table(self, crypto_curr="ALL"):
        if crypto_curr is None:
            crypto_curr = "ALL"

        coindelta_data = utils.call_exchange_api(self.URL)
        coindelta_list = []
        coindelta_list.append(['CryptoCurrency Name', 'Symbol', 'Buy Rate', 'Sell Rate'] )
        for curr in self.supported_cryptos:
            if (self.supported_cryptos[curr].upper() == crypto_curr.upper() or crypto_curr == "ALL"):
                buyrate, sellrate = self.rates_from_response(curr, coindelta_data)
                coindelta_list.append([self.supported_cryptos[curr], curr, buyrate, sellrate])
        utils.draw_table(self.title, coindelta_list)

    def rates_from_response(self, curr, coindelta_data):
        for cd_curr in coindelta_data:
            if curr.lower() in cd_curr['MarketName']:
                return cd_curr['Bid'], cd_curr['Ask']
