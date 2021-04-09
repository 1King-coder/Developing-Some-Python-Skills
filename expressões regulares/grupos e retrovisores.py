# (1)    \1
# (1) (2)     \1 \2
# (1(2)) (3)   \1 \2 \3


import re
from pprint import pprint
texto = """
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
"""


pprint(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 Mais \3 Alguma coisa \4', texto))

# tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# pprint(tags)

"""
tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)

pprint(tags)

for tag in tags:
    um, dois = tag
    pprint(dois)

tags1 = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', texto)

pprint(tags1)

for tag in tags1:
    um, dois, tres = tag
    pprint(um)
"""
