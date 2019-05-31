from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app

app = create_app('development')

# 添加扩展命令行
manager = Manager(app)

# 数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)


# @app.route('/index')
# def index():
#     return 'index'


if __name__ == '__main__':
    manager.run()
# db = SQLAlchemy(app)
# redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# CSRFProtect(app)
# Session(app)
# manager = Manager(app)
# Migrate(app, db)
# manager.add_command('db', MigrateCommand)