from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# For security reasons, many modern web frameworks actually limit incoming connections to only come from localhost.
# This means that our Flask app is running, but only accessible from within the Docker container, not from our Mac host.
# The easiest way to fix this is to add `host=’0.0.0.0’` as a keyword argument to `app.run()` in main.py:

# This change tells Flask to listen not only to requests from localhost (in this case the docker container),
# but on all network connections. In the case of our container this means we can access it from our host,
# and depending on configuration from other computers in our network.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
