from flask import Flask, request, render_template
from note2story import convert

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
	convert()