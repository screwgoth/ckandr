from .koinex import Koinex
from .zebpay import Zebpay
from .unocoin import Unocoin

class Ckandr(object):
    """Main Ckandr class"""

    def __init__(self):
        self.main()

    def main(self):
        koinex = Koinex()
        koinex.get_koinex_rates()
        zebpay = Zebpay()
        zebpay.get_zebpay_rates()
        #unocoin = Unocoin()
        #unocoin.get_unocoin_rates()
