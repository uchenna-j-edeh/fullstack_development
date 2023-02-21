from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uchennaedeh@localhost:5432/example'
db = SQLAlchemy(app)

def init_db():
    db.create_all()

class Person(db.Model):
    __tablename__ = 'Persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)


with app.app_context():
    init_db()

@app.route('/')
def index():
    return "Hello World!"