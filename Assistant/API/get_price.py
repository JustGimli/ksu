from configparser import ConfigParser
import requests
from requests.exceptions import Timeout, ConnectionError, TooManyRedirects

import json

def get_currency(query='USD')-> dict:
    API_KEY = _get_api_token("exchange_api")

    if query == 'USD' or query == "EUR":
        CURNCY = query
    else: 
        result = {
            "title": "Error: unknown currency",
            "price": "None"
        }
        return result

    try:
        data = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{CURNCY}/BYN").json()        
        byn_price = data.get("conversion_rate")

        result = {
            "title": query,
            "price": byn_price
        }
        
        print(byn_price)
    except (TooManyRedirects, Timeout, ConnectionError) as e:
        print(e) # raise connection handler
    except Exception as e:
        print("Unknown error")


def _get_api_token(name)->str:
    conf = ConfigParser()
    conf.read('./Assistant/storage/config.ini')

    return conf['currency'][f'{name}']

