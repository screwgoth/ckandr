# Ckandr

from setuptools import setup

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


setup(
    name = 'ckandr',
    packages = ['ckandr'],
    install_requires = requirements(),
    version = '0.1',
    license = 'MIT',
    description = 'Cryptocurrency Ka Napaakh Desi Rate : Cryptocurrency prices from Indian websites',
    long_description= 'Cryptocurrency Ka Napaakh Desi Rate : Cryptocurrency prices from Indian websites',
    author = 'Raseel Bhagat',
    author_email = 'raseelbhagat@gmail.com',
    url = 'https://github.com/screwgoth/ckandr',
    download_url = 'https://github.com/screwgoth/ckandr',
    entry_points={
        'console_scripts': ['ckandr=ckandr.main:main'],
    },
    #scripts=['ckandr/main.py'],
    keywords = 'bitcoin cryptocurrency crypto ticker python cli price-tracker command-line',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)
