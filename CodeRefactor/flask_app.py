from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_app import db

#import time
#import os

app = Flask(__name__)
app.config["DEBUG"] = True

# configuring the database connection..

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="htorres6",
    password="chula_1-2-3",
    hostname="htorres6.mysql.pythonanywhere-services.com",
    databasename="htorres6$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model):
	__tablename__ = 'comments'
	
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(4096))
	
	#timestamp = db.Column(db.String(256))

#comments = []

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", comments=Comment.query.all())

    comments = Comment(content=request.form["contents"])
    db.session.add(comment)
    adb.session.commit()

    return redirect(url_for('index'))

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
    