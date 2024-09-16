from flask import Flask

from flask_moment import Moment

app = Flask(__name__)


moment = Moment(app)

t = moment('2021-06-28T21:45:23+00:00')

print(t)