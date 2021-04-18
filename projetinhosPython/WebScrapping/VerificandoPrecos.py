from pathlib import Path
import os
import requests
from bs4 import BeautifulSoup
import re
import openpyxl


DATA_FILE = "C:/Programação/VSCode/CursoPython/projetinhosPython/WebScrapping/Dados/comparaPrecos.xlsx"


class SalvaEComparaPreco:
    def __init__(self, response, planilha_path):
        self.preco = response
        self.planilha_path = planilha_path
        self.planilha = openpyxl.load_workbook(planilha_path)

        self._seta_preco()
        self._compara_precos()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, response):
        bs = BeautifulSoup(response.text, 'html.parser')
        self._preco = bs.find_all(class_="price-tag-fraction")[0].text

    def _seta_preco(self):
        self.planilha['precos']['b1'].value = float(self.preco)
        self.planilha.save(self.planilha_path)

    def _compara_precos(self):
        comparacao_preco = float(self.planilha['precos']['b1'].value)
        preco_antigo = float(self.planilha['precos']['a1'].value)

        if comparacao_preco != preco_antigo:
            print(f'tem desconto! deconto: {preco_antigo - comparacao_preco}')
        else:
            print('tudo padrão')


BASE_URL = ["https://www.mercadolivre.com.br/teclado-gamer-hyperx-alloy-origins-qwerty-red-portugus-brasil-preto-com-luz-rgb/p/MLB15580684#reco_item_pos=0&reco_backend=machinalis-v2p-pdp-boost-v2-tracksv2&reco_backend_type=low_level&reco_client=vip-v2p&reco_id=d53c0ab7-f607-45ca-9ce4-0751df003e4e",
            "https://www.mercadolivre.com.br/teclado-gamer-hyperx-alloy-fps-pro-qwerty-cherry-mx-red-ingls-us-preto-com-luz-vermelho/p/MLB9038151#reco_item_pos=1&reco_backend=machinalis-pdp&reco_backend_type=low_level&reco_client=pdp-v2p&reco_id=cc4074e3-5f86-4008-85b6-2ec73be9cc84",
            "https://www.mercadolivre.com.br/teclado-gamer-redragon-kumara-k552-qwerty-outemu-red-portugus-brasil-preto-com-luz-vermelho/p/MLB15104680#reco_item_pos=0&reco_backend=machinalis-pdp&reco_backend_type=low_level&reco_client=pdp-v2p&reco_id=cc4074e3-5f86-4008-85b6-2ec73be9cc84",
            "https://www.mercadolivre.com.br/teclado-gamer-hyperx-alloy-origins-core-qwerty-red-portugus-brasil-preto-com-luz-rgb/p/MLB15761144#reco_item_pos=2&reco_backend=machinalis-pdp&reco_backend_type=low_level&reco_client=pdp-v2p&reco_id=cc4074e3-5f86-4008-85b6-2ec73be9cc84"]

for i in BASE_URL:
    SalvaEComparaPreco(requests.get(i), DATA_FILE)
