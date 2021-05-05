from flask import Flask, render_template, abort
import json

app = Flask(__name__)

with open("books.json") as fichero:
        doc = json.load(fichero)

@app.route('/')
def pagina_principal():
    return render_template("pagina.html",documento=doc)

@app.route('/libro/<isbn>')
def pagina_detalle_libro(isbn):
    for i in doc:
        if i["isbn"]==isbn:
            return render_template("detalle.html",i=i,isbn=doc[0]["isbn"],titulo=doc[0]["title"],imagen=doc[0]["thumbnailUrl"],numpaginas=doc[0]["pageCount"],descripcioncorta=doc[0]["shortDescription"],descripcionlarga=doc[0]["longDescription"],autores=doc[0]["authors"],categorias=doc[0]["categories"])
    abort(404)
app.run(debug=True)