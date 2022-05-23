import requests
# from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "XLC8DK693TU2FWOT"
NEWS_API_KEY = "83cfc2ed14e9485a83926cc3eae544da"

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response_code = requests.get(STOCK_ENDPOINT, params=stock_param)
data = response_code.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = yesterday_data["4. close"]
print(yesterday_closing_data)

yesterday_data_2 = data_list[1]
yesterday_closing_data_2 = yesterday_data_2["4. close"]
print(yesterday_closing_data_2)

price_diffrence = abs(float(yesterday_closing_data) - float(yesterday_closing_data_2))
print(price_diffrence)

percentage_diff = (price_diffrence / float(yesterday_closing_data)) * 100
print(percentage_diff)

if percentage_diff > 5:
    get_news = True
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    new_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = new_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formated_article = [f"Headline: {articles['title']}. \nBrief: "
                        f"{articles['description']}" for articles in three_articles]


# my twilio account not working SMS AUTOMATION CODED

#