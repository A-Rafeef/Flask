from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({ "status": "working"})

@app.route("/api/analyze", methods=["POST","GET"])
def analyze():
    data=request.get_json()
    student=data["students"]
    total=0
    for i in student:
        total=student["math"]+student["science"]+student["english"]
        avarage=total/3


    return jsonify({
        "total":total
    })

if __name__==("__main__"):
    app.run(debug=True)
