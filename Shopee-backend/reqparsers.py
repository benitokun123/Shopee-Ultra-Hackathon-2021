from flask_restful import reqparse

def initializeParsers():
    putreqparser = reqparse.RequestParser()
    # putreqparser.add_argument("user_id", type=str, help="user_id required", required = True)
    putreqparser.add_argument("item_id", type=int, help="item_id ", required = True)
    putreqparser.add_argument("shop_id", type=int, help="shop_id required", required = True)
    putreqparser.add_argument("post", type=str, help="post required", required = True)

    # updatereqparser = reqparse.RequestParser()
    # updatereqparser.add_argument("name", type=str, help="")
    # updatereqparser.add_argument("wishlist", type=str)
    # updatereqparser.add_argument("email", type=str, help="")

    return putreqparser

if __name__ == "__main__":
    print("Run from main script")
    pass