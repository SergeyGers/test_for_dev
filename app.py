from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["name"]
    return f"<h2>Hello, {name}! Welcome to our site!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
