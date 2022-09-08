from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# from datetime import datetime 

db = SQLAlchemy()

#import your module
class User(db.Model):
    """User"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} user_name={self.user_name}'

class Count(db.Model):
    """Count"""
    
    __tablename__ = "count"

    count_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    term_id = db.Column(db.Integer, db.ForeignKey('terminology.term_id'))
    count_value = db.Column(db.Integer)

    terminology = db.relationship("Terminology", backref="count")
    user =db.relationship("User", backref="count")

    def __repr__(self):
        return f'<Count ID count_id={self.count_id} count_value={self.count_value}'
    
class Terminology(db.Model):
    """Terminology"""

    __tablename__ = "terminology"

    term_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)
    non_inclus_term = db.Column(db.String)
    inclus_term = db.Column(db.String)
    term_topic = db.Column(db.String)
    explainer_desc = db.Column(db.String)
    active_status = db.Column(db.Boolean, nullable=False, default = True)


    def __repr__(self):
        return f'<Term term_id ={self.term_id} inclus_term={self.inclus_term}'


#place at end of file

def connect_to_db(flask_app, db_uri="postgresql:///inclusivedb", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    db.create_all()
    print("Connected to the db!")