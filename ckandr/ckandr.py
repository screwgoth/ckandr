from ckandr.koinex import Koinex
from ckandr.zebpay import Zebpay
from ckandr.unocoin import Unocoin

class Ckandr(object):
    """Main Ckandr class"""

    def __init__(self):
        self.main()

    def main(self):
        koinex = Koinex()
        koinex.get_koinex_rates()
        zebpay = Zebpay()
        zebpay.get_zebpay_rates()
        unocoin = Unocoin()
        unocoin.get_unocoin_rates()
