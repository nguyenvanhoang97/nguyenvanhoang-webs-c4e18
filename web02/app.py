from flask import Flask, render_template
import mlab
from models.service import Service

app = Flask(__name__)

#0. create connection
mlab.connect()

# new_service = Service(
#     name = "Đạt 100",
#     yob = 1996,
#     gender = 1,
#     height = 174,
#     phone = "0123456789",
#     address = "Trần Duy Hưng",
#     status = False
# )
# new_service.save()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender = gender , yob__lte = 1998 , address__icontains = "Hà Nội")
    return render_template("search.html" , all_service = all_service)
#search id
@app.route('/searchid/<id>')
def searchid(id):
    service = Service.objects.with_id(id)
    return render_template("searchid.html" , service = service)

#chưa lm được phần xóa id

#delete id
# @app.route('/dele/<id>')
# def dele(id):
#     Service.objects(type=id).delete()
#     return "Xóa thành công"

if __name__ == '__main__':
    app.run(debug=True)