from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from reqparsers import initializeParsers
from database_init import WishlistModel, FriendsModel
import json

app  = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# db.create_all()

wishlistPutReqParser = initializeParsers()

# Resource fields for wishlist database model
wishlist_resource_fields = {
    'user_id': fields.Integer,
    'item_id': fields.Integer,
    'shop_id': fields.Integer,
    'post': fields.String
}
class Wishlist(Resource):
    @marshal_with(wishlist_resource_fields)
    def get(self, user_id):
        result = WishlistModel.query.filter_by(user_id = user_id).all()
        print(result)
        if not result:
            abort(404, message = "user id does not yet exist")

        return result

    @marshal_with(wishlist_resource_fields)
    def put(self, user_id):
        args = wishlistPutReqParser.parse_args()
        wishlist = WishlistModel(user_id = user_id, item_id = args['item_id'], shop_id = args['shop_id'], post = args['post'])
        db.session.add(wishlist)
        db.session.commit()
        
# Resource fields for friends database model
friends_resource_fields = {
    'user_id': fields.Integer,
    'item_id': fields.Integer,
    'post': fields.String,
    'shop_id': fields.Integer
}
class Friends(Resource):
    @marshal_with(friends_resource_fields)
    def get(self, user_id):
        result = FriendsModel.query.filter_by(user_id = user_id).all()
        # return result
        jsonResult = json.loads(str(result))
        print(jsonResult)
        friendslist = jsonResult[0]['friends_id']
        print(friendslist)

        listOfItems = []
        for friend_id in friendslist:
            resultWishList = WishlistModel.query.filter_by(user_id = friend_id).all()
            jsonResultWishList = json.loads(str(resultWishList))
            for friendsWishList in jsonResultWishList:
                listOfItems.append(friendsWishList)
                print(friendsWishList)
        
        print(friendslist)

        return listOfItems

@app.route("/")
def home():
    return "a buttplug"
    
def getApp():
    return app
    
api.add_resource(Friends, "/friends/<int:user_id>")
api.add_resource(Wishlist, "/wishlist/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)