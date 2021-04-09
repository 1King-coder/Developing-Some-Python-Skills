# Metacaracteres -> . ^ $ * + ? { } [ ] \ | ( )

# | -> OU
# . -> Qualquer caractere (com exceção da quebra de linha)
# [] -> conjunto de caracteres
# * 0 ou n
# + 1 ou n              (aplicam-se ao elemento a sua esquerda)
# ?  0 ou 1  (existir ou não)
# {n}
# {min, max}
# (grupos)+ [a-zA-Z0-9]+

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
Maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvi a maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'Jo+ão+', texto, flags=re.I))
print(re.findall(r'Jo{1,}ão{1,}', texto, flags=re.I))

"""
print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'[Jj]oão|[Mm]aria|ad....s', texto))
print(re.findall(r'[a-z]aria', texto))
print(re.findall(r'[A-Z]aria', texto))
print(re.findall(r'[a-zA-Z0-9]aria', texto))
print(re.findall(r'jOãO|MaRiA', texto, flags=re.I))
"""
