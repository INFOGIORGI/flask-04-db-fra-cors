from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)



app.config['MYSQL_HOST'] = "138.41.20.102"
app.config['MYSQL_PORT'] = 53306  
app.config['MYSQL_USER'] = "ospite"
app.config['MYSQL_PASSWORD'] = "ospite"
app.config['MYSQL_DB'] = "w3schools"

#Creazione oggetto mysql
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html", titolo="Home")

@app.route("/products")
def products():
    
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    dati = cursor.fetchall()
    cursor.close()

    return render_template("products.html", titolo="Products", dati=dati)

@app.route("/products_c/<int:categoryID>")  
def products_c(categoryID):

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    dati = cursor.fetchall()
    
    lista=[]
    for i in dati:
        if int(i[0]) == categoryID:
            lista.append(i)

    cursor.close()
    return render_template("products_c.html", titolo="Categories", categoryID=categoryID, lista=lista)

 
app.run(debug=True)