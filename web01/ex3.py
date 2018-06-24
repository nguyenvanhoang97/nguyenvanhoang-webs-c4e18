from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    users = {
        
        "Manh" : {
            "name" : "Manh",
            "age" : 23
        },
        
        "Hoang" : {
            "name" : "Hoang",
            "age" : 21
        }
    }

    return render_template("ex3.html", users = users , username = username)


if __name__ == '__main__':
  app.run(debug=True)