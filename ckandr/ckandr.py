import argparse
import sys
from .koinex import Koinex
from .zebpay import Zebpay
from .unocoin import Unocoin
from .coindelta import Coindelta
from .coinsecure import Coinsecure
from terminaltables import DoubleTable

class Ckandr(object):
    """Main Ckandr class"""

    def __init__(self):
        self.supported_exchanges = ["koinex", "zebpay", "unocoin", "coindelta", "coinsecure"]
        parser = argparse.ArgumentParser(description="Command-line application to fetch latest cryptocurrency prices from Indian exchanges")
        parser.add_argument('-v', '--version', action='version', version="0.3")
        parser.add_argument('-e', '--exchange', dest='exchange', help='Name of the Exchange whose rates you want to checkout. Eg., Koinex, Zebpay, etc.')
        parser.add_argument('-c', '--cryptocurrency', dest='crypto', help='Name of the Cryptocurrency')
        parser.add_argument('-l', '--list', help='List supported Cryptocurrency Exchanges', dest='list', action='store_true')
        self.args = parser.parse_args()
        self.main()

    def main(self):
        if self.args.list:
            self.list_exchanges()
        if self.args.exchange:
            exchange = self.args.exchange
        else:
            exchange = "ALL"
        if ("KOINEX" in exchange.upper() or "ALL" in exchange.upper()):
            koinex = Koinex()
            koinex.get_koinex_rates(self.args.crypto)
        if ("ZEBPAY" in exchange.upper() or "ALL" in exchange.upper()):
            zebpay = Zebpay()
            zebpay.get_zebpay_rates(self.args.crypto)
        if ("COINDELTA" in exchange.upper() or "ALL" in exchange.upper()):
            coindelta = Coindelta()
            coindelta.get_coindelta_rates(self.args.crypto)
        if ("COINSECURE" in exchange.upper() or "ALL" in exchange.upper()):
            coinsecure = Coinsecure()
            coinsecure.get_coinsecure_rates(self.args.crypto)
        if ("UNOCOIN" in exchange.upper() or "ALL" in exchange.upper()):
            unocoin = Unocoin()
            unocoin.get_unocoin_rates(self.args.crypto)

    def list_exchanges(self):
        """List supported Cryptocurrency Exchanges"""
        exchanges_list = []
        exchanges_list.append(['Supported'])
        for ex in self.supported_exchanges:
            tmp_list = []
            tmp_list.append(ex)
            exchanges_list.append(tmp_list)
        table = DoubleTable(exchanges_list)
        table.title = "\033[94mExchanges\033[0m"
        table.inner_row_border = True
        print (table.table)
        sys.exit(0)
