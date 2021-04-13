import hashlib

try:
    passes = open('MiniProjetosPessoaisPython/' +
                  'Hashing_in_Python/Passwords.txt', 'r')
    passwords = passes.readlines().copy()
except Exception:
    print("Unnable to open 'Passwords.txt'")
    quit()

try:
    hashes = open('MiniProjetosPessoaisPython/' +
                  'Hashing_in_Python/Hashes.txt', 'w+')
except Exception:
    print("Unnable to open 'Hashes.txt'")
    quit()

for password in passwords:
    hashes.writelines(hashlib.sha256(
        password.strip().encode('utf-8')).hexdigest()+'\n')


hashes.close()
hashes2 = open('MiniProjetosPessoaisPython/' +
               'Hashing_in_Python/Hashes.txt', 'r')
hashes_to_compare = hashes2.readlines().copy()

for i in range(len(hashes_to_compare)):
    print(hashes_to_compare[i] == hashlib.sha256(
        passwords[i].strip().encode('utf-8')).hexdigest()+'\n')

hashes2.close()

passes.close()
