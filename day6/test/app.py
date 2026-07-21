from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/health", methods=["GET"])
def health():

    return jsonify({
        "status": "working"
    })


@app.route("/api/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    students = data["students"]

    total_average = 0
    top_average = 0
    pass_count = 0

    for student in students:

        average = (
            student["math"] +
            student["science"] +
            student["english"]
        ) / 3

        total_average += average

        if average > top_average:
            top_average = average

        if average >= 40:
            pass_count += 1

    class_average = total_average / len(students)

    pass_percentage = (pass_count / len(students)) * 100

    return jsonify({

        "class_average": round(class_average, 2),

        "top_average": round(top_average, 2),

        "pass_percentage": round(pass_percentage, 2)

    })


if __name__ == "__main__":
    app.run(debug=True)