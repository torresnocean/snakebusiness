from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
from flask_sslify import SSLify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import login_user, LoginManager, UserMixin, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

#import time
#import os

app = Flask(__name__)
sslify = SSLify(app)
app.config["DEBUG"] = True
app.debug = False

# configuring db connection..
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
migrate = Migrate(app, db)

app.secret_key = "My Mt.sac username"
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    posted = db.Column(db.DateTime, default=datetime.now)
    commenter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    commenter = db.relationship('User', foreign_keys=commenter_id)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", comments=Comment.query.all())

    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    comment = Comment(content=request.form["contents"], commenter=current_user)
    db.session.add(comment)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/login_page/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_page.html", error=False)

    user = load_user(request.form["username"])
    if user is None:
        return render_template("login_page.html", error=True)

    if not user.check_password(request.form["password"]):
        return render_template("login_page.html", error=True)

    login_user(user)
    return redirect(url_for('index'))


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))




# END OF FILE..



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
