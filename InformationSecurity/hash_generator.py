import hashlib

result = hashlib.md5(b'Python Security') #b' is to convert string into bytes
print('string hash is ', result.hexdigest())

string = input('Type the text to convert:')

menu = int(input ('''
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Type the hash number
                '''))
if menu == 1:
    result = hashlib.md5(string.encode('utf-8')) 
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8')) 
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8')) 
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8')) 



print('string hash is ', result.hexdigest())
