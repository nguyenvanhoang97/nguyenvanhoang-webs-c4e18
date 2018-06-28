from flask import *
import mlab
from models.service import Service


app = Flask(__name__)

#0. create connection
mlab.connect()

@app.route('/delete')
def delete():
    all_service = Service.objects()
    for service in all_service:
        service.delete()
    return "Xóa thành công"

@app.route('/detail/<id>')
def detail(id):
    service = Service.objects().with_id(id)
    return render_template('detail.html', service = service)

@app.route('/update/<id>')
def update(id):
    service = Service.objects().with_id(id)
    return render_template('update.html', service = service)

@app.route('/continent/<continent>')
def continent(continent):
    river = River.objects(continent = continent)
    return render_template('continent.html', river = river)

@app.route('/lenght')
def lenght():
    all_river = River.objects(lenght__lte = 1000)
    return render_template('lenght.html', all_river = all_river)

if __name__ == '__main__':
    app.run(debug=True)