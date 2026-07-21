from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return 
students = [
    {"name": "Rafi", "age": 21},
    {"name": "Amal", "age": 20},
    {"name": "Adil", "age": 22}
]

@app.route("/about")
def about():
    return 

@app.route("/students")
def student():
    return render_template("index.html",student=students)

@app.route("/student/<name>")
def name(name):
    return f"name {name}"

if __name__=="__main__":
    app.run(debug=True)


