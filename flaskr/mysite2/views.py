# mysite1/views.py
from flask import Blueprint,render_template

mysite2_bp = Blueprint('mysite2', __name__, url_prefix='/site2')

#https://wwww.aaa/site2/hello にアクセスされると以下の関数が実行される
@mysite2_bp.route('/hello')
def hello():
    return render_template('mysite2/hello.html')