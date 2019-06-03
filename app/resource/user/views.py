# from flask import request, jsonify

from . import index_blu
# from . import user_blu


@index_blu.route('/')
def index():
    return 'index'

# @user_blu.route('/login', methords = ["post"])
# def login():
#     """
#        1. 获取参数和判断是否有值
#        2. 从数据库查询出指定的用户
#        3. 校验密码
#        4. 保存用户登录状态
#        5. 返回结果
#        :return:
#        """
#
#     # 1. 获取参数和判断是否有值
#     json_data = request.json
#
#     mobile = json_data.get("mobile")
#     password = json_data.get("password")

    # if not all([mobile, password]):
    #     # 参数不全
    #     return jsonify(errno=RET.PARAMERR, errmsg="参数不全")
    #
    # # 2. 从数据库查询出指定的用户
    # try:
    #     user = User.query.filter_by(mobile=mobile).first()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.DBERR, errmsg="查询数据错误")
    #
    # if not user:
    #     return jsonify(errno=RET.USERERR, errmsg="用户不存在")
    #
    # # 3. 校验密码
    # if not user.check_passowrd(password):
    #     return jsonify(errno=RET.PWDERR, errmsg="密码错误")
    #
    # # 4. 保存用户登录状态
    # session["user_id"] = user.id
    # session["nick_name"] = user.nick_name
    # session["mobile"] = user.mobile
    # # 记录用户最后一次登录时间
    # user.last_login = datetime.now()
    # try:
    #     db.session.commit()
    # except Exception as e:
    #     current_app.logger.error(e)
    # # 5. 登录成功
    # return jsonify(errno=RET.OK, errmsg="OK")