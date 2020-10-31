from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    ID = StringField('Cedula', validators=[DataRequired()])
    Tipo_Doc = StringField('Tipo de documento', validators=[DataRequired()])
    Nacionalidad = StringField('Nacionalidad', validators=[DataRequired()])
    nombre = StringField('nombre', validators=[DataRequired()])
    fechaNacimiento = StringField('nombre', validators=[DataRequired()])
    Sexo =  StringField('M / F / O ', validators=[DataRequired()])
    Telefono = StringField('Telefono', validators=[DataRequired()])
    Apellido = StringField('Apellido', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class Personas(db.Model):
    ID=db.Column(db.Integer, primary_key=True)
    ID_usuario =db.Column(db.String(50))
    Tip_doc=db.Column(db.String(50))
    Nacionalidad =db.Column(db.String(50))
    Nom_usuario = db.Column(db.String(50))
    fech_naci=db.Column(db.String(50))
    sexo=db.Column(db.String(50))
    telefono=db.Column(db.String(50))
    apll_usuario=db.Column(db.String(50))
