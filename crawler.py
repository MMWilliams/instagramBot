import requests
from bs4 import BeautifulSoup
#scraping from google

url = ""
#https://www.discoverphl.com/business-directory/
response = requests.get(url)
data = response.text

#storing entire webpage and parsing the html
soup = BeautifulSoup(data,'html.parser')

#=================================================
#            SCRAPING FOR PHONE NUMBERS AND EMAIL ADDRESSES WITH REGEX
#data = requests.get('https://www.google.com/search?rlz=1C5CHFA_enUS838US838&ei=d1hTXdvBNsyZ_QaW7Y6ICQ&q=%22gmail.com%22+restaurant&oq=%22gmail.com%22+restaurant&gs_l=psy-ab.3..0i8i30l2j0i8i10i30.7549.12452..12621...0.0..0.104.869.9j1......0....1..gws-wiz.......0i71j0i7i30j0i7i10i30j0i8i7i30j0i13i30j0i30j0i8i7i10i30.3y-eHIS29oo&ved=0ahUKEwib2a2FkIHkAhXMTN8KHZa2A5EQ4dUDCAo&uact=5')
#data1 = requests.get('https://www.google.com/search?rlz=1C5CHFA_enUS838US838&ei=d1hTXdvBNsyZ_QaW7Y6ICQ&q=%22gmail.com%22+restaurant&oq=%22gmail.com%22+restaurant&gs_l=psy-ab.3..0i8i30l2j0i8i10i30.7549.12452..12621...0.0..0.104.869.9j1......0....1..gws-wiz.......0i71j0i7i30j0i7i10i30j0i8i7i30j0i13i30j0i30j0i8i7i10i30.3y-eHIS29oo&ved=0ahUKEwib2a2FkIHkAhXMTN8KHZa2A5EQ4dUDCAo&uact=5')

# extract the phone numbers, emails, whatever
#phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
#emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
#phones1 = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
#emails1 = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

#phonelist = [x.strip() for x in phones.split(',')]
#emaillist = [x.strip() for x in emails.split(',')]

#sort through pages, which are stored in a table
#count_emails = len(emails)
#count_phones = len(phones)
#count_emails1 = len(emails1)
#count_phones1 = len(phones1)

#print('email count: ', count_emails, 'phone count: ', count_phones)
#print('email1 count: ', count_emails1, 'phone1 count: ', count_phones1)

#all_contact_info = phones + emails
#all_contact_info1 = phones1 + emails1
#complete_ist = all_contact_info + all_contact_info1
#print(all_contact_info)
#print(all_contact_info1)


#d = {'Emails':emaillist,'Phone':phonelist}
#df = pd.DataFrame(complete_ist)
#print(df)

#export_csv = df.to_csv('~/Desktop/contactinfo.csv',index = None, header=True)
#print("saved to csv")
#=================================================

#returning all job titles
#titles = soup.find_all('a',{"class":"result-title"})
#for title in titles:
#    print(title.text)

#return all links on page
#tags = soup.find_all('a')
#for tag in tags:
#    print(tag.get('href'))

#returning all addresses on webpage
#address = soup.find_all("span",{"class":"result-hood"})
#for address in address:
#    print(address.text)

#returning job, title, location and links, if there is no location, returns N/A
#if one tag is missing, an error will be returned
#find is used instead of find all, because we only want the first occurence, not all occurences

#returning job, title, location and links, if there is no location, returns N/A
#if one tag is missing, an error will be returned
#find is used instead of find all, because we only want the first occurence, not all occurences

job_no = 0
page = 1
job = soup.find_all('div',{"class":"r"}) # title and link
#job = all data pertaining to the jobs

#with all the data, separate by certain class names
for job in jobs:
    title = job.find('dv',{"class":"ellip"}).text #small link
    small_link = job.find('cite',{"class":"iUh30"}) #text block - was small_link
    small_link_if = small_link.text[2:-1] if small_link else "N/A" #[2:-1] removes braskets surrounding lication
    #date = job.find('a',{"class":"result-date"}) #date posted
    link = job.find('cite',{"class":"iUh30"}).get('href')
    #returning the job description for each job, which is housed though the link
    #refer to webpage for classes and headers
    job_response = requests.get(link) #opening link to job posting
    job_data = job_response.text
    job_soup = BeautifulSoup(job_data,'html.parser')
    emails = job_soup.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
    #job_description = job_soup.find('section',{"id":"postingbody"}).text #this pertains to the job desctiption on the job's page after clicking the link
    #job_attributes_tag = job_soup.find('p',{"class":"attrgroup"}) #attributes, such as pay, employment type:full time/contract
    #job_attributes = job_attributes_tag if job_attributes_tag else "N/A"
    #job_no+=1
    #print('Job Title:', title, '\nLocation:', location, '\nDate:', date, '\nLink:', link,"\n", job_attributes, '\nJob Description:', job_description,'\n---')
    print(emails)
    #moving to the next page to continue scraping
    #if the next page text, is an href as in link, do the following
    url_tag = soup.find('a',{"aria-label":"page " + page}) #pertains to next page button on original search page
    page+=1
    if url_tag.get('href'):
        url = 'https://google.com' + url_tag.get('href') #href example = /search/jjj?s=120
        print(url)
    else:
        break


print("Total Jobs: ", job_no)
