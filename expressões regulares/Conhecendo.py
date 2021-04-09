import re


string = 'O rato roeu a roeu roupa do rei de roma'
print('############')
search = re.search(r'221321', string)

print(search, '\n')


print(re.findall(r'roeu', string), '\n')

print(re.sub(r'roeu', 'OUTRA COISA', string), '\n')

print(re.sub(r'roeu', 'OUTRA COISA', string, count=1), '\n')

print('############')

regexp = re.compile(r'roeu')

print(regexp.search(string), '\n')

print(regexp.findall(string), '\n')

print(regexp.sub('DIFERENTE', string), '\n')

print(regexp.sub('DIFERENTE', string, count=1), '\n')

print('############')
