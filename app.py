import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Obtener el token del bot desde una variable de entorno
TOKEN = os.environ['6230169151:AAFvEHXvVCmsd282A1lB1gpL2zAzxg3wIl4']

# Función para responder a los comandos de inicio
def start(update, context):
    chat_id = update.message.chat_id
    message = "Hola, soy un bot de prueba de Python."
    context.bot.send_message(chat_id=chat_id, text=message)

# Crear el manejador de eventos y agregarle los controladores
updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))

# Iniciar el bot
updater.start_polling()
