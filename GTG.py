import requests
from bs4 import BeautifulSoup
import telebot
import schedule
import time

TOKEN = '7865974744:AAHp8T_HpOaQLgmrqAypOF1Q0AKwx8gisCQ'
CHANNEL_ID = '@SekretyNedvizhimosti'
NEWS_URL = 'https://realty.rbc.ru/'

def get_latest_news():
    response = requests.get(NEWS_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', class_='item__link', limit=3)
    news_list = []
    for article in articles:
        title = article.get_text(strip=True)
        link = article['href']
        if not link.startswith('http'):
            link = 'https://realty.rbc.ru' + link
        news_list.append(f"{title}\n{link}")
    return "\n\n".join(news_list)

def publish_news(time_slot):
    bot = telebot.TeleBot(TOKEN)
    news = get_latest_news()
    message = f"Новости недвижимости ({time_slot}):\n\n{news}"
    bot.send_message(CHANNEL_ID, message)

def main():
    schedule.every().day.at("09:00").do(publish_news, "утро")
    schedule.every().day.at("15:00").do(publish_news, "день")
    schedule.every().day.at("21:00").do(publish_news, "вечер")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
