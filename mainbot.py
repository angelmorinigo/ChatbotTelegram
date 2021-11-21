import telebot


API_KEY = '2129977767:AAGS_auwT4uftbJ1Nyz_z0BmfttCz0CMa68'
bot =  telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hola'])
def greet(message):
  bot.reply_to(message, "Hola, Bievenido a mi primer bot")
  
bot.polling()
