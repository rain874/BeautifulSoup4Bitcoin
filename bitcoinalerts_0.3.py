# Das requests module wird importiert und mit rq angesprochen
import requests as rq
from bs4 import BeautifulSoup

def getrequests(url):
    req_row = rq.get(url)

    return req_row

url = "https://www.finanzen.net/devisen/realtimekurs/bitcoin-euro-kurs"
#url = "https://www.finanzen.net/devisen/realtimekurs/euro-yen-kurs"

responscode = getrequests(url)
responscode.status_code

while responscode.status_code <= 200:
    responscode = getrequests(url)
    c = responscode.content
    soup = BeautifulSoup(c, 'lxml')

    for realtime in soup.find_all('span', class_='push-data quotebox-textsize'):
        print(realtime.text)           

print("FACK OFF!")
