from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/snijplanken")
def snijplanken():
    return render_template('snijplanken.html')

@app.route("/koekenpannen")
def koekenpannen():
    return render_template('koekenpannen.html')

@app.route("/hapjespannen")
def hapjespannen():
    return render_template('hapjespannen.html')

@app.route("/wokpannen")
def wokpannen():
    return render_template('wokpannen.html')

@app.route("/vershoudcontainers")
def vershoudcontainers():
    return render_template('vershoudcontainers.html')

@app.route("/airfryers")
def airfryers():
    return render_template('airfryers.html')

@app.route("/elements")
def elements():
    return render_template('elements.html')

if __name__ == "__main__":
    app.run(debug=True)
