#! env/bin/python
# -*- coding: utf-8 -*-
from main import bot, falar
from flask import Flask, jsonify
from flask_compress import Compress
from flask_cors import CORS
from werkzeug.exceptions import default_exceptions, HTTPException

__all__ = ['make_json_app']

def make_json_app(import_name, **kwargs):
    '''
    Creates a JSON-oriented Flask app.

    (from: http://flask.pocoo.org/snippets/83/)
    All error responses that you don't specifically
    manage yourself will have applicatio0,0n/json content
    type, and will contain JSON like this (just an example):

    { 'message': '405: Method Not Allowed' }
    '''
    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
                                if isinstance(ex, HTTPException)
                                else 500)
        return response

    app = Flask(import_name, **kwargs)

    for code in default_exceptions.items():
        app.error_handler_spec[None][code] = make_json_error

    return app

app = make_json_app(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['JSON_AS_ASCII'] = False
Compress(app)
CORS(app)

@app.route('/')
def hello():
    return jsonify('Olá, mundo!')

@app.route('/chat/<pergunta>')
def resposta(pergunta):
    resposta = bot.respond(pergunta)
    resposta = 'Ops!' if resposta == '' else resposta
    resposta = {
                    'resposta': resposta,
                    'url': falar(resposta)
                }
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,)
