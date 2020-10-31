from app import app
from modelos import *
from flask import render_template

@app.route('/')
def login():
    form = LoginForm()
    return render_template('index.html', title='Sign In', form=form)




@app.route('/consulta')
def index():
    #listas
    personas=Personas.query.order_by(Personas.ID).all()
    print(personas)
    return render_template('Consulta.html', persona=personas)
