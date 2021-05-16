import requests
from bs4 import BeautifulSoup


class Html_getter:

    def __init__(self, topic):
        self.topic = topic

    def _response(self):
        return requests.get(f'http://pt.wikipedia.com/wiki/{self.topic}')

    @staticmethod
    def _BeautifulSoup(response):
        return BeautifulSoup(response.text, 'html.parser')


class Research(Html_getter):

    def __init__(self, topic):
        super().__init__(topic)
        self.bs = self._BeautifulSoup(self._response())
        self.texts = self._paragrafs(self.bs)
        self.titles = self._titles(self.bs)

    def _response(self):
        return requests.get(f'http://pt.wikipedia.com/wiki/{self.topic}')

    @staticmethod
    def _titles(bs_result):
        return bs_result.find_all(r'h2')

    @staticmethod
    def _paragrafs(bs_result):
        return bs_result.find_all('p')

    @staticmethod
    def _BeautifulSoup(response):
        return BeautifulSoup(response.text, 'html.parser')


def write(titles=[], texts=''):
    with open('research.txt', 'w', encoding='UTF-8') as f:
        for index in range(len(titles) - 1):
            if titles[index].text != 'Índice' and titles[index].text != "Menu de navegação" and titles[index].text != 'Ver também':
                if titles[index].text != 'Notas' and titles[index].text != 'Referências' and titles[index].text != 'Bibliografia':
                    f.write(titles[index].text.replace(
                        "[editar | editar código-fonte]", ''))
                    f.write('\n')
                    f.write(texts[index].text)
                    f.write('\n')


if __name__ == '__main__':
    superman_research = Research('hitler')

    texts = superman_research.texts
    titles = superman_research.titles

    write(titles, texts)
