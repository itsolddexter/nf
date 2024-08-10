import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = '7210609135:AAGbTNxTTErPo1gc40CnBb89t1hawCXXsdE'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    welcome_message = f"<b>{user_first_name}</b>, Welcome! 🎉\n\n" \
                      "These are my following commands:\n\n" \
                      "<b>/netflix</b> - Netflix Web 🍿"

    markup = InlineKeyboardMarkup()
    dev_button = InlineKeyboardButton(
        text="Developer ❤️‍🩹",
        url="https://telegram.dog/SandeepKhadka7"
    )
    markup.add(dev_button)

    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(commands=['netflix'])
def netflix_command(message):
    markup = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(
        text="Open Netflix Web App 📺",
        web_app=WebAppInfo(url="https://iosmirror.cc")
    )
    markup.add(web_app_button)

    netflix_message = "🎬 <b>Welcome to the Netflix section!</b>\n\n" \
                      "Click the button below to open the web app. 👇"
    bot.send_message(message.chat.id, netflix_message, reply_markup=markup)

bot.infinity_polling()
