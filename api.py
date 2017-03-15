from main import *
from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chat/<pergunta>")
def resposta(pergunta):
    resposta = {'resposta':bot.respond(pergunta)}
    return(jsonify(resposta))

if __name__ == "__main__":
    app.run()
