import telebot
import threading
import schedule
import time
from datetime import date
import pytz

TOKEN = "8480403879:AAEMjk3sIeRkMBRG82FBHKqw7Sm6B4JwcmQ"
bot = telebot.TeleBot(TOKEN)

# 🔹 целевая дата для отсчёта
target_date = date(2026, 1, 1)

# 🔹 словарь пользователей, чтобы бот знал, кому писать каждый день
users = set()

# 🔹 при старте добавляем пользователя в список
@bot.message_handler(commands=['start'])
def start(message):
    users.add(message.chat.id)
    bot.send_message(message.chat.id, "Привет! Я буду писать тебе каждый день в 9 утра ☀️")

# 🔹 функция ежедневной рассылки
def send_daily_message():
    today = date.today()
    days_left = (target_date - today).days

    for user_id in users:
        bot.send_message(user_id, "☀️ Доброе утро!")
        bot.send_message(user_id, f"📅 Сегодня {today.strftime('%d.%m.%Y')}")
        bot.send_message(user_id, f"⏳ До {target_date.strftime('%d.%m.%Y')} осталось {days_left} дней!")
        bot.send_message(user_id, "Не забывай про свои цели")
        time.sleep(1)

# 🔹 планировщик (каждый день в 9:00 по времени Астаны)
def schedule_jobs():
    tz = pytz.timezone("Asia/Almaty")
    schedule.every().day.at("10:00").do(send_daily_message)

    while True:
        schedule.run_pending()
        time.sleep(30)

# 🔹 запуск планировщика в отдельном потоке
threading.Thread(target=schedule_jobs, daemon=True).start()

print("Бот запущен...")
bot.polling()
