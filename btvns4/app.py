from flask import *
import mlabservice
from models.service import Service
from models.service import User
from models.service import Order
from datetime import datetime


app = Flask(__name__)

#0. create connection
mlabservice.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ["GET","POST"])
def login():
    all_user = User.object()
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        for user in all_user:
            if username == user.username and password == user.password:
                return redirect(url_for('detail'))
            else:
                return "Sai mat khau hoac tai khoan"

@app.route('/detail')
def detail():
    all_service = Service.objects()
    return render_template('detail.html', all_service = all_service)

@app.route('/order/<id_user>/<id_doitac>')
def order(id_user , id_doitac):
    order = Order.objects()
    new_order = Order(
        id_doitac = id_doitac,
        id_nguoidung = id_user,
        thoigian = datetime.now(),
        is_accepted = False
    )    
    new_order.save()
    return "gửi yêu cầu"

@app.route('/newuser' , methods = ["GET" , "POST"])
def newuser():
    if request.method == "GET":
        return render_template("newuser.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        email = form["email"]
        fullname = form["fullname"]

        new_user = User(
            username = "username",
            password = "password",
            email = "email",
            fullname = "fullname"
        )
        new_user.save()
        return "Thêm thành công"

@app.route('/pheduyet')
def pheduyet():
    all_order = Order.objects()
    list_id = []
    for order in all_order:
        id_nguoidung = order.id_nguoidung
        id_doitac = order.id_doitac
        user = User.object.with_id(id_nguoidung)
        nguoidung = user.username
        service = Service.object.with_id(id_doitac)
        doitac = service.name
        thoigian = order.datetime
        trangthai = order.is_accepted
        list_id.append(nguoidung , doitac , thoigian , trangthai)
    return render_template("order.html" , list_id = list_id)


if __name__ == '__main__':
    app.run(debug=True)