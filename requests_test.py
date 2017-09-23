import requests
from requests.packages import urllib3
urllib3.disable_warnings()

data = {
    'name': 'germey',
    'age': 22
}

headers = {
    'User-Agent': 'PregnancyHelper/5.7.0 (iPhone;iOS 11.0;375*667)'
}

files = {'file': open('favicon.ico', 'rb')}
response = requests.get('https://www.baidu.com')
response1 = requests.get('http://httpbin.org/get', params=data)
response2 = requests.get('https://github.com/favicon.ico')
response3 = requests.post('http://httpbin.org/post', data=data)
response4 = requests.get('http://www.jianshu.com/hello.html')
response5 = requests.post('http://httpbin.org/post', files=files)
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response6 = s.get('http://httpbin.org/cookies')
response7 = requests.get('https://www.12306.cn', verify=False)


print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
# print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)
print(response1.text)
print(response1.json())
print(response5.text)
# with open('favicon.ico', 'wb') as f:
#     f.write(response2.content)
#     f.close()

print(response3.text)
print(response6.text)
print(response7.status_code)
# exit() if not response4.status_code == 404 else print('Request Successfully')