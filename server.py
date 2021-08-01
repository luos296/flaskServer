#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
# 解决跨域
CORS(app, supports_credentials=True)

username = 'root'
pwd = 'ls296760'
ip = '127.0.0.1'
port = '3306'
database = 'demo'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# start
if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    from apis.testcase import TestCaseServer
    api.add_resource(TestCaseServer, '/testcase')
    app.run(debug=True)