from gtts import gTTS
from pygame import mixer
from chatterbot import ChatBot as Bot

def falar(texto):
    idioma = "pt-BR"
    som = "tmp/tts.mp3"
    # print("Convertendo texto para voz: %s\nAguarde..." % texto)
    tts = gTTS(text=texto, lang=idioma)
    tts.save(som)
    # print("Reproduzindo voz...")
    mixer.init()
    mixer.music.load(som)
    mixer.music.play()


chatbot = Bot(
    'Aida',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.portuguese")

# Get a response to an input statement
while True: print(chatbot.get_response(input('bot> ')))
