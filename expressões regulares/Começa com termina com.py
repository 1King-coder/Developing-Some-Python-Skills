# ^ -> Começa com
# $ -> Temina com
# [^a-z] -> Negação

import re

cpf = '147.312.543-12'

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.sub(r'[^0-9]+', ' ', cpf))
