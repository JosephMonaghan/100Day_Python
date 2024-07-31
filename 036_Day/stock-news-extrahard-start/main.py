import os
import requests
import json
import smtplib


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_AlphaVantage = os.environ.get("API_KEY_ALPHAVANTAGE")

ENDURL = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_AlphaVantage,
}

request = requests.get(ENDURL,params=parameters)
request.raise_for_status()

with open("prices.json",'w') as file:
    json.dump(request.json(),file,indent=4)

with open("prices.json",'r') as file:
    request = json.load(file)


data= request["Time Series (Daily)"]


yesterday_close = float(list(data.values())[0]["4. close"])
day_before_close = float(list(data.values())[1]["4. close"])

percent_change = 100*(yesterday_close-day_before_close)/yesterday_close

if percent_change > 5:
    need_news = True
elif percent_change < -5:
    need_news = True
else:
    need_news = False


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_parameters = {
    "function": "NEWS_SENTIMENT",
    "tickers": STOCK,
    "limit": 3,
    "apikey": API_KEY_AlphaVantage
}

if need_news:
    news = requests.get(ENDURL,news_parameters)
    news.raise_for_status()
    with open("news.json",'w') as file:
        json.dump(news.json(),file,indent=4)

    with open("news.json", 'r') as file:
        news = json.load(file)

    iter=0
    titles=[]
    briefs=[]
    for item in news['feed']:
        titles.append(item["title"])
        briefs.append(item["summary"])
        iter +=1
        if iter > 3:
            break



    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    if percent_change > 5:  
        messages = [f"{COMPANY_NAME} : +{round(percent_change,1)}\n"]
    elif percent_change < -5:
        messages = [f"{COMPANY_NAME} : {round(percent_change,1)}\n"]
    for i in range(len(titles)):
        new_message = f"Headline: {''.join(titles[i])}\n Brief: {''.join(briefs[i])}"
        messages += new_message

    messages = "".join(messages)
    print(messages)

    email = "JM.Python.Learn@gmail.com"
    app_passcode =os.environ.get("app_passcode")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=app_passcode)
        connection.sendmail(
            from_addr=email,
            to_addrs="Joseph_Monaghan@outlook.com",
            msg=f"Subject: Your {STOCK} report\n\n{messages}"
        )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

