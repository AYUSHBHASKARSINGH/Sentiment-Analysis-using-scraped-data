import requests
from bs4 import BeautifulSoup 
import pandas
import csv

# Define the URL to scrape

url_2024 = ["https://www.moneycontrol.com/company-article/larsentoubro/news/LT",
       "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=M&Year=&duration=6&news_type="]


url_2023 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2023",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2023&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2023&duration=1&news_type="]

url_2022= ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2022",
           "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2022&duration=1&news_type=",
           "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2022&duration=1&news_type=",
           ]

url_2021 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2021",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            ]

url_2020 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2020",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2020&duration=1&news_type="]

url_2019 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2019",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2019&duration=1&news_type="]

url_2018 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2018",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2018&duration=1&news_type="]

url_2017 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2017",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2017&duration=1&news_type="]

url_combined = ["https://www.moneycontrol.com/company-article/larsentoubro/news/LT",
       "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=M&Year=&duration=6&news_type=","https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2023",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2023&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2023&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2022",
           "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2022&duration=1&news_type=",
           "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2022&duration=1&news_type=",
           "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2021",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2020",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2019",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2018",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2017",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2017&duration=1&news_type="]



Final_news1 = []
for url in url_combined:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    nifty50 = soup.find_all("a", class_="g_14bl")
    sensex = soup.find_all("p", class_="PT3")

    for l in range(len(nifty50)):
            str1 = nifty50[l].text
            Final_news1.append(str1)
        
    for l1 in range(len(sensex)):
        if l1%2!=0:
            str2 = sensex[l1].text
            Final_news1.append(str2)

Final_news1 = list(set(Final_news1))



file_path = "Scraped-news/news.csv"



with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Strings'])
    for string in Final_news1:
        writer.writerow([string])

print(f"CSV file saved successfully at: {file_path}")
