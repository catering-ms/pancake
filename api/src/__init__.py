# 标准库
import sys
import os
import logging

# 第三方
from flask import Flask
from flask_cors import CORS
import json_logging

# 内部
from src.database.model import db
from src.posts import posts

# init the logger as usual
logger = logging.getLogger("test-logger")



def create_app(test_config=None):
    app = Flask(__name__, 
    instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
        )
    else:
        app.config.from_mapping(test_config)
    
    # 初始化数据库
    db.app = app
    db.init_app(app)

    # 
    app.register_blueprint(posts)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # 设置跨域
    CORS(app, resources={r"/posts": {"origins": "http://localhost:3000"}})
    
    # 设置日志

    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init_flask(enable_json=True)
    json_logging.init_request_instrument(app)

    # # init the logger as usual
    logger = logging.getLogger("test-logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.info("create flask application successful")
    return app