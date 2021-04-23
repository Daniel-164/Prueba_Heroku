from flask import Flask, render_template, abort
import json

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("pagina.html")

@app.route('/libro/<int:isbn>')
def pagina_detalle_libro(isbn):
    return render_template("detalle.html")

app.run(debug=True)