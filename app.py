from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=["POST"])
def save():
    return redirect(url_for('index'))





app.run(debug=True, host='0.0.0.0', port=3000)

