import pandas as pd

a = pd.read_excel(
    './MiniProjetosPessoaisPython/Pandas/Gastos e ganhos ano.xlsx',
    sheet_name='Abril')


INPMB = a['Maior Gasto'][0]

print(a['Custo'])
