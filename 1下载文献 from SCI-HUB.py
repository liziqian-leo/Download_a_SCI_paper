import requests
import re
import codecs


with open("SCI-HUB的有效链接.txt","r",encoding="utf-8")as f:
    SCI_HUB_URL=f.readline()

HEADERS={'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
DOI='10.1136/BMJEBM-2019-111331'#########这里输入DOI


def request(URL):###取网页
    global r
    r=requests.get("https://"+URL+"/"+DOI,headers=HEADERS,timeout=None)
    print("https://"+URL+"/"+DOI)

request(SCI_HUB_URL)


print()
search_1='//'+SCI_HUB_URL+'/downloads.*\.pdf'
result=re.search(search_1,r.content.decode('utf-8'))
print(type(r.content))
print(result)
result1='https:'+str(result[0])
print(result1)


###这以上是获取网页PDF链接######
#result2=requests.get(result1)
#print(result2)
#file_name="fi"

#with open(file_name,'wb+') as f:
#    f.write(result.content)


