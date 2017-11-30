# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_app import db

import time
import os

app = Flask(__name__)
app.config["DEBUG"] = True

# configuring the database connection..

app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+mysqlconnector://'
    + 'htorres6:pythonanywheremysql@htorres6.mysql.pythonanywhere-services.com'
    + '/htorres6$commentApp'
    )
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    timestamp = db.Column(db.String(256))

@app.route("/", methods = ["GET", "POST"])

def index():
    get_post = redirect(url_for('index'))
    if request.method == "GET":
        get_post = render_template("index.html", comments = comment.query.all())
    else:
        comment = Comment()
        comment.content = request.form['fieldComment']
        os.environ['TZ'] = 'US/Pacific'
        time.tzset()
        comment.timestamp = time.strftime("%a %b %d %Y", time.localtime()
        db.session.add(comment)
        db.session.commit()

# i stopped here and it crashed..

    return get_post
