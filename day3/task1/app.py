from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/form")
def form():
    return render_template ("form.html")

@app.route("/studentform", methods=["POST"])
def studentform():
    name= request.form["Name"]
    return f"hellow {name}"

@app.route("/table")

def table():
    student= [{ "name":"raeff", "age":21},{ "name":"fwaeff", "age":221},{ "name":"raeff", "age":21}]
    return render_template("table.html",student=student)


if __name__ == '__main__':
    app.run(debug=True)