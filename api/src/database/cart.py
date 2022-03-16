import json

from sqlalchemy import update
from src.database.model import db
from src.database.model import ProductOfCartModel, ProductListModel, ProductPriceModel
from src.utils.gjson import covert_str_to_json

def get_cart_quantity():
    init_cart_status = 0
    data = ProductOfCartModel.query.filter_by(status=init_cart_status).all()
    return len(data)

def add_into_cart(product_id_list, user_id, quantity, price, extras):
    # username = "reday" # 网关验证信息后通过HEADER带进来
    status = 0 
    # print("before json dumps", extras)
    extras_dumps = json.dumps(extras)

    product_ids =json.dumps(product_id_list)
    # print("after json dumps", extras_dumps)

    m = ProductOfCartModel(
        username=user_id, 
        product_ids=product_ids, 
        quantity=quantity,
        price=price,
        extras_dumps=extras_dumps,
        status=status,
        )
    db.session.add(m)
    db.session.commit()


def get_cart():
    init_cart_status = 0
    data = ProductOfCartModel.query.filter_by(status=init_cart_status).all()
    print("all data from cart===>", data)
    # rows = [row for row in data]
    new_rows = covert_str_to_json(data)
    sumQuantity = 0
    sumTotal = 0.0
    for i in new_rows:
        # i["extras"] = json.loads(i.get("extras_dumps"))
        product_ids = i.get("product_ids", "[]")
        product_id_list = json.loads(product_ids)
        extras_dumps = i.get("extras_dumps")
        extras = json.loads(extras_dumps)
        products = []
        for product_id in product_id_list:
            single_product = ProductListModel.query.filter_by(product_id=product_id).first()
            single_price = ProductPriceModel.query.filter_by(product_id=product_id).first()
            d = {
                "name": single_product.name,
                "desc": single_product.desc,
                "img_url": single_product.img_url,
                "extras": extras,
                "price":  i.get("price"), #single_price.price_value
                "quantity":  i.get("quantity"), #single_price.price_value
            }
            products.append(d)
        # all_product_data = ProductListModel.query.filter(
        # ProductListModel.product_id.in_(product_id_list)).all()
        # rows = [row for row in data]
        # new_rows = covert_str_to_json(all_product_data)
        print("products--->", products)
        # payload = data.to_dict()
        # payload["price_list"] = json.loads(payload.get("price_list"))
        # 查询商品价格

        # 批量查询所有商品价格，进行统计
        # data2 = ProductPriceModel.query.filter_by(product_id=product_id).first()

        # i.update({
        #     "name": payload.get("name"),
        #     "desc": payload.get("desc"),
        #     "img_url": payload.get("img_url"),
        # })
        sumQuantity += i.get("quantity")
        sumTotal += i.get("price")

    print("new_rows---->", new_rows)
    payload = {
        "products": products,
        "quantity": sumQuantity,
        "total": sumTotal
    }
    return payload