import sys, os, datetime, requests, json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from os import remove
from os import path

token="1693375773:AAFsKYkReYRaegSIpSAO3TavSkmHqf7DwSc"

def start(bot, update):
    try:
        username=update.message.from_user.username
        message="Bienvenido soy un bot identificador de Picaduras" + username
        update.message.reply_text(message)
            
    except Exception as error:
        print("Error 001 {}".format(error.args[0]))

def echo(bot, update):
    try:
        text=update.message.text
        update.message.reply_text(text)
    except Exception as error:
        print("Error 002 {}".format(error.args[0]))

def help(bot, update):
    try:
        message="Puedes enviar imagenes para reconocer tu Picadura"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 003 {}".format(error.args[0]))

def error(bot, update, error):
    try:
        print(error)
    except Exception as e:
        print("Error 004 {}".format(e.args[0]))

def getImagen(bot, update):
    try:
        message="Enviando imagen"
        update.message.reply_text(message)

        file= bot.getFile(update.message.photo[-1].file_id)
        id=file.file_id
        filename= os.path.join("imagenes/","{}.jpg".format(id))
        file.download(filename)
        message="Imagen enviada"
        update.message.reply_text(message)
        message="Reconociendo picadura..."
        update.message.reply_text(message)                   
        myobj={"myfile":open(filename,'rb')}
        r = requests.post("https://8080-copper-damselfly-36qh7h0w.ws-us03.gitpod.io/upload", files=myobj)
        update.message.reply_text(r.text)
        
    except Exception as error:
        print("Error 005 {}".format(e.args[0]))
    

def evaluar(bot,filename):
    try:
        message="Evaluando..."
        update.message.reply_text(message)       
        params = {'myfile':filename}
        
        r = requests.post("https://8080-copper-damselfly-36qh7h0w.ws-us03.gitpod.io/upload", myfile=params)
        print(r.text)
        update.message.reply_text(r.text)
    except Exception as error:
        print("Error 0 {}".format(e.args[0]))

def main():
    try:
        updater=Updater(token)
        dp=updater.dispatcher
        
        dp.add_handler(CommandHandler("start",start))
        dp.add_handler(CommandHandler("help",help))

        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, getImagen))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()
        print("Bot listo")
    except Exception as e:
        print("Error 010 {}".format(e.args[0]))

if __name__=="__main__":
    try:
        main()
    except Exception as error:
        print("Error 011 {}".format(e.args[0]))