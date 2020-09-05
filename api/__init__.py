from api.routes.productsRoutes import products
from flask import Flask, jsonify, render_template
# from flask_cors import CORS
# import mysql.connector
import os

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)
CORS(app)


cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

app.register_blueprint(products)


@app.route('/', methods=["GET"])
def rootFunc():
    return render_template('index.html')
