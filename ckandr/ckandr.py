from ckandr.koinex import Koinex
from ckandr.zebpay import Zebpay

class Ckandr(object):
    """Main Ckandr class"""

    def __init__(self):
        self.main()

    def main(self):
        koinex = Koinex()
        koinex.get_koinex_rates()
        zebpay = Zebpay()
        zebpay.get_zebpay_rates()
