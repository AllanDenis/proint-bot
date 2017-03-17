import aiml
from gtts import gTTS as tts
import random, string

bot = aiml.Kernel()
bot.learn("aiml/personality.aiml")

def nomeRandom(length=4):
    return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length)])


def falar(texto,lang='pt-BR'):
    if texto == '':
        texto = 'Eita!!!'
    fala = tts(text=texto, lang=lang)
    nome = 'tmp/' + nomeRandom() + '.mp3'
    fala.save(nome)
    return nome


def cli():
    """Interface de linha de comando para testar o bot."""
    while True:
        try:
            resposta = bot.respond(input("Você>\t"))
            print('Bot>\t' + resposta)
        except KeyboardInterrupt:
            print('')
            print('Bot>\t' + bot.respond('BYE'))
            exit(0)


if __name__ == "__main__":
    cli()
