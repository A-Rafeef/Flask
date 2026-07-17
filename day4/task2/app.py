from flask import Flask, render_template, request
import pandas as pd
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/act", methods=["POST","GET"])
def act():
    file2=request.files.get("csvfile")
    file=pd.read_csv(file2)
    file["total"]=file["Maths"]+file["Science"]+file["English"]
    file["avarage"]=(file["total"]/300)*100
    def gradee(avarage):
        if avarage >=90:
            return "A"
        elif avarage >=80:
            return "B"
        else :
            return "fail"

    file["grade"]=file["avarage"].apply(gradee)
    


    return file.to_html()





if __name__==("__main__"):
    app.run(debug=True)