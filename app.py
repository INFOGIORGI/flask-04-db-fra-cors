from flask import Flask, render_templates
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = "138.41.20.102"
app.config['MYSQL_PORT'] = "53306"
app.config['MYSQL_DB'] = "w3schools"
app.config['MYSQL_USER'] = "ospite"
app.config['MYSQL_PASSWORD'] = "ospite"



@app.route("/")
def home():
    return render_templates("home.html", titolo = home)

def products():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM prducts"
    cursor.execute(query)
    dati = cursor.fetchall
    
    return render_templates("products.html", titolo = products)

app.run()
