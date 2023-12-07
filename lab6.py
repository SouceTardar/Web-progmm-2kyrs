from flask import Blueprint, render_template, request, redirect, session, url_for
from DB import db
from werkzeug.security import check_password_hash, generate_password_hash
from Db.models import users, articles
from flask_login import login_user, login_required, current_user

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/cheak')
def main():
    my_users = users.query.all()
    print(my_users)
    return ' result in console'