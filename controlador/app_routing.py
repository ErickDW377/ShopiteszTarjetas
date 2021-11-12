from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
from DAO import db, Tarjetas


app=Flask(__name__,template_folder='../paginas',static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Hola.123@127.0.0.1/Shopitesz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

Bootstrap(app)



@app.route('/')
def incio():    
    return  render_template('inicio/inicio.html')

@app.route('/tarjetas')
def tarjetas(): 
    c= Tarjetas()
    tarjetas = c.consultarAll()
    return  render_template('tarjetas/tarjetas.html', lista = tarjetas)


@app.route('/Registro')
def Registro():
    return  render_template('tarjetas/Registro.html')

@app.route('/Editar')
def Editar():
    return  render_template('tarjetas/Editar.html')

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)
