from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/snijplanken")
def snijplanken():
    return render_template('snijplanken.html')

@app.route("/pannen")
def pannen():
    return render_template('pannen.html')

@app.route("/elements")
def elements():
    return render_template('elements.html')

if __name__ == "__main__":
    app.run(debug=True)
