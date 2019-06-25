from flask import Blueprint, request, jsonify
from flask_restful import Api,Resource
# from resources import profiles
from flask_restful.reqparse import RequestParser

from apps.common.maketoken import jwtEncoding
from apps.common.utils import trueReturn
from models import User

articles = Blueprint('articles', __name__)

@articles.route('/')
def show():
    return 'app01.hello'

@articles.route('/login', methods=['GET', 'POST'])
def login():
    str = request.get_json()
    print(str)
    name = str['name']

    admin = User.query.filter_by(name=name).first() #这里需要重新修改成成缓存里取，减少处理时间

    userInfo = {
        "id":admin.id,
        "username":admin.name,
        "email":admin.email
    }

    if admin == None:
        return jsonify(trueReturn("{'ok':Flase}", "not the user"))
    else:
        #request.headers['Authorization']='liuliuyyeshibushidslfdslfsdkfkdsf23234243kds'
        #login_user(admin)
        token = jwtEncoding(userInfo)
        print(token)
        return jsonify(trueReturn("{'ok':True,'token':"+token.decode()+"}", "you are sucess"))


api = Api(articles)
# api.add_resource(profiles.ProfileListResource, '/profiles')


class ArticlesView(Resource):
    """
    示例profile list资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        resp={"msg":"获取成功"}
        return resp,201
# from apps.articles import articles
#
# @articles.route('/')
# def index():
# 	return 'articles'