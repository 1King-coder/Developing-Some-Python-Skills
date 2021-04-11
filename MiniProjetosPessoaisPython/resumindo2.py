import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Html_getter(ABC):
    @staticmethod
    @abstractmethod
    def _response(topic): pass

    @staticmethod
    @abstractmethod
    def _BeautifulSoup(response): pass


class Research(Html_getter):
    def __init__(self, topic):
        self.texts = self._paragrafs(
            self._BeautifulSoup(self._response(topic)))
        self.titles = self._titles(
            self._BeautifulSoup(self._response(topic)))

    @staticmethod
    def _response(topic):
        return requests.get(f'http://pt.wikipedia.com/wiki/{topic}')

    @staticmethod
    def _titles(bs_result):
        return bs_result.find_all(r'h2')

    @staticmethod
    def _paragrafs(bs_result):
        return bs_result.find_all('p')

    @staticmethod
    def _BeautifulSoup(response):
        return BeautifulSoup(response.text, 'html.parser')


if __name__ == '__main__':
    superman_research = Research('superman')

    texts = superman_research.texts
    titles = superman_research.titles
