from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2
from Db import db
from Db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/cheak')
def main():
    my_users = users.query.all()
    print(my_users)
    return ' result in console'

@lab6.route("/lab6/checkarticles")
def checkarticles():
    all_articles= articles.query.all()
    print(all_articles)
    return "result in console!"