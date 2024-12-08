from flask import Flask, redirect,render_template, url_for
from DAO_client import ClienteDAO
from client import Cliente
from cliente_form import ClienteForm

app = Flask(__name__)

titulo_app = 'Udinder'
app.config['SECRET_KEY']='llave_secreta'

@app.route('/')
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    #Interactuando con la base de datos
    clientes_db = ClienteDAO.seleccionar()
    
    # CLiente Vacío
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    
    
    return render_template('index.html', titulo=titulo_app,
                           clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    app.logger.debug('Entramos al path de guardar /guardar')
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    if cliente_forma.validate_on_submit():
        # Llenar cliente con los valores que dan en el formulario
        cliente_forma.populate_obj(cliente)
        #Validacion de existencia o no
        if not cliente.id: #Comprobamos si el id es cadena vacia, si lo es, regresa veradero   
            # Lo enviamos a la BD y se guarda
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)
        # Redireccionamos a la pagina principal
        return redirect(url_for('inicio'))

    else:
        return 'Error al guardar el cliente'

@app.route('/editar/<int:id>') #para editar el registro respectivo a ese id
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForm(obj=cliente)
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app,
                           clientes=clientes_db,
                           forma=cliente_forma)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    app.logger.debug('Entramos al path de limpiar /limpiar')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)