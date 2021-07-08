""" 
Online encrypt/decript using MD5
https://md5decrypt.net/en/

Hashlib SA1, SHA256, MD5

"""

import hashlib
import pathlib

path = str(pathlib.Path().resolve()) + "/InformationSecurity/"
file1 = path + 'ping_multiple.py'
file2 = path + 'ping_simple.py'

hash1 = hashlib.new('ripemd160')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'the file {file1} is nor equal to {file2}')
else:
    print(f'the file {file1} is equal to {file2}')
