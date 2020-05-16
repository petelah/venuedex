from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_share import Share
#from flask_mail import Mail
from vd.config import Config
#from wtf_tinymce import wtf_tinymce
#from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.login_message_category = 'info'
share = Share()
#migrate = Migrate()
#mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    share.init_app(app)
    #mail.init_app(app)
    #wtf_tinymce.init_app(app)
    #migrate.init_app(app, db)

    #from flaskblog.users.routes import users
    from vd.posts.routes import posts
    from vd.main.routes import main
    from vd.errors.handlers import errors
    from vd.admin.routes import admin
    app.register_blueprint(admin)
    app.register_blueprint(errors)
    #app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
