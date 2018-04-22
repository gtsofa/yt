#guest_book.py
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://sql7233805:FGtSvLX88h@sql7.freemysqlhosting.net/sql7233805'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://guest_admin:FGtSvLX88h@localhost/guest_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#institiate the db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

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

    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()

@app.route('/home')
def home():
    return render_template('example.html', myvarr='I love jinja')

if __name__=='__main__':
    app.run(debug=True)

