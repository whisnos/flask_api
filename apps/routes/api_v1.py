# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
# from resources import profiles
from apps.articles.views import ArticlesView
from apps.users.views import UserInfoViewset, login

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

api.add_resource(ArticlesView, '/articles')
api.add_resource(UserInfoViewset, '/users')
