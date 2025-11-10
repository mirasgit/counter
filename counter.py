import telebot
import schedule
import time
from datetime import datetime

TOKEN = "8480403879:AAEMjk3sIeRkMBRG82FBHKqw7Sm6B4JwcmQ"
CHAT_ID = 892077871 # без кавычек, просто число
TARGET_DATE = datetime(2077, 1, 1)  # дата до которой идёт отсчёт

bot = telebot.TeleBot(TOKEN)

def send_countdown():
    today = datetime.now()
    remaining = (TARGET_DATE - today).days
    if remaining > 0:
        message = f"До {TARGET_DATE.strftime('%d.%m.%Y')} осталось {remaining} дней! ⏳"
    elif remaining == 0:
        message = "Сегодня тот самый день! 🎉"
    else:
        message = f"Дата уже прошла {abs(remaining)} дней назад."
    bot.send_message(CHAT_ID, message)

# Запускаем каждый день в 09:00
schedule.every().day.at("09:00").do(send_countdown)

# Бесконечный цикл
while True:
    schedule.run_pending()
    time.sleep(60)
