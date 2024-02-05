from flask import Flask, request, Response, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable=False)

    def __str__(self):
        return self.name
            
    def __init__(self, name):
        self.name = name

    def to_json(self):
        return{"id": self.id, "name": self.name}


@app.route("/users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    users_json = [user.to_json() for user in users]
    return Response(json.dumps(users_json), status=200, mimetype="application/json")

@app.route("/user/", methods=["POST"])
def create_user():
    body = request.get_json()
    name = body["name"]
    print(name)
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return Response("user created with success", 200)

@app.route('/')
def hello_world():
    return render_template('index.html', name="Ana")




if __name__ == '__main__':
    # db.create_all()
    app.run(debug = True)
