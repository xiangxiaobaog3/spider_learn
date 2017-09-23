import requests
from requests.packages import urllib3
urllib3.disable_warnings()

s = requests.Session()
headers = {
    'User-Agent': 'PregnancyHelper/5.7.0 (iPhone;iOS 11.0;375*667)'
}

proxies = {
    'http': 'http://192.168.1.46:8888'
}

data = {
    'blocks': 'grow,focus,earlyknowledge,fourpalace,recommendtool,knowledge,food,remind,repository,entrance,mamasee,advertise,xsxbuy,recordguide',
    'bb_sex': 2,
    'uid': 0,
    'version': '5.7.0',
    'bid': 0,
    'rel': 2,
    'period': 1,
    'unid': -1,
    'bb_nickname': '昕昕',
    'source': 2,
    'cityname': '北京市',
    'mode': 2,
    't': 1506067526,
    'days': 33,
    'appkey': 'pt_iphone',
    'device_id': 'b0810cd54d9dc42d18586becd6f3df56e6558f78',
    'week': '',
    'bb_birthday': '2017-08-21',
    'sign': '2767003EA834949A4E786B5AA0E6E2B4'
}

# proxies = {"http": "http://127.0.0.1:8888"}
cookies = dict(UUID='5BAC76A7-C6EE-439E-A9DA-E01E8A2E07CB')
response = requests.get('https://papi.mama.cn/v5_2_0/api/home/get.php', params=data, cookies=cookies, verify=False, headers=headers, proxies=proxies)
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)
print(response.status_code)
print(response.json())