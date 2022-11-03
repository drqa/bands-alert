from bs4 import BeautifulSoup
import requests

source = requests.get('https://therebellounge.com/events/').content
soup = BeautifulSoup(source, 'html.parser')
table = soup.find('table', attrs={'class':'calendar'})
css_selector = 'div.calender:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) > h1:nth-child(1)'
all_results = table.select(css_selector)
print(all_results)



# table = soup.find('table', attrs={'class':'calendar'})
# weeks = table.find_all('tr')
# for week in weeks:
#     days = week.find_all('td', attrs={'class':'calendar-day calendar-day-event'})
#     for day in days:
#         headliners = day.find_all('h1')
#         for headliner in headliners:
#             print(headliner.text)
    









