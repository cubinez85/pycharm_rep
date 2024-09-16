# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#   return "Hello from flask"
# if __name__ == "__main__":
#   app.run()

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
   return '<h1>Hello from cubinez85<h1>'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
   return render_template('hello.html', name=name)
if __name__ == "__main__":
   app.run()
