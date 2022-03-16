import string
import random

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import func, text
from enum import unique
from datetime import datetime
from dataclasses import dataclass, field
from typing import List

db = SQLAlchemy()


# ProductListModel 菜单模型
@dataclass
class ProductListModel(db.Model):

    # 数据库表
    __tablename__ = 'product_list'

    # 字段类型
    id: int
    name: str
    product_id: str
    alias: str
    desc: str
    brand: str
    img_url: str
    category: str
    status: str

    # 表字段名称
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False,
    server_default=db.func.current_timestamp(),
    server_onupdate=db.func.current_timestamp())

    # 产品名称
    name = db.Column(db.String(120), unique=True, nullable=True)
    # 产品编号
    product_id = db.Column(db.String(320), nullable=True)
    # 子产品编号 | 例如螺蛳粉 + 肉; 肉为子产品编号
    sub_product_id = db.Column(db.String(320), nullable=True)
    # 产品别名
    alias = db.Column(db.String(120), nullable=True)
    # 产品信息描述
    desc = db.Column(db.Text, nullable=True)
    # 产品品牌
    brand = db.Column(db.String(120), nullable=True)
    # 图片展示
    img_url = db.Column(db.Text, nullable=True)
    # 产品分类: 获取分类列表
    category = db.Column(db.String(120), nullable=True)
    # 状态
    status = db.Column(db.String(120), nullable=True)

    def __repr__(self) -> str:
        return 'product list >>> ' + self.name
    
    # 将数据转为dict
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


# ProductPriceModel 产品价格固化表
@dataclass
class ProductPriceModel(db.Model):

    # 数据库表
    __tablename__ = 'product_price'


    # 字段类型
    id: int
    merchant_id: str
    product_id: str
    sub_product_id: str
    price_value: str # [12, 14, 15]
    price_name: str # ["normal", "vip", "super"]
    status: str

    # 表字段名称
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False,
    server_default=db.func.current_timestamp(),
    server_onupdate=db.func.current_timestamp())

    # 商户编号
    merchant_id = db.Column(db.String(320), nullable=True)
    # 产品编号
    product_id = db.Column(db.String(320),  nullable=True)
    # 子产品编号
    sub_product_id = db.Column(db.String(320), nullable=True)
    # 价格值
    price_value = db.Column(db.String(320), nullable=True)
    # 价格名
    price_name = db.Column(db.String(320), nullable=True)
    # 默认展示价格下标
    default_privce=db.Column(db.Integer, default=0, nullable=True)
    # 状态
    status = db.Column(db.String(120), nullable=True)


# ProductSalesModel 产品销量信息
@dataclass
class ProductSalesModel(db.Model):

    # 数据库表
    __tablename__ = 'product_sales'

    # 字段类型
    id: int
    # 商户订单
    merchant_id: str
    # 产品单
    product_id: str
    # 子单
    sub_product_id: str
    # 热度阀值
    hot_threshold: int
    # 销量
    sales: int
    # 库存
    inventory: int
    # 状态
    status: str

    # 表字段名称
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False,
    server_default=db.func.current_timestamp(),
    server_onupdate=db.func.current_timestamp())

    # 商户编号
    merchant_id = db.Column(db.String(320), nullable=True)
    # 产品编号
    product_id = db.Column(db.String(320), nullable=True)
    # 子产品编号
    sub_product_id = db.Column(db.String(320), nullable=True)
    # 该产品需要达到的阀值后才定义为热度产品
    hot_threshold = db.Column(db.Integer, default=100, nullable=True)
    # 总销量
    sales = db.Column(db.Integer, default=0, nullable=True)
    # 库存 默认为0
    inventory = db.Column(db.Integer, default=0, nullable=True)
    # 状态 true 启用; false 禁用
    status = db.Column(db.String(120), default="true", nullable=True)

    def __repr__(self) -> str:
        return 'product sales >>> ' + self.name
    
    # 将数据转为dict
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}




# Order 消费者订单
@dataclass
class CustomerOrderModel(db.Model):

    # 数据库表
    __tablename__ = 'customer_order'


    # 字段类型
    id: int
    user_id: int
    merchant_id: int
    status: int
    order_id: str


    # 表字段名称
    # 自增id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.now())
    # 更新时间
    updated_at = db.Column(db.DateTime, nullable=False,
    server_default=db.func.current_timestamp(),
    server_onupdate=db.func.current_timestamp())
    # 用户 id
    user_id = db.Column(db.Integer, nullable=True)
    # 商户id
    merchant_id = db.Column(db.Integer, nullable=True)
    # 订单状态 0.成功; 1.退款; 2.支付失败;
    status = db.Column(db.Integer, nullable=True)
    # 用户可以通过该字段进行消费详情查询
    order_id = db.Column(db.String(320), nullable=False)

    # pay_method: 0:现金到付；1: 线上支付
    pay_method = db.Column(db.Integer, nullable=True)

    # 将数据转为dict
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


    def __repr__(self) -> str:
        return 'Order >>> ' + self.username


# Order 消费者订单
@dataclass
class OrderProductList(db.Model):

    # 数据库表
    __tablename__ = 'order_product_list'

    # 字段类型
    id: int
    customer: str
    address: str
    total: str
    method: str
    img_url: str


    # 表字段名称
    # 自增id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.now())
    # 更新时间
    updated_at = db.Column(db.DateTime, nullable=False,
    server_default=db.func.current_timestamp(),
    server_onupdate=db.func.current_timestamp())


    customer = db.Column(db.String(320), nullable=True)

    address = db.Column(db.String(320), nullable=True)

    total = db.Column(db.Integer, nullable=True)

    method = db.Column(db.Integer, nullable=True)

    # 头像地址
    img_url = db.Column(db.String(1024), nullable=True)

    status = db.Column(db.Integer, nullable=True)

    # 将数据转为dict
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


    def __repr__(self) -> str:
        return 'Order product list>>> ' + self.customer

# ============================== 支付 ===========================
# PayByCash 订单支付信息
@dataclass
class PayByCashModel(db.Model):

    # 数据库表
    __tablename__ = 'pay_by_cash'

    # 字段类型
    id: int
    username: str
    # 产品具体信息id
    product_id: str
    # name: str
    # desc: str
    price: float
    # total: float
    quantity: int
    # img_url: str
    extras_dumps: str
    status: int

    # 表字段名称
    # 自增id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.now())
    # 更新时间
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    # Product	Name	Extras	Price	Quantity	Total
    username = db.Column(db.String(320), nullable=True)
    product_id = db.Column(db.Integer, nullable=True)
    # name = db.Column(db.String(320), nullable=True)
    # desc = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=True)
    # total = db.Column(db.Float, nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    # img_url = db.Column(db.String(1024), nullable=True)
    extras_dumps = db.Column(db.Text, nullable=True)
    # 0 仅添加; 1 已经购买过；2 已经付款
    status = db.Column(db.Integer, nullable=True)

    # 将数据转为dict
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


    def __repr__(self) -> str:
        return 'Cart >>> ' + self.username + "_" + str(self.product_id)

# ============================== 流水 ===========================

# ProductOfCartModel 消费者购物车
@dataclass
class ProductOfCartModel(db.Model):

    # 数据库表
    __tablename__ = 'product_of_cart'

    # 字段类型
    id: int
    username: str
    # 产品具体信息id
    product_ids: str
    # name: str
    # desc: str
    price: float
    # total: float
    quantity: int
    # img_url: str
    extras_dumps: str
    status: int

    # 表字段名称
    # 自增id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.now())
    # 更新时间
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    # Product	Name	Extras	Price	Quantity	Total
    username = db.Column(db.String(320), nullable=True)
    product_ids = db.Column(db.Text, nullable=True)
    # name = db.Column(db.String(320), nullable=True)
    # desc = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=True)
    # total = db.Column(db.Float, nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    # img_url = db.Column(db.String(1024), nullable=True)
    extras_dumps = db.Column(db.Text, nullable=True)
    # 0 仅添加; 1 已经购买过；2 已经付款
    status = db.Column(db.Integer, nullable=True)

    # 将数据转为dict
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


    def __repr__(self) -> str:
        return 'Cart >>> ' + str(self.id)