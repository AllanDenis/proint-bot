# -*- coding: utf-8 -*-
from gtts import gTTS
from pygame import mixer
from pprint import pprint
import aiml
import speech_recognition as sr

def falar(texto, idioma='pt-BR'):
    som = "/tmp/tts.mp3"
    # print("Convertendo texto para voz: %s\nAguarde..." % texto)
    tts = ''
    try:
        tts = gTTS(text=texto, lang=idioma)
        tts.save(som)
    except Exception as e:
        pprint(e.message)

    try:
        mixer.init()
            # print("Reproduzindo voz...")
        mixer.music.load(som)
        mixer.music.play()
    except Exception as e:
        print('Erro: ' + str(e))

bot = aiml.Kernel()
# bot.learn("bot.xml")
bot.learn("aiml-en-us-foundation-alice/personality.aiml")

def cli():
    while True:
        try:
            resposta = bot.respond(raw_input("Você>\t"))
            print('Bot>\t' + resposta)
        except KeyboardInterrupt:
            print('')
            resposta = bot.respond('ADEUS')
            print(resposta)


if __name__ == "__main__":
    cli()
