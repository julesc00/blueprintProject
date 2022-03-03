from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return "Contact me at '555-5555' or email me at test@somewhere.com"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    else:
        pass


if __name__ == '__main__':
    app.run()
