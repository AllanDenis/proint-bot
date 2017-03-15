from main import *
from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException

__all__ = ['make_json_app']

def make_json_app(import_name, **kwargs):
    """
    Creates a JSON-oriented Flask app.

    (from: http://flask.pocoo.org/snippets/83/)
    All error responses that you don't specifically
    manage yourself will have application/json content
    type, and will contain JSON like this (just an example):

    { "message": "405: Method Not Allowed" }
    """
    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
                                if isinstance(ex, HTTPException)
                                else 500)
        return response

    app = Flask(import_name, **kwargs)

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error

    return app

app = make_json_app(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chat/<pergunta>")
def resposta(pergunta):
    resposta = {'resposta':bot.respond(pergunta)}
    return(jsonify(resposta))

if __name__ == "__main__":
    app.run()
