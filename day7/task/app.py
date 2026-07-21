from flask import Flask, request, render_template, jsonify
import pandas as pd
from calculation import calcutions, grade, total
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({ "status" : "working"})

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data=request.get_json()

    df=pd.DataFrame(data["students"])
    df=calcutions(df)
    class_average, class_topper = total(df)
    return jsonify({ "class topper": str(class_topper), 
                    "class_average": float(class_average),
                    "data" : df.to_dict(orient="records") })
@app.route("/name/<name>")
def name(name):
    return f"name:  {name}"

@app.route("/act", methods=["POST","GET"])
def act():
    data=request.files["csv"]
    data=pd.read_csv(data)
    data=calcutions(data)
    classavarge, classtopper=total(data)
    
        
    return render_template("summary.html",table=data.to_html(), classavarge=round(classavarge), classtopper=classtopper )



if __name__==("__main__"):
    app.run(debug=True)