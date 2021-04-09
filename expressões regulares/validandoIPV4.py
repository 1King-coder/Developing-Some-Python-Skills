import re
cpf = '122.346.907-73'

cpf_regexp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

# print(cpf_regexp.search(cpf))

ip_regexp = re.compile(r'''
    ^
    (?:
        (?:
        25[0-5]|
        2[0-4][0-9]|
        1[0-9]{2}|
        [1-9][0-9]|
        [0-9]
        )
        \.?
    ){4}
    \b
    $
''', flags=re.X)

for i in range(256):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_regexp.findall(ip))
