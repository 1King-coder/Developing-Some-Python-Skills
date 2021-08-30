import requests
import re
from bs4 import BeautifulSoup as BS


def response(link):
    return requests.get(link)


def bs(response):
    return BS(response.text, 'html.parser')


try:
    res = response(
        'http://localhost:3000/quero'
    )

    bs_r = bs(res)

    tag_list = bs_r.find_all("img")

    def html_tag(i):
        return re.findall(r'data-src=".*?"', f'{tag_list[i]}')[0]

    def limpa(i):
        return re.sub(r'data-src="*"', '', html_tag(i))

    def url(i):
        string = limpa(i)
        return string[:len(string)-1]

    for i in range(1, len(tag_list)+1):
        with open(f'./Dados/imagem_{i}.png', 'wb') as img:

            img.write(response(url(i-1)).content)

    print('DEU CERTOOOOOOOOOOOO')

except Exception as e:
    print(f'Deu merda {e}')
