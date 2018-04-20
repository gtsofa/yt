#guest_book.py
from flask import Flask, render_template, request

app = Flask(__name__)

# create a route - decorate and the action
@app.route('/')
def index():

    #return '<h1>Hello There!</h1>'
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=["post"])
def process():
    name = request.form['name']
    comment = request.form['comment']
    #return 'Name is: '+name+' and the comment is: '+comment
    return render_template('index.html', name=name, comment=comment)

@app.route('/home')
def home():
    return render_template('example.html', myvarr='I love jinja')

if __name__=='__main__':
    app.run(debug=True)

