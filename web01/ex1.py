from flask import Flask, render_template
app = Flask(__name__)
    
@app.route('/about-me')
def myself():
    info = [
        {
            "name" :"Nguyen Van Hoang",
            "age" : 21,
            "address" : "Ha Noi"
        }
    ]
    return render_template("myself.html", info = info )



if __name__ == '__main__':
  app.run(debug=True)