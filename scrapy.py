import requests
from bs4 import BeautifulSoup
#https://www.youtube.com/watch?v=F1kZ39SvuGE

#get databases
#inspect website to determine ID name, class name, and where email addresses are stored
data = requests.get('https://umggaming.com/leaderboards')
#load data into bs4

soup = BeautifulSoup(data.text, 'html.parser')
#This data is stored in tables
#by inspecting element, we find table id "leaderboard-table"
#inside of div class "table-responsive margin-40"
#inside of <table id "leaderboard-table"> is <tbody>
leaderboard = soup.find('table', { 'id': 'leaderboard-table' })
tbody = leaderboard.find('tbody')
#Inside of <tbody> is <tr>
#inside of <tr> is <td>
#we are grabbin the first value (0) in the first <td> which is 1st place
#next, we are grabbign the second occurance of <td>,
#which houses <a> which houses the username
#next we are grabbing the value in the 4th occurance of <td> which
#is the xp points

for tr in tbody.find_all('tr'):
	place = tr.find_all('td')[0].text.strip()
	username = tr.find_all('td')[1].find_all('a')[1].text.strip()
	xp = tr.find_all('td')[3].text.strip()
	print(place, username, xp)
