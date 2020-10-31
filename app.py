from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=LAPTOP-4SCBBM4T\SQLEXPRESS;DATABASE=Airp;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
db = SQLAlchemy(app)


from controlador import *

if __name__ == '__main__':
    app.run(host="localhost", port=2000, debug=True)