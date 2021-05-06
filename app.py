# importing the necessary libraries
from flask import Flask, render_template, request, redirect, send_file 
import requests
from request import Request
import time


app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    """
    Function that will render the home.html.
    This is also the home page of the Flask App.
    """
    return render_template("home.html")


@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    """
    Function that has both GET and POST method.
    This is the function where it will ask the user input and 
    then summarize that input and return it back to the html file
    """
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

        
        """
        :attrib text will contain the text input from the html
        :attrib article will contain the article link input from the html
        :attrib book will contain the search book input from the html
        :attrib file will contain the uploaded file input from the html
        :attrib book_name will contain the chosen book to summarize
        :attrib start will contain the start time on when the program started
        :attrib end will contain the end time on when the program ended
        """
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
            clean = ".".join(summary.split(" ."))
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
            print(f"Searching for Book name: {book}")
            df = Request.search(book)
            return render_template('summarize.html', column_names=df.columns.values, row_data=list(df.values.tolist()), 
                                    link_column="Link", summ_column = "Summarize", zip=zip, search_book=book)
        
        elif book_name:
            print(f"Summarize the book link: {book_name}")
            chapter_summary = Request.book_summary(book_name)
            # summarize the entire book
            Request.save_file(chapter_summary)
            end = time.time()
            print(f"Program runs for {end - start} seconds.")
            return render_template("summary.html", book_summary=chapter_summary)

        else:
            return render_template("summarize.html")


@app.route("/summary")
def save_file():
    """
    Function that can be able to save the txt file summary
    using the send_file()
    """
    file = "static/summary.txt"
    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

