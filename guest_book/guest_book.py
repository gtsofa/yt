#guest_book.py
from flask import Flask, render_template

app = Flask(__name__)

# create a route - decorate and the action
@app.route('/')
def index():

    return '<h1>Hello There!</h1>'

@app.route('/home')
def home():
    return render_template('example.html', myvar='I love jinja')

if __name__=='__main__':
    app.run(debug=True)

