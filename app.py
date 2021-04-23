from flask import Flask, render_template, abort
import json

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("pagina.html")

@app.route('/libro/<int:isbn>')
def pagina_detalle_libro(isbn):
    with open("books.json") as fichero:
        doc = json.load(fichero)
    return render_template("detalle.html",diccionario_libros=doc)

app.run(debug=True)