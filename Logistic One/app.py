from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Crear la aplicación Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
db = SQLAlchemy(app)

# Definir el modelo de la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('logistic_one.html', servicios=servicios)

# Ruta para agregar un nuevo usuario
@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        correo = request.form['correo']
        edad = request.form['edad']
        
        if Usuario.query.filter_by(cedula=cedula).first():
            flash('Esta cédula ya está registrada.')
        else:
            nuevo_usuario = Usuario(cedula=cedula, nombre=nombre, apellido=apellido, direccion=direccion, correo=correo, edad=edad)
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario agregado exitosamente.')
    return redirect(url_for('logistic_one.html'))

# Ruta para la página de registro exitoso
@app.route('/registro_exitoso')
def registro_exitoso():
    return render_template('logistic_one.html')

# Ruta para verificar la base de datos
@app.route('/verificar_bd')
def verificar_bd():
    # Ejemplo de operación de lectura en la base de datos
    usuarios = Usuario.query.all()
    print("Usuarios en la base de datos:", usuarios)

    # Ejemplo de operación de escritura en la base de datos
    nuevo_usuario = Usuario(cedula='123456789', nombre='Ejemplo', apellido='Usuario', direccion='Calle 123', correo='ejemplo@usuario.com', edad=30)
    db.session.add(nuevo_usuario)
    db.session.commit()
    print("Usuario agregado correctamente.")

    return "Verifica la consola del servidor Flask para ver los resultados."

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
