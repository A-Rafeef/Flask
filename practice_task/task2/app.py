from flask import Flask, request, render_template

app=Flask(__name__)

def check(name,age,course):
    if name=="" or age=="" or course=="":
        return "fill all feilds"
    else : 
        return f"""name: {name}
                age:{age}
                course: {course} """

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/form", methods=["POST"])
def form():

    try:
        name=request.form["name"]
        age=request.form["age"]
        course=request.form["course"]
        result=check(name,age,course)
        return result
        
    except:
        return f" ivalid out put, or fill all details"

    
   



if __name__==("__main__"):
    app.run(debug=True)
