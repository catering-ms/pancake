import json

from sqlalchemy import update
from src.database.model import CustomerOrderModel
from src.database.model import PayByCashModel

from src.utils.gjson import covert_str_to_json


def add_order():
    print("is add order ...")
    # 查看商品当前库存及信息
    # m = MenuModel.query.filter_by(menu_id=id).all()

    # 写入订单信息
    # m1 = CustomerOrderModel(
    #     user_id=user_id,
    #     merchant_id=merchant_id,
    #     status=defaut_order_status,
    #     order_id=order_id,
    #     pay_method=method
    # )
    # db.session.add(m1)
    
    # 支付方式 
    # method: 0:现金到付；1: 线上支付
    # if method == 0:
    #     m = PayByCashModel(
    #         customer=customer, 
    #         address=address, 
    #         total=total,
    #         method=method,
    #         img_url=img_url,
    #     status=status)
    #     db.session.add(m)
    # db.session.commit()
    # db.session.refresh(m)

