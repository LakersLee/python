import ssl
ssl._create_default_https_context = ssl._create_unverified_context	

from urllib.request import urlopen

url = 'https://github.com/LakersLee'
url = 'https://httpstat.us/500'
res = urlopen(url)
print(res)
#print(res.read().decode())
#print(dir(res))
#print(res.info())
print(res.getcode())







