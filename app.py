from flask import Flask, render_template, request, redirect, send_file
import requests
from request import Request
import time


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
            and "book" not in request.form
            and "book_name" not in request.form
        ):
            return redirect(request.url)

        text = request.form.get("text")
        print(f"Text Input: {text}")
        article = request.form.get("article")
        print(f"Article Input: {article}")
        book = request.form.get("book")
        print(f"Book Input: {book}")
        file = request.files.get("file")
        print(f"File Input: {file}")
        book_name = request.form.get("book_name")
        print(f"Book Name Input: {book_name}")
        start = time.time()

        if text == "" and article == "" and file == "" and book == "" and book_name == "":
            return redirect(request.url)

        elif text:
            print("Elif text file")
            summary = Request.chunks(text)
            clean = ".".join(summ.split(" ."))
            Request.save_file(clean)
            end = time.time()
            print(f"Program runs for {end - start} seconds.")
            return render_template("summary.html", summary=clean)

        elif article:
            print("Elif article file")
            summary = Request.article(article)
            chunks = Request.chunks(summary)
            clean = ".".join(chunks.split(" ."))
            Request.save_file(clean)
            end = time.time()
            print(f"Program runs for {end - start} seconds.")
            return render_template("summary.html", summary=clean)

        elif file:
            print("Elif Upload file")
            txt_file = file.read()
            txt = txt_file.decode("utf-8")
            print(f" File Type: {type(txt_file)}")
            print(f" Txt Type: {type(txt_file)}")
            summary = Request.chunks(txt)
            summ = ".".join(summary.split(" ."))
            Request.save_file(summ)
            end = time.time()
            print(f"Program runs for {end - start} seconds.")
            return render_template("summary.html", summary=summ)

        elif book:
            print("Book name is here")
            df = Request.search(book)
            return render_template('summarize.html', column_names=df.columns.values, row_data=list(df.values.tolist()), 
                                    link_column="Link", summ_column = "Summarize", zip=zip)
        
        elif book_name:
            print("Name of the Book here.")
            Request.save_file(book_name)
            end = time.time()
            print(f"Program runs for {end - start} seconds.")
            return render_template("summary.html", summary=book_name)

        else:
            return render_template("summarize.html")


@app.route("/summary")
def save_file():
    file = "static/summary.txt"
    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

