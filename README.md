# ckandr (Crypto KA Naya Desi Rate)
************************************
**ckandr** is a python-based command-line application Cryptocurrency prices from popular Indian cryptocurrency exchanges.
There are already some great command-line cryptocurrency price ticker tools like [Coinmon](https://github.com/bichenkk/coinmon) and it's python port [Pycoinmon](https://github.com/RDCH106/pycoinmon). **ckandr** is heavily inspired by both these projects.
However, both these projects get their data from [CoinMarketCap](http://coinmarketcap.com)'s API. This is of no use to Indian investors who are investing through Indian exchanges like [Koinex](http://koinex.in), [ZebPay](http://zebpay.com) and others.
**ckandr** aims to solve this problem by fetching prices from these sites. (and more to follow soon)

_For all you non-Hindi speaking people out there, ckandr is a play on a Hindi word, Sikander, which means a "warrior" or "defender". And the pseudo-acronym of ckandr, Crypto KA Naya Desi Rate, just means the latest price of cryptocurrencies in Rupees._


## Installation
It can be done in a couple of ways

### The easy way
```
$ pip install ckandr
```
And if you want to upgrade
```
$ pip install ckandr --upgrade
```

### Installing from source
Clone the Repo
```
git clone git@github.com:screwgoth/ckandr.git
cd ckandr
```

Setup a virtual environement (optional)
```
virtualenv -p python3 .venv36
```

Install the requirements
```
pip install -r requirements.txt
```

Install ckandr
```
pip install .
```

If you ever pull the latest code, you can just upgrade
```
pip install . --upgrade
```

## Usage
Checkout help:
```
ckandr --help
```

## Screenshot
![ckandr_screenshot](https://raw.githubusercontent.com/screwgoth/ckandr/master/ckandr_screenshot.png)

## TODO
Please refer to the `TODO.md` file for the list of things to do for _world domination_

## Licensing
The code in this project is licensed under the MIT License.
Please refer to the `LICENSE` file for more information
