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
Check out help:

::

    $ ckandr --help

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
    install_requires = ['certifi==2017.11.5', 'chardet==3.0.4', 'idna==2.6', 'requests==2.18.4', 'terminaltables==3.1.0', 'urllib3==1.22'],
    version = '0.3',
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
    keywords = 'bitcoin cryptocurrency ticker python cli price-tracker command-line',
    classifiers = [
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: End Users/Desktop',
      'License :: OSI Approved :: MIT License',
      'Operating System :: MacOS',
      'Operating System :: POSIX',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.6',
      'Topic :: Utilities'
      ],
)
