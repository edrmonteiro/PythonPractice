import os

ip = input("type the IP: ")

print('-' * 60)
os.system('ping -c 6 {}'.format(ip))
print('-' * 60)

stop = 1