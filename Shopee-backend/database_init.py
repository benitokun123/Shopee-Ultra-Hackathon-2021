# RUNNING THIS WILL DELETE ALL DATA IN DATABASE

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from reqparsers import initializeParsers
import sys
import json

app  = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class WishlistModel(db.Model):
    column_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, nullable = False)
    item_id = db.Column(db.Integer, nullable = False)
    shop_id = db.Column(db.Integer, nullable = False)
    post = db.Column(db.String, nullable = False)

    def __repr__(self):
        pythondict = {"user_id" : self.user_id, "item_id" : self.item_id, "shop_id" : self.shop_id, "post" : self.post}
        return json.dumps(pythondict)
    #     return f"Wishlist(user_id = {self.user_id}), item_id = {self.item_id}, post = {self.post}"

class FriendsModel(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    friends_id = db.Column(db.String, nullable = False)

    def __repr__(self):
        # return f"Friends(user_id = {self.user_id}), friends_id = {self.friends_id}"
        pythondict = {"user_id" : self.user_id, "friends_id" : self.friends_id}
        return json.dumps(pythondict)

if __name__ == "__main__":
    yn = input("Warning: This will delete all database entries and create new db file. type y to continue and n to exit ->")

    if yn != "y":
        print("exiting")
        sys.exit()
    db.create_all()