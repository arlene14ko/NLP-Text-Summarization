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
            and "link" not in request.form
            and "file" not in request.files
        ):
            return redirect(request.url)

        text = request.form.get("text")
        print(f"Text Input: {text}")
        link = request.form.get("link")
        print(f"Link Input: {link}")
        file = request.files["file"]
        print(f"File Input: {file}")

        if text == "" and link == "" and file == "":
            return redirect(request.url)

        elif text:
            summary = Request.summarize(text)
            summ = summary[0]["summary_text"]
            return render_template("summary.html", summary=summ)

        elif link:
            summary = Request.request(link)
            return render_template("summary.html", summary=summary)

        elif file:
            summary = Request.file_read(file)
            return render_template("summary.html", summary=summary)
        else:
            return render_template("summarize.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

