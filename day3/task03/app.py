from flask import Flask, render_template, request
import csv
app=Flask(__name__)
# student form
@app.route("/")
def studentform():
    return render_template("index.html")
@app.route("/show",methods=["POST","GET"])
def show():
    file=request.files.get("csv")
    f= file.read().decode("utf-8").splitlines()
    return str(f)




if __name__ =="__main__":
    app.run(debug=True)