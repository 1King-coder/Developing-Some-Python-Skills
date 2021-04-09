import re

texto = """
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
"""

# print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))
# print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))

print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))
print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))
