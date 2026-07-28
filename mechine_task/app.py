from flask import Flask,render_template, request
from calcutions import calcutions
app=Flask(__name__)

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calcution():
    try:
        name=(request.form.get("name"))
        maths=int(request.form.get("maths"))
        science=int(request.form.get("science"))
        eng=int(request.form.get("english"))
    except:
        return f"must all feilds required "
    if name=="" or maths=="" or science=="" or eng=="":
        return f" fill all feilds " 
    if maths<0 or maths>=100 or science<0 or science>+100 or eng<0 or eng>=100 :
        return f"must all marks are between 0 and 100"
    name,total,average,grade,remark=calcutions(name,maths,science,eng)
    return render_template("calculate.html",name=name, total=total, average=average, grade=grade, remark=remark)




if __name__==("__main__"):
    app.run(debug=True)