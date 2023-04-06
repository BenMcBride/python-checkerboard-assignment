from flask import Flask, render_template
import math
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", rows = 8, columns = 8   )

@app.route('/<x>')
def x(x):
    return render_template("index.html", rows = int(x), columns = 8)

@app.route('/<x>/<y>')
def xY(x, y):
    return render_template("index.html", rows = int(x), columns = int(y))

if __name__=="__main__":
    app.run(debug=True)