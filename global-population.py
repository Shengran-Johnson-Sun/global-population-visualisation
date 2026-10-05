import pandas as pd
import requests
import plotly.express as px
from bs4 import BeautifulSoup
import os

url = "https://srv1.worldometers.info/geography/countries-of-the-world/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

countries = []
populations = []
for row in table.find_all('tr')[1:16]:
    cols = row.find_all('td')
    if len(cols) >= 2:
        country = cols[1].text.strip()
        countries.append(country)
        population = cols[2].text.strip().replace(',','')   #去除千分位符
        populations.append(int(population))

df = pd.DataFrame({
    'Country': countries,
    'Population': populations
})

print(df)

fig = px.pie(df, names = 'Country', values = 'Population', title = "Global Population Distribution")

# 保存到桌面
desktop_path = os.path.expanduser('~/Desktop/Global_Population_Distribution.html')
fig.write_html(desktop_path, include_plotlyjs = 'direct')