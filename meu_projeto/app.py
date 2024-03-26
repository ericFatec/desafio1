from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/quem")
def quem():
    return render_template('quem.html')