from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("students_practice.csv")
    df["total"]=df["Maths"]+df["Science"]+ df["English"]
    df["avarage"]=df["total"]/3
    df["percentage"] = (df["total"]/300)*100
    df["bones"]= df["total"]+5
    df["collage"]="wmo collage"

    total_students = df["Name"].count()
    highest_mark = df["total"].max()
    lowest_mark = df["total"].min()
    average_mark = df["total"].mean()
    df=df.to_html

    return render_template("index.html",df=df,total_students=total_students, highest_mark=highest_mark, lowest_mark=lowest_mark, average_mark=average_mark)

if __name__ == "__main__":
    app.run(debug=True)