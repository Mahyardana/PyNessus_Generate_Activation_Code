import requests
import re
import cfscrape
from bs4 import BeautifulSoup
class Mohmal:
    def __init__(self):
        self.scrape=cfscrape.create_scraper()
    def Get_Random_Email(self):
        response=requests.Response
        #headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}
        #response=requests.get("https://www.mohmal.com/en/inbox",headers=headers)
        text=str

        text=str(self.scrape.get("https://www.mohmal.com/en/inbox").content)        
        print(text)
        #text=response.text
        r1=re.findall(r"data-email=\"([\S]+)\"",text)
        #print(r1)
        return r1[0]
        #response=requests.get("https://www.mohmal.com/en/refresh",headers=headers)
        #text=str(self.scrape.get("https://www.mohmal.com/en/refresh").content)   
        #text=response.text
        #r1=re.findall(r"data-email=\"([\S]+)\"",text)
        #print(r1)
    def get_mailbox(self,tosearch):
        text=str(self.scrape.get("https://www.mohmal.com/en/refresh").content)
        if re.findall(tosearch,text).__len__() > 0:
            bs=BeautifulSoup(text,'html.parser')
            trs=bs.findAll("tr")
            for tr in trs:
                if re.findall(tosearch,str(tr)).__len__() > 0:
                   msgid=re.findall(r"data-msg-id=\"([0-9]+)\"",str(tr))[0]
                   return msgid
            return None
        else:
            return None
    def read_mail(self,msgid):
        return str(self.scrape.get("https://www.mohmal.com/en/message/"+msgid).content)
#mohmal=Mohmal()
#mohmal.Get_Random_Email()