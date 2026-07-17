from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/out", methods=["POST"])

def out():

    name=request.form.get("name")
    age=int(request.form.get("age"))
    email=request.form.get("email")
    course=request.form.get("course")

    if age<=0:
        return "Age must be greater than 0", 400
    else:
        return f" NAME : {name} <br> Age: {age} <br>  Email: {email} <br> Course: {course}"
    



if __name__=="__main__":
    app.run(debug=True)