#!/usr/bin/python3


from bs4 import BeautifulSoup
import requests
import urllib

suc = 0
idd = int(input("Please put your ID: "))
times = int(input("How many votes do you want?: "))
url = "http://158.69.76.135/level2.php"
heady = {'Referer': url, 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64;\
 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141\
 Safari/537.36 Edg/87.0.664.75"}

print("\nWorking... Please wait some time, even if this is slow, i'm\
 faster than you.")

for i in range(0, times):
    cokie = requests.session()
    tmp = cokie.get(url)
    content = tmp.content
    web = BeautifulSoup(content, 'html.parser')
    hml = web.find_all('input')
    for l in hml:
        if l.get('name') == "key":
            key = l.get('value')
    form = {'id': idd, 'key': key, 'holdthedoor': 'Submit'}
    req = cokie.post(url, headers=heady, data=form)
    if req.status_code == 200:
        suc += 1
    del cokie
print("Successful requests: {:d}".format(suc))
