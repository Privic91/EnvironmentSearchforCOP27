
# coding: utf-8

# In[58]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import bs4
import csv
URL = "https://economictimes.indiatimes.com/topic/environment-and-natural-resources"



page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml")

results = soup.find_all('div',class_="contentD")


data = []
v=[]

for job_element in results:


    python1 = job_element.find('h2')

    data.append(python1.string)
for job_element in results:


    python2 = job_element.find('time')

    v.append(python2.string)
df = pd.DataFrame({"Data": data,"Date":v})



b = df[df['Data'].str.contains("COP27")] 


b.to_csv("India.csv")






# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import bs4
import csv
URL = "https://www.mse.gov.sg/news/"



page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data=[]

results = soup.find_all('div',class_='media-card-plain bg-media-color-5 padding--lg')
results



for job_element in results:


    python1 = job_element.find('h5')

    data.append(python1.string)



df = pd.DataFrame({"Data": data})

df=df[1:40]


b = df[df['Data'].str.contains("COP27")]


b.to_csv('SIngapore.csv')




# In[10]:



import pandas as pd
import bs4
import csv

import requests
from bs4 import BeautifulSoup as bs

element_list = []
for page in range(1, 20, 5):
    URL = "https://eng.me.go.kr/eng/web/board/list.do?maxPageItems=6&maxIndexPages=10&searchKey=&searchValue=&boardMasterId=523&menuId=460&boardCategoryId=3&condition.hideCate=&condition.createDeptCode=&condition.createDeptName=&condition.fromDate=&condition.toDate=&condition.order=&condition.createId=&decorator=&condition.proxyParam1=&condition.proxyParam2=&condition.proxyParam3=&proxyListPath=&proxyReadPath=&pagerOffset=" + str(page)

    req = requests.get(URL)
    soup = bs(req.content, 'html.parser')
    
    
    titles = soup.find_all('div',class_='txt')
    
   

    for i in range(len(titles)):
        element_list.append([titles[i].text])
        


df = pd.DataFrame({"Element_list": element_list})


df.to_csv("Korea1.csv")


df = pd.read_csv("Korea1.csv")
df.replace('u\n','')
a= df[df['Element_list'].str.contains('COP27')]
a.to_csv("korea.csv")


# In[11]:


import pandas as pd
import bs4
import csv

import requests
from bs4 import BeautifulSoup as bs

element_list = []
data=[]
for page in range(1,30, 5):
    URL = "https://www.denr.gov.ph/index.php/news-events/press-releases?start=" + str(page)
    


    req = requests.get(URL)
    soup = bs(req.content, 'html.parser')
    
    
    titles = soup.find_all('div',class_="page-header")
    titles1 = soup.find_all(class_="published")
    

    
    for i in range(len(titles)):
        element_list.append([titles[i].text])
        
    for i in range(len(titles1)):
        
        

        data.append([titles1[i].text])
 
      
        
df = pd.DataFrame({"Element_list": element_list,"time":data})

df.to_csv("PHILLI.csv")

df = pd.read_csv("PHILLI.csv")
df.replace('u\n','')
a= df[df['Element_list'].str.contains('COP27')]
a.to_csv("phillipines.csv")






# In[49]:


import pandas as pd
import bs4
import csv

import requests
from bs4 import BeautifulSoup as bs

element_list = []
data=[]
for pag in range(1,10, 10):
    URL = "https://vietnamnews.vn/environment?p=" + str(pag)
    
    

    req = requests.get(URL)
    soup = bs(req.content, 'html.parser')
    

    titles = soup.find_all('a',class_="story__title")
    
    
    for i in range(len(titles)):
        element_list.append([titles[i].text])
        
df = pd.DataFrame({"Element_list": element_list})
df.align

df.to_csv("Viet.csv")



# In[50]:


import pandas as pd
import bs4
import csv

import requests
from bs4 import BeautifulSoup as bs

element_list = []
data=[]
for pag in range(2,10, 10):
    URL = "https://vietnamnews.vn/environment?p=" + str(pag)
    
    

    req = requests.get(URL)
    soup = bs(req.content, 'html.parser')
    

    titles = soup.find_all('a',class_="story__title")
    
    
    for i in range(len(titles)):
        element_list.append([titles[i].text])
        
df = pd.DataFrame({"Element_list": element_list})
df.align

df.to_csv("Vietn.csv")





# In[53]:


df = pd.read_csv("Vietn.csv")

a= df[df['Element_list'].str.contains('COP27')]
a.to_csv("Vietnam.csv")


# In[54]:


df = pd.read_csv("Viet.csv")

a= df[df['Element_list'].str.contains('COP27')]
a.to_csv("Vietnam1.csv")


# In[14]:


import pandas as pd
import bs4
import csv

import requests
from bs4 import BeautifulSoup as bs

element_list = []
data=[]
for pag in range(1,40, 40):
    URL = "https://thainews.prd.go.th/en/news/category/1/" + str(pag)
    req = requests.get(URL)
    soup = bs(req.content, 'html.parser')
    
    titles = soup.find_all('div',class_="col-12 pl-2")
    
    for i in range(len(titles)):
        element_list.append([titles[i].text])
        
df = pd.DataFrame({"Element_list": element_list})
df.to_csv("thai.csv")
df = pd.read_csv("thai.csv")
df.replace('u\n','')
a= df[df['Element_list'].str.contains('COP27')]
a.to_csv("Thailand.csv")

