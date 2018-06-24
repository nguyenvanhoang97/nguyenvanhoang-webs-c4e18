from flask import Flask, render_template
import mlab
app = Flask(__name__)
from models.cus import Service

mlab.connect()

@app.route('/')
def customer():
    all_service= Service.objects()
    return render_template("customer.html", all_service= all_service)

if __name__ == '__main__':
  app.run(debug=True)