# web_dynamic/4-hbnb.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/4-hbnb', strict_slashes=False)
def display_4_hbnb():
    # Your code to fetch data and render template
    # For example:
    data = {'some_key': 'some_value'}
    return render_template('4-hbnb.html', data=data)
