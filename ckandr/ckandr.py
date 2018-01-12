from ckandr.koinex import Koinex

class Ckandr(object):
    """Main Ckandr class"""

    def __init__(self):
        self.main()

    def main(self):
        koinex = Koinex()
        koinex.get_koinex_rates()
