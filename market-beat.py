import requests
from bs4 import BeautifulSoup 
import pandas
import csv


# Define the URL to scrape
url = "https://www.marketbeat.com/stocks/OTCMKTS/LTOUF/news/"



# Final_news1 = []
# for url in url:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     nifty50 = soup.find_all("a", class_="g_14bl")
#     sensex = soup.find_all("p", class_="PT3")

#     for l in range(len(nifty50)):
#             str1 = nifty50[l].text
#             Final_news1.append(str1)
        
#     for l1 in range(len(sensex)):
#         if l1%2!=0:
#             str2 = sensex[l1].text
#             Final_news1.append(str2)



# Final_news1 = list(set(Final_news1))

# file_path = "Scraped-news/news.csv"


# with open(file_path, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Strings'])
#     for string in Final_news1:
#         writer.writerow([string])

# print(f"CSV file saved successfully at: {file_path}")





response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

# Find the table with class "s-table"
table = soup.find("table", class_="s-table")

# Extract data from the table
data = []
if table:
    # Loop through each row in the table
    for row in table.find_all("tr"):
        # Extract data from each cell in the row
        cells = row.find_all("td")
        if len(cells) == 2:
            headline = cells.text()
            data.append({"Headline": headline})

