import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://www.isscheb.eu/jmenny-telefonni-seznam/'
 


def get_contacts(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'tablepress-15'})
    rows = table.find_all('tr')
    contacts = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 1:
            contact = {
                'name': cells[0].text,
                'phone': cells[1].text
            }
            contacts.append(contact)
    return contacts

contacts = get_contacts(url)

df = pd.DataFrame(contacts)
df.to_excel('contacts.xlsx', index=False)


