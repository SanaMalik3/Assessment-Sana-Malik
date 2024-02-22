# Question No 5:
# Write a Python code that scrapes the table above from the website and saves it in a CSV file named django_vs_flask.csv.
import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://www.geeksforgeeks.org/differences-between-django-vs-flask/'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')
data=[]
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if cells: 
        cell_data = [cell.text.strip() for cell in cells]
        print(cell_data)
        data.append(cell_data)
df = pd.DataFrame(data, columns=['Django', 'Flask'])
csv = df.to_csv("django_vs_flask.csv")