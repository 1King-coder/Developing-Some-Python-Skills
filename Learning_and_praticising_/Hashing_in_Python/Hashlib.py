import hashlib

try:
    """
    open Passwords text archieve and set readlines copy
    that returns a iterator to a array.
    """
    passes = open('Passwords.txt', 'r')
    passwords = passes.readlines().copy()
except Exception:
    print("Unnable to open 'Passwords.txt'")
    quit()

try:
    """
    Open the archieve where the hashes will
    be stored.
    """
    hashes = open('Hashes.txt', 'w+')
except Exception:
    print("Unnable to open 'Hashes.txt'")
    quit()

for password in passwords:
    """
    iterate into the passwords in the archieve,
    turn them to sha256 and write the hash into
    the hash's archieves.
    """
    hashes.writelines(hashlib.sha256(
        password.strip().encode('utf-8')).hexdigest()+'\n')


hashes.close()  # Close the archieve for writing.

"""
 Opens the hashe's archieve for reading.
"""
hashes2 = open('Hashes.txt', 'r')

hashes_to_compare = hashes2.readlines().copy()  # Sets readlines to array.

for i in range(len(hashes_to_compare)):
    """
    Compares the hashes and password's hashes.
    """
    print(hashes_to_compare[i] == hashlib.sha256(
        passwords[i].strip().encode('utf-8')).hexdigest()+'\n')

hashes2.close()

passes.close()
