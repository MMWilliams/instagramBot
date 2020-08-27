import requests
import re
import pandas as pd
import csv



#for each i in 1 through 10:
    #first page url
    #
    #
    #
    #
    #
# get the data
data = requests.get('')
data1 = requests.get('')

# extract the phone numbers, emails, whatever
phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
phones1 = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails1 = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
#phonelist = [x.strip() for x in phones.split(',')]
#emaillist = [x.strip() for x in emails.split(',')]
phonetype = type(phones)
emailtype = type(emails)
phonetype = type(phones1)
emailtype = type(emails1)

#sort through pages, which are stored in a table
count_emails = len(emails)
count_phones = len(phones)
count_emails1 = len(emails1)
count_phones1 = len(phones1)

print('email count: ', count_emails, 'phone count: ', count_phones)
print('email1 count: ', count_emails1, 'phone1 count: ', count_phones1)

all_contact_info = phones + emails
all_contact_info1 = phones1 + emails1
complete_ist = all_contact_info + all_contact_info1
print(all_contact_info)
print(all_contact_info1)


#d = {'Emails':emaillist,'Phone':phonelist}
df = pd.DataFrame(complete_ist)
print(df)

export_csv = df.to_csv('~/Desktop/contactinfo.csv',index = None, header=True)
print("saved to csv")
#get the data (url)
#data = requests.get('http://www.petecoffeegolf.com/contact.php')

#load into bs4
#soup = BeautifulSoup(data.text, 'html.parser')

# get data simply by looking for each tr
#inspect webpage tr = list
#data = []
#for tr in soup.find_all('tr'):
#    values = [td.text for td in tr.find_all('td')]
#        data.append(values)


#selecting classes by class name
#can also be done for ID name or numbers
#data = []
#for tr in soup.find_all('tr' {'class': 'special'}):
#    values = [td.text for td in tr.find_all('td')]
#        data.append(values)

#get data within a specific elements
#determine element type inside of div class
#data = []
#div = soup.find('div', { 'class': 'special_table' })
#for tr in div.find_all('tr'):
#    values = [td.text for td in tr.find_all('td')]
#        data.append(values)
# extract the phone numbers, emails, extract
#phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})',data.text)
#phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)

#emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
#emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
