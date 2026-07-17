from flask import Flask, render_template, request
import pandas as pd
from validation import checking, requered_colomn
from process import process_data
app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploaded", methods=["POST"])

def uploaded():
    data=request.files.get("csv")
    if checking(data):
        return "no data uploaded"

    
    try:
        data=pd.read_csv(data)
    except:
        return "invalid file"
    if requered_colomn(data) :
        return "invalid file uploaded"
    
    data=process_data(data)
    
    return data.to_html()

if __name__=="__main__":
    app.run(debug=True)