from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    app.logger.info(f'Entramos al path: {request.path}')# Para mandar infromacion a la consola
    return 'Hello, World from world!.'

@app.route('/saludar/<nombre>')
def saludar(nombre):
    app.logger.info(f'Entramos al path: {request.path}')
    return f'Holiiiii {nombre}'

@app.route('/edad/<int:edad>')
def show_age(edad):
    return f'Tu edad es: {edad}'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)