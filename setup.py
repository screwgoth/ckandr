# Ckandr

from setuptools import setup

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """
About
-----
ckandr is a python-based command-line application Cryptocurrency prices from popular Indian cryptocurrency exchanges.
There are already some great command-line cryptocurrency price ticker tools like `Coinmon`_ and it's python port `Pycoinmon`_.
ckandr is heavily inspired by both these projects.
However, both these projects get their data from `CoinMarketCap`_'s API. This is of no use to Indian investors who are investing through Indian exchanges like `Koinex`_, `ZebPay`_ and others.
ckandr aims to solve this problem by fetching prices from these sites (and more to follow soon).

For all you non-Hindi speaking people out there, ckandr is a play on a Hindi word, Sikander, which means a "warrior" or "defender". And the pseudo-acronym of ckandr, Crypto KA Naya Desi Rate, just means the latest price of cryptocurrencies in Rupees(INR).

Usage
-----
It's as easy as:

::

    $ ckandr

Screenshot
----------

.. figure:: https://raw.githubusercontent.com/screwgoth/ckandr/master/ckandr_screenshot.png
   :alt: ckandr screenshot

.. _Coinmon : https://github.com/bichenkk/coinmon
.. _Pycoinmon : https://github.com/RDCH106/pycoinmon
.. _Koinex : http://koinex.in
.. _ZebPay : http://zebpay.com
.. _CoinMarketCap: https://coinmarketcap.com/

    """

setup(
    name = 'ckandr',
    packages = ['ckandr'],
    install_requires = requirements(),
    version = '0.1',
    license = 'MIT',
    description = 'Cryptocurrency Ka Naya Desi Rate : Cryptocurrency prices from Indian exchanges',
    long_description= long_description,
    author = 'Raseel Bhagat',
    author_email = 'raseelbhagat@gmail.com',
    url = 'https://github.com/screwgoth/ckandr',
    download_url = 'https://github.com/screwgoth/ckandr/archive/0.1.tar.gz',
    entry_points={
        'console_scripts': ['ckandr=ckandr.main:main'],
    },
    #scripts=['ckandr/main.py'],
    keywords = 'bitcoin cryptocurrency ticker python cli price-tracker command-line',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)
