import json

from sqlalchemy import update
from src.database.model import ProductListModel, db
from src.database.model import ProductPriceModel
from src.database.model import ProductSalesModel

from src.utils.id import get_product_id
from src.utils.id import get_sub_product_id


# 产品注册
# sub_product_id 选择该产品附带支持的子产品列表
def register_product(name, sub_product_id):
    # name="a"
    alias="alias-a"
    desc="desc abc"
    brand="brand"
    img_url="https://www.zhifure.com/upload/images/2018/9/17113536844.jpg"
    category="none"
    status="true" # is working staus
    product_id=get_product_id()
    # sub_product_id=get_sub_product_id()
    # 商户信息
    merchant_id="mch-001"
    price_value = json.dumps([
        12.30,
        13.40,
        15.30
    ])
    price_name = json.dumps([
        "normal",
        "vip",
        "super"
    ])

    # 产品列表展示
    m = ProductListModel(
        name=name,
        product_id=product_id,
        sub_product_id=sub_product_id,
        alias=alias,
        desc=desc,
        brand=brand,
        img_url=img_url,
        category=category,
        status=status
    )
    db.session.add(m)

    # 产品价格
    m2 = ProductPriceModel(
        merchant_id=merchant_id,
        product_id=product_id,
        sub_product_id=sub_product_id,
        price_value=price_value,
        price_name=price_name,
        status=status
    )
    db.session.add(m2)

    # 产品销售库存
    m3 = ProductSalesModel(
        merchant_id=merchant_id,
        product_id=product_id,
        sub_product_id=sub_product_id,
    )
    db.session.add(m3)
    db.session.commit()

# 产品进件
def add_product(product_id, merchant_id, number):

    data = ProductSalesModel.query.filter_by(
        product_id=product_id,
        # sub_product_id=sub_product_id,
        merchant_id=merchant_id
    ).first()
    db.session.execute(
         update(ProductSalesModel).
         where(
             ProductSalesModel.product_id == product_id,
            #  ProductSalesModel.sub_product_id == sub_product_id,
             ProductSalesModel.merchant_id == merchant_id
             ).
         values(inventory=data.inventory+number)
         )

    # 更新库存
    db.session.commit()

