from bs4 import BeautifulSoup
import requests
import pandas as pd



URL = 'https://in.indeed.com/jobs?q=data%20science&start=10'
#html = requests.get(URL)
#html_txt=html.text.encode('utf=8')
#print(html)

url2='https://in.indeed.com/jobs?q=data+science&start=0&from=mobRdr&utm_source=%2Fm%2F&utm_medium=redir&utm_campaign=dt'
#soup = BeautifulSoup(html_txt,'lxml')


title_ds = []
company_ds = []
location_ds = []
salary_ds = []
summary_ds = []
len(URL)
len(url2)

def retrive():
    
    for i in range(0,5000,10):
        
        URL = 'https://in.indeed.com/jobs?q=data%20science&start={}'.format(i)
        
        url2='https://in.indeed.com/jobs?q=data+science&start={}&from=mobRdr&utm_source=%2Fm%2F&utm_medium=redir&utm_campaign=dt'.format(i)
        html = requests.get(url2)
        html_txt=html.text.encode('utf=8')
        soup = BeautifulSoup(html_txt,'lxml')
        print(i)
        
        
        for full in soup.find_all('div',class_ ='jobsearch-SerpJobCard'):
            
            
            try:
                
                title = full.h2.a.text
                title_ds.append(title)
            except :
                title_ds.append('nan')
            
            try:
                comp = full.find('div',class_ = 'sjcl').span.text
                company_ds.append(comp)
            except:
                company_ds.append('nan')
        
        
            try:
                loc = full.find('span' ,class_='location').text
                location_ds.append(loc)
            except:
                location_ds.append('nan')
        
            try:
                salary = full.find('div', class_ ='salarySnippet').span.text
                salary_ds.append(salary)
            except:
                salary_ds.append('nan')
        
            try:
                summary = full.find('div',class_ = 'summary').ul.li.text
                summary_ds.append(summary)
            except:
                summary_ds.append('nan')
      

retriving = retrive()
df = pd.DataFrame(list(zip(title_ds, company_ds,location_ds,salary_ds,summary_ds)),
                   columns =['title', 'company','location','salary','summary'])

df.to_csv('data_science.csv')
