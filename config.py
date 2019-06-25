# -*- coding: utf-8 -*-
import os
import multiprocessing

MODE = 'develop'  # develop: 开发模式; production: 生产模式


class ProductionConfig(object):
    """
    生产配置
    """
    BIND = '127.0.0.1:5000'
    WORKERS = multiprocessing.cpu_count() * 2 + 1
    WORKER_CONNECTIONS = 10000
    BACKLOG = 64
    TIMEOUT = 60
    LOG_LEVEL = 'INFO'
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), 'logs')
    LOG_FILE_MAX_BYTES = 1024 * 1024 * 100
    LOG_FILE_BACKUP_COUNT = 10
    PID_FILE = 'run.pid'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'example.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(object):
    """
    开发配置
    """
    BIND = '0.0.0.0:5000'
    WORKERS = 2
    WORKER_CONNECTIONS = 1000
    BACKLOG = 64
    TIMEOUT = 30
    LOG_LEVEL = 'DEBUG'
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), 'logs')
    LOG_FILE_MAX_BYTES = 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 1
    PID_FILE = 'run.pid'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'example.db')
    SQLALCHEMY_DATABASE_URI = ('mysql+pymysql://root:root@127.0.0.1:3306/flask_test')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT_AUTH_URL_RULE = '/login'


if MODE == 'production':
    config = ProductionConfig
else:
    config = DevelopConfig
