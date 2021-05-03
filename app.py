from flask import Flask, render_template, request, redirect
import requests
from request import Request


app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    if request.method == "GET":
        return render_template("summarize.html")

    if request.method == "POST":

        if (
            "text" not in request.form
            and "article" not in request.form
            and "file" not in request.files
            and "book" not in request.files
        ):
            return redirect(request.url)

        text = request.form.get("text")
        print(f"Text Input: {text}")
        article = request.form.get("article")
        print(f"Link Input: {article}")
        file = request.files["file"]
        print(f"File Input: {file}")

        if text == "" and link == "" and file == "":
            return redirect(request.url)

        elif text:
            summary = Request.summarize(text)
            summ = summary[0]["summary_text"]
            clean = ".".join(summ.split(" ."))
            return render_template("summary.html", summary=clean)

        elif article:
            summary = Request.request(article)
            clean = ".".join(summary.split(" ."))
            return render_template("summary.html", summary=clean)

        elif file:
            txt_file = file.read()
            txt = txt_file.decode("utf-8")
            print(f" File Type: {type(txt_file)}")
            print(f" Txt Type: {type(txt_file)}")
            summary = Request.summarize(txt)
            summ = summary[0]["summary_text"]
            clean = ".".join(summ.split(" ."))
            return render_template("summary.html", summary=clean)

        else:
            return render_template("summarize.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

