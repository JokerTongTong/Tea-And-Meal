from _datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__) #创建实例化app对象
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/test_tam"
# # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  #配置，如果设置True,将会追踪对象修改并且发送信号
# db = SQLAlchemy(app)  #定义db，传入app对象
#定义用户数据模型
from app import db


class User(db.Model):
    __tablename__ = "user"  #存入表名称
    #column字段  unique唯一
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100),unique=True) #昵称
    pwd = db.Column(db.String(100))  #密码
    email = db.Column(db.String(100),unique=True)  #邮箱
    phone = db.Column(db.String(11),unique=True)  #手机号码
    info = db.Column(db.Text)   #个性简介
    face = db.Column(db.String(255),unique=True)  #头像
    addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    uuid = db.Column(db.String(255),unique=True)  #唯一标识符
    userlogs = db.relationship('Userlog',backref='user') #会员日志外键关系
    comments = db.relationship('Comment',backref='user') #评论外键关系
    moviecols = db.relationship('Moviecol',backref='user') #收藏外键关系

    # 定义一个方法，返回的类型
    def __repr__(self):
        return "<User %r>" % self.name
