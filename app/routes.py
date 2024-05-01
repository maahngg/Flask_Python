from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    abencoados = 'Hello World, HexaGuard!'
    return render_template('index.html', bencao=abencoados)

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')