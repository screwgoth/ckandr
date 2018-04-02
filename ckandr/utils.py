import requests
from terminaltables import DoubleTable


def call_exchange_api(url):
    try:
        response = requests.get(url)
    except Exception as e:
        print(type(e).__name__)
    if response and response.status_code == 200:
        resp_data = response.json()
        return resp_data


def draw_table(title, exchange_list):
    table = DoubleTable(exchange_list)
    table.title = title
    table.inner_row_border = True
    print(table.table)
