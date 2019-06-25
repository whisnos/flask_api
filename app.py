'''
pip install flask-restful
pip install Flask-MySQLdb
pip install flask-migrate
pip install flask_script
pip install Flask-JWT
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
from models import db

app = Flask(__name__)
api = Api(app, prefix='/api/v1')
# 保留flask原生异常处理
handle_exception = app.handle_exception
handle_user_exception = app.handle_user_exception
# MySQL configurations
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'blog_api'
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# mysql = MySQL(app)
# article_request_parser = RequestParser(bundle_errors=True)
#
# article_request_parser.add_argument('title', type=str, required=True, help='Title must be string')
# article_request_parser.add_argument('content', type=str, required=True, help='Content must be string')

# from apps.articles import articles
# app.register_blueprint(articles, url_prefix='/')

# class ArticleCollection(Resource):
#     def get(self):
#         cur = mysql.connection.cursor()
#         cur.execute('''SELECT id, title, content FROM articles''')
#         articles = cur.fetchall()
#
#         return make_response(jsonify(articles), 200)
#
#     def post(self):
#         args = article_request_parser.parse_args()
#         cur = mysql.connection.cursor()
#         query = '''INSERT INTO articles (title, content) VALUES ('{title}', '{content}')'''.format(**args)
#
#         cur.execute(query)
#         cur.connection.commit()
#         return { 'msg': 'New article created.', 'data': args }, 201
#
#
# class Article(Resource):
#     def get(self, id):
#         cur = mysql.connection.cursor()
#         cur.execute('''SELECT id, title, content FROM articles WHERE id = {id}'''.format(id=id))
#         article = cur.fetchone()
#         if not article:
#             return { 'error': 'article not found of id {id}'.format(id=id) }
#         return article, 200
#
#     def put(self, id):
#         args = article_request_parser.parse_args()
#         cur = mysql.connection.cursor()
#         query = '''UPDATE articles SET title = '{title}', content = '{content}' WHERE id = {id}'''.format(**args, id=id)
#         cur.execute(query)
#         cur.connection.commit()
#
#         return { 'msg': 'Article updated.', 'data': args }, 200
#
#     def delete(self, id):
#         cur = mysql.connection.cursor()
#         query = '''DELETE FROM articles WHERE id = {id}'''.format(id=id)
#         cur.execute(query)
#         cur.connection.commit()
#         return { 'msg': 'Article Deleted' }, 202

# api.add_resource(ArticleCollection, '/articles/')
# api.add_resource(Article, '/articles/<int:id>')
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
    # 添加配置
    app.config.from_object(config)
    # 解决跨域
    app.after_request(_access_control)
    # 自定义abort 400 响应数据格式
    flask_restful.abort = _custom_abort
    # 认证
    from apps.auth.auths import Auth
    auth = Auth()
    jwt = JWT(app, auth.authenticate, auth.identity)

    # 数据库初始化
    db.init_app(app)

    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    # 注册蓝图
    from apps.routes import api_v1
    from apps.articles import articles
    from apps.users import users
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    app.register_blueprint(articles, url_prefix='/articles')
    app.register_blueprint(users, url_prefix='/users')
    # 使用flask原生异常处理程序
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
# if __name__ == '__main__':
#     app.run(debug=True)


# from apps.users import users
# from apps.center import center
#
# app.register_blueprint(users, url_prefix='/')
# app.register_blueprint(center, url_prefix='/center')

