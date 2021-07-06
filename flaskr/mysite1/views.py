# mysite1/views.py
from flask import Blueprint,render_template

#home.htmlの<a href="{{url_for('mysite1.hello')}}">mysite1</a>のurl_forに該当するところが下記引数一つ目のmysite1
mysite1_bp = Blueprint('mysite1', __name__, url_prefix='/site1')

#https://wwww.aaa/site1/hello にアクセスされると以下の関数が実行される
@mysite1_bp.route('/hello')
def hello():
    return render_template('mysite1/hello.html')