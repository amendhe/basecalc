import os
from flask import Flask, request, redirect, url_for, render_template, flash, Response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    print ('in about')
    return render_template('about.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
