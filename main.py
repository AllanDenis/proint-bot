from pprint import pprint
import aiml

bot = aiml.Kernel()
bot.learn("aiml/personality.aiml")

def cli():
"""Interface de linha de comando para testar o bot."""
    while True:
        try:
            resposta = bot.respond(input("Você>\t"))
            print('Bot>\t' + resposta)
        except KeyboardInterrupt:
            print('')
            resposta = bot.respond('ADEUS')
            print(resposta)


if __name__ == "__main__":
    cli()
