import config
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, and_
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask import Flask, request, send_file, render_template, redirect, abort, session, url_for, make_response, jsonify
from datetime import timedelta, datetime
import random
from openpyxl import Workbook
from io import BytesIO


app = Flask(__name__)
app.config.update(SECRET_KEY=config.SECRET_KEY)
app.permanent_session_lifetime = timedelta(days=365)




