from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/productform")
def productform():
    return render_template("studentform.html")


@app.route("/product", methods=["POST"])
def product():
    name = request.form.get("name")
    price = float(request.form.get("price"))
    category = request.form.get("category")

    if price <= 0:
        return "Invalid price"

    return f"""
    Product: {name} <br>
    Price: {price} <br>
    Category: {category}
    """


if __name__ == "__main__":
    app.run(debug=True)