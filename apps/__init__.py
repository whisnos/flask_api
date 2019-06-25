'''
pip install flask-restful
pip install Flask-MySQLdb
pip install flask-migrate
pip install flask_script
pip install Flask-JWT
pip install pymysql
'''
import flask_restful
from flask import Flask, jsonify, make_response, abort
from flask_jwt import JWT
from flask_login import LoginManager
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from flask_mysqldb import MySQL
login_manager = LoginManager()
from apps.common import pretty_result, code
# from models import db
from apps.models import db

def _custom_abort(http_status_code, **kwargs):
    """
    自定义abort 400响应数据格式
    """
    if http_status_code == 400:
        message = kwargs.get('message')
        if isinstance(message, dict):
            param, info = list(message.items())[0]
            data = '{}:{}!'.format(param, info)
            return abort(jsonify(pretty_result(code.PARAM_ERROR, data=data)))
        else:
            return abort(jsonify(pretty_result(code.PARAM_ERROR, data=message)))
    return abort(http_status_code)

def _access_control(response):
    """
    解决跨域请求
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,HEAD,PUT,PATCH,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Max-Age'] = 86400
    return response

def create_app(config):
    """
    创建app
    """
    app = Flask(__name__)
    api = Api(app, prefix='/api/v1')
    # 保留flask原生异常处理
    handle_exception = app.handle_exception
    handle_user_exception = app.handle_user_exception
    # 添加配置
    app.config.from_object(config)
    # 解决跨域
    app.after_request(_access_control)
    # 自定义abort 400 响应数据格式
    flask_restful.abort = _custom_abort
    # 认证
    # from apps.auth.auths import Auth
    # auth = Auth()
    # jwt = JWT(app, auth.authenticate, auth.identity)

    # 数据库初始化
    db.init_app(app)
    db.create_all(app=app)
    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    # 注册蓝图
    register_blueprint(app)
    # from apps.routes import api_v1
    # from apps.articles import articles
    # from apps.users import users
    # app.register_blueprint(api_v1, url_prefix='/api/v1')
    # app.register_blueprint(articles, url_prefix='/articles')
    # app.register_blueprint(users, url_prefix='/users')
    # # 使用flask原生异常处理程序
    app.handle_exception = handle_exception
    app.handle_user_exception = handle_user_exception
    return app

def register_blueprint(app):
    # 注册蓝图
    from apps.routes import api_v1
    from apps.articles import articles
    from apps.users import users
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    app.register_blueprint(articles, url_prefix='/articles')
    app.register_blueprint(users, url_prefix='/users')

