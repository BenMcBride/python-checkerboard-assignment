from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", rows = 8, columns = 8, darkClr = 'black', lightClr = 'red'  )

@app.route('/<x>')
def x(x):
    return render_template("index.html", rows = int(x), columns = 8)

@app.route('/<x>/<y>')
def xY(x, y):
    return render_template("index.html", rows = int(x), columns = int(y))

@app.route('/<x>/<y>/<darkClr>/<lightClr>')
def xYClrs(x, y, darkClr, lightClr):
    return render_template("index.html", rows = int(x), columns = int(y), darkClr = darkClr, lightClr = lightClr)


if __name__=="__main__":
    app.run(debug=True)