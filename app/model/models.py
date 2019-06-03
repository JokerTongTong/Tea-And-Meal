#定义用户数据模型
from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = "user"  #存入表名称
    #column字段  unique唯一
    id = db.Column(db.Integer, primary_key=True) #编号
    nick_name = db.Column(db.String(100),unique=True) #昵称，唯一性
    avatar_url = db.Column(db.String(100))
    mobile = db.Column(db.String(11),unique=True) #手机，唯一性
    password_hash = db.Column(db.String(255), nullable=False)  # 密码，不允许为空
    last_login = db.Column(db.DateTime, nullable=True) # 最后一次登录时间，允许为空
    is_admin = db.Column(db.Boolean,default=0) # 管理员，默认为0，否
    signature = db.Column(db.String(255),default=None)
    gender = db.Column(db.String(40), default="男")



    # email = db.Column(db.String(100),unique=True)  #邮箱
    # phone = db.Column(db.String(11),unique=True)  #手机号码
    # info = db.Column(db.Text)   #个性简介
    # face = db.Column(db.String(255),unique=True)  #头像
    # addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    # uuid = db.Column(db.String(255),unique=True)  #唯一标识符
    # userlogs = db.relationship('Userlog',backref='user') #会员日志外键关系
    # comments = db.relationship('Comment',backref='user') #评论外键关系
    # moviecols = db.relationship('Moviecol',backref='user') #收藏外键关系

    # 定义一个方法，返回的类型
    def __repr__(self):
        return "<User %r>" % self.nick_name

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    # 转换密码为hash存入数据库
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 检查密码
    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


# arctire_tag = Table(
# "arctire_tag"       #表名
# Base.metadata   #表继承的类
# Column(“arctire_id” , Integer , primary_key=True , ForeignKey("arctire.id")      #arctire_id 为字段名
# Column("tag_id" , Integer , primary_key=True , ForeignKey("tag.id")   
# )
