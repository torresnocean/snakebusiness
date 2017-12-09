from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
#from flask_app import db

#import time
#import os
=======
from flask_login import login_user, LoginManager, UserMixin, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

#import time (for future use)
#import os (for future use)
>>>>>>> oceans-local-to-master

app = Flask(__name__)
app.config["DEBUG"] = True

<<<<<<< HEAD
# configuring the database connection..

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="htorres6",
    password="chula_1-2-3",
    hostname="htorres6.mysql.pythonanywhere-services.com",
    databasename="htorres6$comments",
=======
# configuring db connection..
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="dvsocean",
    password="renegade9",
    hostname="dvsocean.mysql.pythonanywhere-services.com",
    databasename="dvsocean$comments",
>>>>>>> oceans-local-to-master
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

<<<<<<< HEAD
class Comment(db.Model):
	__tablename__ = 'comments'
	
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(4096))
	
	#timestamp = db.Column(db.String(256))

#comments = []

@app.route("/", methods = ["GET", "POST"])
=======
app.secret_key = "renegade9"
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.username

all_users = {
    "Daniel": User("ocean", generate_password_hash("renegade9")),
    "Joe": User("stranger", generate_password_hash("snake")),
    "guest": User("guest", generate_password_hash("walker")),
    }

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

    #timestamp = db.Column(db.String(4096))

@app.route("/", methods=["GET", "POST"])
>>>>>>> oceans-local-to-master
def index():
    if request.method == "GET":
        return render_template("index.html", comments=Comment.query.all())

<<<<<<< HEAD
    comments = Comment(content=request.form["contents"])
=======
    comment = Comment(content=request.form["contents"])
>>>>>>> oceans-local-to-master
    db.session.add(comment)
    db.session.commit()

    return redirect(url_for('index'))

<<<<<<< HEAD
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


#if __name__ == '__main__':


# else:
#     comment = Comment()
#     comment.content = request.form['fieldComment']
#     os.environ['TZ'] = 'US/Pacific'
#     time.tzset()
#     comment.timestamp = time.strftime("%a %b %d %Y", time.localtime()
#     db.session.add(comment)
#     db.session.commit()
#return get_post
    
=======
>>>>>>> oceans-local-to-master
