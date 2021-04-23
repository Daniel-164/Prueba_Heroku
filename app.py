from flask import Flask, render_template, abort
import json
#import os

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("pagina.html")

@app.route('/libro/<isbn>')
def pagina_detalle_libro(titulo,imagen):
    with open("libros.json") as fichero:
        doc = json.load(fichero)
#if isbn != doc[0]['isbn']:
    return render_template("detalle.html")

#port=os.environ["PORT"]
app.run(debug=True)