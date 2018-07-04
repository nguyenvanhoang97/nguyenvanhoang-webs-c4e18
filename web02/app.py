from flask import *
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
    all_service = Service.objects(gender = gender )#, yob__lte = 1998 , address__icontains = "Hà Nội")
    return render_template("search.html" , all_service = all_service)
#search id
@app.route('/searchid/<id>')
def searchid(id):
    service = Service.objects.with_id(id)
    return render_template("searchid.html" , service = service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template("admin.html" , all_service = all_service)

@app.route('/dele/<service_id>')
def dele(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is None:
        print("Not found")
    else:
        service_to_delete.delete()
        return redirect(url_for('admin'))

@app.route('/newservice' , methods = ["GET" , "POST"])
def newservice():

    if request.method == "GET":
        return render_template("newservice.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        address = form["address"]

        new_service = Service(
            name = "name",
            yob = yob,
            address = "address"
        )
        new_service.save()

        return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)