import os
import requests
import re
path = r'C:/Windows/System32/drivers/etc/'
os.chdir(path)
file = 'hosts'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}
def website(url):
    response=requests.get(url,headers=headers)
    if response.status_code == 200:

        return response.text
    return None
def parse(html):
    pattern=re.compile('<th>IP Address</th><td>(.*?)</td>',re.S).findall(html)
    for i in pattern:
        return i

def delet():
    lines = [l for l in open(file, "r", encoding='utf-8') if l.find("151", 0, 8) != 0]
    fd = open(file, "w", encoding="utf-8")
    fd.writelines(lines)
    fd.close()
    print("delet success")


def writeToHost(ip):
    with open(file,'a',encoding='utf-8') as f:

        f.write(ip+" global-ssl.fastly.net")
        print("write success!")

if __name__ == '__main__':
    url_one="http://github.global.ssl.fastly.net.ipaddress.com/"
    delet()
    html=website(url_one)
    ip=parse(html)
    print(ip)
    writeToHost(ip)

    os.popen('ipconfig /flushdns')
    print("flush success！")











