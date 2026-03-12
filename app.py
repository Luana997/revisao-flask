from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/revisao')
def revisao():
    return '''
    <h1>Funcionou?</h1>
    <p>!!!!</p>
    <p style= "color: purple;">PIP</p>
    ''' 

@app.route('/revisao/<nome>/<int:idade>')
def parametros(nome, idade):
    ano_nascimento = 2026 - idade
    return f'Olá {nome} tenho {idade} anos, por que nasceu no {ano_nascimento} '


if __name__ == '__main__':
  
    app.run(debug=True)


