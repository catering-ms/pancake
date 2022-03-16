import json
from flask import Blueprint, request, jsonify
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
from src.constants.http_status_codes import HTTP_200_OK
from src.constants.http_status_codes import HTTP_401_UNAUTHORIZED
from src.database.admin import register_product, add_product
from src.utils.token import auth_by_token
from flask_cors import cross_origin

import logging


logger = logging.getLogger("test-logger")
posts = Blueprint("posts", __name__, url_prefix="/")

@posts.route("/posts")
# @cross_origin()
def all():
    print("headers-->", request.headers)

    payload = [
        {
            "userId": 10,
            "id": 100,
            "title": "at nam consequatur ea labore ea harum",
            "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut",
            "views": 1999,
            "published_at": "12/10/2022"
        }
    ]
    headers = {
        "X-Total-Count": "20"
    }
    response = jsonify(payload)
    return response, HTTP_200_OK, headers


@posts.post("/new")
def new():
    if request.json is not None:
        name = request.json.get("name")
        # 如果没有传入子单列表，则使用空列表代替
        sub_product_id_list = request.json.get("sub_product_id_list", [])
        sub_product_ids = json.dumps(sub_product_id_list)

        register_product(name, sub_product_ids)

        # 返回结果
        payload = {
            "message": "product created"
        }
        return jsonify(payload), 201
    else:
        payload = {
            "message": "invalid data input"
        }
        return jsonify(payload), HTTP_400_BAD_REQUEST


# 店长进货
@posts.post("/add")
def add():
    token = request.headers.get('token')
    merchant_id = auth_by_token(token)
    if merchant_id is None:
        payload = {
            "message": "invalid data input"
        }
        return jsonify(payload), HTTP_401_UNAUTHORIZED

    if request.json is not None:
        product_id = request.json.get("product_id")
        number = request.json.get("number")
        payload = {
            "message": "update product"
        } 
        # merchant_id="mch-001"
        # product_id= "2334d4a7-eb09-56ea-a1da-522afd5b21c8"
        # sub_product_id= "b1985cd3-6c54-59fb-b634-724d5112500f"
        number=int(number)
        add_product(product_id, merchant_id, number)
        return jsonify(payload), 201
    else:
        payload = {
            "message": "invalid data input"
        }
        return jsonify(payload), HTTP_400_BAD_REQUEST
