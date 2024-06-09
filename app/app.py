from flask import Flask, render_template
from func import calc

app = Flask(__name__)


@app.route("/")
def index():
    x = calc(1,5)
    print("test")
    return (f"test compole {x}")

@app.route("/test")
def test():
    return ("test2")


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
