from flask import Flask, render_template, request

app=Flask(__name__)
# student form
@app.route("/")
def studentform():
    return render_template("studentform.html")
@app.route("/welcomepage",methods=["POST"])
def welcomepage():
    name=request.form.get("name")
    file2=request.files["resume"]
    file=file2.read().decode("utf-8").splitlines()
    row=len(file)
    return f"""
    name: {name}<br>
file name: {file2.filename}<br>
extention: {file2.filename.split(".")[-1]}<br>
content type: {row}"""

# feedback
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/feed-back")
def feeddback():
    return f""


if __name__ =="__main__":
    app.run(debug=True)