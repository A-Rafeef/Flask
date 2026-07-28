from flask import Flask, request

app=Flask(__name__)

@app.route("/api", methods=[""])
def api():
    data=request.get_json()

    return 



if __name__==("__main__"):
    app.run(debug=True)