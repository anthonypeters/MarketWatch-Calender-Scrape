from bs4 import *
import requests
import pandas as pd

url = "https://www.marketwatch.com/economy-politics/calendar"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all(name='table')
df = pd.read_html(str(results))[0]

df = df.set_index(['Time (ET)'])
print(df)