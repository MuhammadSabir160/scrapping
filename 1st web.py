# import pandas as pd
# import numpy as np
# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# from random import randint


# headers={"Accept-Language":"es-UN,es;q=0.5"}
import requests
from bs4 import BeautifulSoup
import os
# url="http://www.pakistanjobsbank.com/"
def imgdown(url):
    r=requests.get(url)
    soap=BeautifulSoup(r.text,'html.parser')
    images=soap.find_all('img',attrs={'id':'Contents_AdImage'})
    for image in images:
        pic=image['src']
        n="http://www.pakistanjobsbank.com/"+pic
        name=image['alt']
        with open(name.replace(' ', '').replace('/','').replace(',','').replace('&','')+'.jpg','wb') as f:
            im=requests.get(n)
            f.write(im.content)




url="http://www.pakistanjobsbank.com/"
r=requests.get(url)
soap=BeautifulSoup(r.text,'html.parser')
for i in range(0,20):
    for j in range(0,20):
        alpha=soap.find_all('a',attrs={'id':'Contents_AdsList_Ads_'+str(i)+'_Job_'+str(j)})
        for image in alpha:
            t=image['href']
            t='http://www.pakistanjobsbank.com/'+t
            imgdown(t)
            

# for l in m:
#     f = open("links.txt", "a")
#     f.write(l+"\n")
#     f.close()


    
    # name=image['alt']
    # with open(name.replace(' ', '').replace('/','').replace(',','').replace('&','')+'.gif','wb') as f:
    #     im=requests.get(pic)
    #     f.write(im.content)

# print(images)

# for image in images:
#     img=image['src']
#     name=image['alt']
#     print(name,image)


# print(htmlContent)

# soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)
# title=soup.title
# print(title)

# get all paras
# paras=soup.find_all('a')

# print(paras)
# print(soup.find('a'))

# print(soup.find('a')['href'])

# print(soup.find_all("div",class_="cell1"))

# anchors=soup.find_all('h2',class_="entry-title")
# print(anchors) kaam ki cheez

# anchors=soup.find_all('a',class_="btn btn-primary")
# print(anchors)
# i=[]
# j=[]
# anchors=soup.find_all('img',loading_="lazy")
# for link in anchors:
    # print(link.get('src'))






# anchors=soup.find_all('a')

#for link in anchors:
#    print(link.get('href'))e