import yfinance as yf
import pandas as pd

# Download Tesla's historical stock data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")  # Get data for the maximum available period

# Reset the index (optional, as we're not saving)
tesla_data = tesla_data.reset_index(drop=True)

# Display the first five rows
print(tesla_data.head())

import yfinance as yf
import pandas as pd

# Download Tesla's financial statements
tesla = yf.Ticker("TSLA")
tesla_financials = tesla.financials

# Extract revenue data (assuming 'Revenue' is the relevant key)
tesla_revenue = tesla_financials['Revenue']

# Display the last five rows (assuming 'Revenue' is a DataFrame)
print(tesla_revenue.tail())


import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# Send a GET request to the URL
response = requests.get(url)
html_data=response.text
soup = BeautifulSoup(html_data, 'html.parser')
rows = table.find_all('tr')

  # Skip the header row (if it exists)
data = [row.find_all('td') for row in rows[1:]]

  # Create empty lists to store extracted data
dates, revenues = [], []

  # Extract data from each table row
for row in data:
    dates.append(row[0].text.strip())  # Assuming date is in the first column
    revenues.append(row[1].text.strip())  # Assuming revenue is in the second column

df = pd.DataFrame({'Date': dates, 'Revenue': revenues})

  # Display the last 5 rows using tail function
last_five_rows = df.tail()
print(last_five_rows)

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# Send a GET request to the URL
response = requests.get(url)
html_data=response.text
soup = BeautifulSoup(html_data, 'html.parser')
table=soup.find("table")
rows = table.find_all('tr')

  # Skip the header row (if it exists)
data = [row.find_all('td') for row in rows[1:]]

  # Create empty lists to store extracted data
dates, revenues = [], []

  # Extract data from each table row
for row in data:
    dates.append(row[0].text.strip())  # Assuming date is in the first column
    revenues.append(row[1].text.strip())  # Assuming revenue is in the second column

df = pd.DataFrame({'Date': dates, 'Revenue': revenues})

  # Display the last 5 rows using tail function
last_five_rows = df.tail()
print(last_five_rows)

import yfinance as yf
import pandas as pd

# Download GME's historical stock data
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")  # Get data for the maximum available period

# Reset the index (optional, as we're not saving)
gme_data = gme_data.reset_index(drop=True)

# Display the first five rows
print(gme_data.head())