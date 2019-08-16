from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis_host = os.environ['redis_host']
redis = Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return '<h1 style="color:orange">Welcome to new Java Home cloud python app - count the number of hits to redis -> {}</h1>'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
