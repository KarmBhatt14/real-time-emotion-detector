import warnings
from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'askhdjabjjkasdj12345ijd'

app.config['SQLALCHEMY_ECHO'] = True

app.config['PERMANENT_sESSION_LIFETIME'] = timedelta(minutes=40)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:root@localhost:3306/expression_detection'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)
app.app_context().push()
from base.com import controller
