from flask import Flask, request, render_template
import pandas as pd
app=Flask(__name__)

def grade(avarage):
        if avarage>=90:
            return f"A+"
        elif avarage>=80:
            return f"A"
        elif avarage>=70:
            return f"B+"
        elif avarage>= 60:
            return f"B"
        else :
            return f"Fail"
        
def calculation(data):
    data["total"]=data["Maths"]+data["English"]+data["Science"]
    data["average"]=round(data["total"]/3)
    data["grade"]=data["average"].apply(grade)
    return data


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/act", methods=["POST"])
def table():
    global data
    data=request.files["csv"]
    data=pd.read_csv(data)

    return render_template("table.html",table=data.to_html())
@app.route("/summary")
def summary():
    
    global data
    data=calculation(data)

    return render_template("summary.html",table2=data.to_html())

if __name__=="__main__":
    app.run(debug=True)


        