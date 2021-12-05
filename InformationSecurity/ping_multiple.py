
import os
import pathlib
import time
path = str(pathlib.Path().resolve()) + "/InformationSecurity/"

with open(path + 'hosts.txt') as file:
    dump = file.read().splitlines()
    for ip in dump:
        print('check IP:', ip)
        os.system('ping -c 2 {}'.format(ip))
        time.sleep(5)

    stop = 1