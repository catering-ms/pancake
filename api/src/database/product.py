import json

from sqlalchemy import update
from src.database.model import ProductListModel, db
from src.database.model import ProductPriceModel
from src.database.model import ProductSalesModel
from src.database.model import PayByCashModel
from src.database.model import CustomerOrderModel

from src.utils.gjson import covert_str_to_json


# 产品注册
def get_product():
    status="true" # is working staus
    data = ProductListModel.query.filter_by(status=status).all()
    rows = covert_str_to_json(data)
    new_rows = []
    for i in rows:
        _id = i.get("id")
        product_id = i.get("product_id")
        sub_product_id = i.get("sub_product_id")
        # 查询商品定价信息
        data = ProductPriceModel.query.filter_by(
            product_id=product_id,
            sub_product_id=sub_product_id
            ).first()
        price_list =  json.loads(data.price_value)
        # 查询销量信息
        data = ProductSalesModel.query.filter_by(
            product_id=product_id,
            sub_product_id=sub_product_id
            ).first()
        sales = data.sales

        d = {
            "id": _id,
            "name": i.get("name"),
            "desc": i.get("desc"),
            "img_url": i.get("img_url"),
            "price_list": price_list,
            "sales": sales
        }
        new_rows.append(d)

    return new_rows

# 产品详情
def get_product_detail(_id):
    status="true" # is working staus
    print("_id ---->", _id)
    # 查询产品信息
    data = ProductListModel.query.filter_by(id=_id).first()
    # 查询价格配置
    price_obj = ProductPriceModel.query.filter_by(
        product_id=data.product_id,
        # sub_product_id=data.sub_product_id
    ).first()

    # 查询子产品信息
    # sub_data = ProductListModel.query.filter_by(
    #     product_id=data.product_id
    #     ).all()

    sub_product_id_list = json.loads(data.sub_product_id)

    sub_data = ProductListModel.query.filter(
         ProductListModel.product_id.in_(sub_product_id_list)).all()

    rows = covert_str_to_json(sub_data)
    
    extraOptions = []
    for i in rows:
        price_obj = ProductPriceModel.query.filter_by(
        product_id=i.get("product_id")).first()

        d = {
            "product_id": i.get("product_id"),
            "id": i.get("id"),
            "text": i.get("name"),
            "price": json.loads(price_obj.price_value)[0]
        }
        extraOptions.append(d)

    d = {
        "id": data.id,
        "product_id": data.product_id,
        "name": data.name,
        "desc": data.desc,
        "img_url": data.img_url,
        "price_list": json.loads(price_obj.price_value),
        "extraOptions": extraOptions
    }
    return d

# # 产品进件
# def add_product(product_id, sub_product_id, merchant_id, number):

#     data = ProductSalesModel.query.filter_by(
#         product_id=product_id,
#         sub_product_id=sub_product_id,
#         merchant_id=merchant_id
#     ).first()
#     db.session.execute(
#          update(ProductSalesModel).
#          where(
#              ProductSalesModel.product_id == product_id,
#              ProductSalesModel.sub_product_id == sub_product_id,
#              ProductSalesModel.merchant_id == merchant_id
#              ).
#          values(inventory=data.inventory+number)
#          )

#     # 更新库存
#     db.session.commit()

def add_product():
    # 查看商品当前库存及信息
    m = MenuModel.query.filter_by(menu_id=id).all()

    # 写入订单信息
    m1 = CustomerOrderModel(
        user_id=user_id,
        merchant_id=merchant_id,
        status=defaut_order_status,
        order_id=order_id,
        pay_method=method
    )
    db.session.add(m1)
    
    # 支付方式 
    # method: 0:现金到付；1: 线上支付
    if method == 0:
        m = PayByCashModel(
            customer=customer, 
            address=address, 
            total=total,
            method=method,
            img_url=img_url,
        status=status)
        db.session.add(m)
    db.session.commit()
    db.session.refresh(m)

