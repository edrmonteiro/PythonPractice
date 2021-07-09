import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

result = urlopen(url)
data = json.load(result)
hostname = data['hostname']
ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print(f'IP:{ip}\nRegion:{region}\ncity:{city}')
