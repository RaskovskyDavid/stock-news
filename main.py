import requests
from password import newsapi_key, API_key, my_email_password
import smtplib
STOCK_NAME = "TSLA"

COMPANY_NAME = "Tesla Inc"
# alphavantage"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

path = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_key
}
response = requests.get(url=path, params=params)
data = response.json()["Time Series (Daily)"]
history_values = [value for (key, value) in data.items()]
yesterday_data = history_values[0]
yesterday_data_closing = yesterday_data["4. close"]

# 2. - Get the day before yesterday's closing stock price
day_before_data = history_values[1]
day_before_data_closing = day_before_data["4. close"]

# 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_data_closing) - float(day_before_data_closing))

# 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_data_closing)) * 100
# 5. - If TODO4 percentage is greater than 5 then print("Get News").
# https://newsapi.org/v2/everything?q=Apple&from=2021-05-04&sortBy=popularity&apiKey=API_KEY
#
if abs(diff_percent) > 5:
    news_param = {
        "qInTitle": COMPANY_NAME,
        "apiKey": newsapi_key
    }
    response_news = requests.get(url=NEWS_ENDPOINT, params= news_param)
    articles = response_news.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.


# 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    begining_title = ""
    if diff_percent > 0:
        begining_title = f"TSLA: ^{round(diff_percent,2)}%"
    elif diff_percent < 0:
        begining_title = f"TSLA: v{round(diff_percent,2)}%"
    letters = [f"Subject:{begining_title}\n\nHeadline: {articles['title']}.(TSLA)?\nBrief: {articles['description']}" for articles in three_articles]


#TODO 9. - Send each article as a separate message via Twilio.
    my_email = "davidraskovskypython@gmail.com"
    to_addrs = "davidraskovskypython@yahoo.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_email_password)
        for letter in letters:
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_addrs,
                                msg=letter
                                )


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

