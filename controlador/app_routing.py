from flask import Flask,render_template,request

app=Flask(__name__,template_folder='../paginas')

@app.route('/')
def incio():    
    return  render_template('inicio/inicio.html')

@app.route('/tarjetas')
def tarjetas():    
    return  render_template('tarjetas/tarjetas.html')


@app.route('/Registro')
def Registro():
    return  render_template('tarjetas/Registro.html')

@app.route('/Editar')
def Editar():
    return  render_template('tarjetas/Editar.html')

@app.route('/Eliminar')
def Eliminar():
    return  render_template('tarjetas/Eliminar.html')
if __name__=='__main__':
    app.run(debug=True)
