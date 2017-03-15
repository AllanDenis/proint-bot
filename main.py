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
            print('Bot>\t' + bot.respond('BYE'))
            exit(0)


if __name__ == "__main__":
    cli()
