from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app.model import models

app = create_app('development')

# 添加扩展命令行
manager = Manager(app)

# 数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
