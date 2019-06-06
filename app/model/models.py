from sqlalchemy import Table
from app import db
from werkzeug.security import generate_password_hash,check_password_hash


#定义用户数据模型
class User(db.Model):
    """
        用户表
    """
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


class News(db.Model):
    """
        新闻表
    """
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(100), unique=True)  # 标题
    content = db.Column(db.String(1000))  # 内容
    source = db.Column(db.String(100))   # 作者/来源
    index_image_url = db.Column(db.String(100))  # 图片连接fastDFS
    create_time = db.Column(db.DateTime)   # 发布时间
    clicks = db.Column(db.Integer)  # 点击量
    status = db.Column(db.Integer) # 状态 审核状态
    # 外键
    category_id = db.Column(db.Integer,db.ForeignKey("category.id"))   # 类别/话题
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))      # 用户/谁发布


class Comment(db.Model):
    """
        评论表
    """
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.String(1000))  # 内容
    create_time = db.Column(db.DateTime)   # 评论时间
    floor = db.Column(db.Integer)  # 第几楼
    like_count = db.Column(db.Integer,default=0) # 点赞数量

    # 外键
    news_id = db.Column(db.Integer,db.ForeignKey("news.id"))  # 类别/话题
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))      # 用户/谁发布


class Category(db.Model):
    """
        新闻种类/话题
    """
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(500))


# 用户收藏新闻 关系 表
User_Collection = Table(
    "user_collection",  # 表名
    db.Model.metadata,  # 表继承的类
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("collection_id", db.Integer, db.ForeignKey("news.id"), primary_key=True),
    db.Column("create_time", db.DateTime)  # create_time 字段名
)

# 用户点赞评论 关系表
Comment_Like = Table(
    "comment_like",
    db.Model.metadata,
    db.Column("comment_id", db.Integer, db.ForeignKey("comment.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)

# 用户点赞新闻 关系表
News_Like = Table(
    "news_like",
    db.Model.metadata,
    db.Column("news_id", db.Integer, db.ForeignKey("news.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)

# 粉丝 关系表
User_Fans = Table(
    "user_fans",
    db.Model.metadata,
    db.Column("follower_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("followered_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
)











