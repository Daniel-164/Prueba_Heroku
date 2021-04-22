from flask import Flask, render_template, abort
app = Flask(__name__)
import os

@app.route('/')
def pagina_principal():
    return render_template("pagina.html")

#port=os.environ["PORT"]
#app.run('0.0.0.0',int(port), debug=True)