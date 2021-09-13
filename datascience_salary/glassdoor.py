from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
#csv_file = open('modda.csv','w')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['title','summery'])

url = 'https://coreyms.com/'
text = requests.get(url).text
soup = BeautifulSoup(text,'lxml')
tit = []
sum = []
for full in soup.find_all('article'):
#print(full.prettify())
    title = full.header.h2.a.text.strip()
    tit.append(title)
    summery = full.div.p.text.strip()
    sum.append(summery)
print(tit)
    #csv_writer.writerow([title,summery])
#csv_file.close()

job =  {'title':tit,
        'summery':sum


}
joblist = []
joblist.append(job)
df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')