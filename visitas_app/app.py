from flask import Flask, session, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'super_clave_secreta_123'  # Clave secreta para sesiones

# Ruta principal: muestra el contador de visitas y reinicios
@app.route('/')
def index():
    # Inicializa el contador de visitas si no existe
    if 'visitas' not in session:
        session['visitas'] = 1
    else:
        session['visitas'] += 1
    # Inicializa el contador de reinicios si no existe
    if 'reinicios' not in session:
        session['reinicios'] = 0
    visitas = session.get('visitas', 1)
    reinicios = session.get('reinicios', 0)
    return render_template('index.html', visitas=visitas, reinicios=reinicios)

# Ruta para destruir la sesión y reiniciar todo
@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()  # Elimina todos los datos de la sesión
    return redirect(url_for('index'))

# Ruta para sumar dos visitas
@app.route('/sumar_dos')
def sumar_dos():
    session['visitas'] = session.get('visitas', 1) + 2
    return redirect(url_for('index'))

# Ruta para reiniciar el contador de visitas y contar reinicios
@app.route('/reiniciar')
def reiniciar():
    session['visitas'] = 0
    session['reinicios'] = session.get('reinicios', 0) + 1
    return redirect(url_for('index'))

# Ruta para aumentar visitas por formulario
@app.route('/aumentar', methods=['POST'])
def aumentar():
    try:
        incremento = int(request.form.get('incremento', 0))
    except ValueError:
        incremento = 0
    session['visitas'] = session.get('visitas', 1) + incremento
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
