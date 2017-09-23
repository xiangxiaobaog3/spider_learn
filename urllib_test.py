import urllib.parse
import urllib.request
from urllib import request, parse
# data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'HOST': 'httpbin.org'
}

dict = {
    'name': 'Germey'
}

data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8’))