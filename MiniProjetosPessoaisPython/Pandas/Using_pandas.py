import requests
from bs4 import BeautifulSoup as BS
import pandas as pd


def response(link):
    return requests.get(link)


def bs(response):
    return BS(response.text, 'html.parser')


response = response('https://github.com/KaweMaximo')
bs_r = bs(response)

print(bs_r.find_all(class_='text-bold color-text-primary')[0].text)
