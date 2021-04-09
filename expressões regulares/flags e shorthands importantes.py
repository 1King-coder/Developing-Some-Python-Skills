# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_] (NEGAÇÃO)
# \W -> [^a-zA-Z0-9_] -> re.A (NEGAÇÃO)
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [\r\n\f\t]
# \s -> [^\r\n\f\t]
# \b -> Borda
# \B -> Não Borda
# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall

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

regexp1 = re.findall(r'[a-zA-Z0-9À-ú]+', texto, flags=re.I)
regexp2 = re.findall(r'\w+', texto, flags=re.A)
regexp3 = re.findall(r'\W+', texto, flags=re.A)
regexp4 = re.findall(r'\be\w+', texto, flags=re.I)

print(regexp1)
print('###########')
print(regexp2)
print('###########')
print(regexp3)
print('###########')
print(regexp4)
