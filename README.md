______________________________________________________________________________________________________________________________________________________
![logo](https://user-images.githubusercontent.com/60827480/117361647-990f5100-aeba-11eb-9a82-761620b04fa3.JPG)
______________________________________________________________________________________________________________________________________________________


- Developer Name: `Arlene Postrado`
- Level: `Junior Data Scientist`
- Duration: `2 weeks`
- Deadline : `07/04/21 9:00 AM`
- Team challenge: `Solo project`
- Type of challenge: `Learning`
- Promotion : `AI Theano 2`
- Team challenge: `Coding Bootcamp: Becode Artificial Intelligence (AI) Bootcamp`

## Mission Objectives

- Be able to use of tokenization, stemming and lemmatization for exploration of text-based datasets.
- Be able to explore state-of-the-art algorithms for text summarization.
- Be able to use of HuggingFace transformers.
- Be able to evaluate the performance of pre-trained models.
- Be able to do the development and deployment of the dashboard for text summarization.

____________________________________________________________________________________________________________________________________________

## About The Repository

This is a project about developing a Natural language processing model that is able to summarize a full book and get an overview of the main ideas expressed by the author, this can also be able to summarize a text, an article or any link given by the user input. 

The task is to develop an "AI-powered tool" that can be able to "read" the content of any given book and make a summarization of the text. Also, the tool has to be deployed online and connect it with the database where the books are stored. 

This project currently works with the public-domain books from [Project Gutenberg](https://www.gutenberg.org/) a collection of more than 60,000 e-books. The e-book is available in several formats such as HTML, UTF-8, but on this project, it uses the UTF-8 format.


**Sample Search bar tab where you search for a book and it will list all the search results, from there you can choose which one to summarize**

![image](https://user-images.githubusercontent.com/60827480/117363726-42574680-aebd-11eb-9ffb-af78de35da95.png)

**Sample Article summary of a news about a `Neuralink video which appears to show monkey controlling game paddle simply by thinking` from [The Guardian](https://www.theguardian.com/technology/2021/apr/09/elon-musk-neuralink-monkey-video-game). There is an option to `save the summary as a file` or to `play, pause or stop` the summary as there is a Text-to-Speech option on the webpage.**
![image](https://user-images.githubusercontent.com/60827480/117369064-ab8e8800-aec4-11eb-9720-72bde06a5417.png)

____________________________________________________________________________________________________________________________________________


## R E P O S I T O R Y

**README.md**
  - has all the necessary information regarding the project

**app.py**
  - Flask app containing all the functions for the program to run in flask

**request.py**
  - python program that contains all the function to get request the information about the book and to summarize the book
  - functions include but not limited to:
         - function that will request the url
         - function that will scrape the url
         - function that will summarize the book
         - function that will create the dataframe table
         - function to save the summary as a txt file

**Procfile**
  - Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
  - This Procfile is used to declare a variety of process types, including: the app's web server.

**requirements.txt**
  - is a txt file used for specifying what python packages are required to run this project

**templates folder**
  - this is where all the html templates are saved
  - this has 4 html files namely:

      1. **home.html**
          - home html file is the starting base of the website


      2. **layout.html**
          - this is where all the imports for the html is located
          - this is also where the NavBar and the Footer is saved so it will be shown on all pages


      3. **summarize.html**
          - this is where the summary option is located
          - it has a tab depending on the type file you want to summarize
                  - Search tab - allows the user to search for a book from the Project Gutenberg ebooks and then an option to summarize that book
                  - Upload tab - allows the user to upload a txt file to summarize
                  - Text tab - allows the user to input a text and then it will summarize that text
                  - Article tab - allows the user to input an article, news, or link and it will summarize that article
                  - Questions tab - allows the user to input a question and the content and it will answer it for you (This is still in Progress..)


      4. **summary.html**
          - this is the page where you will see the summary of the input, either a book, an upload, a text or a link
          - there is also an option to save the summary as a txt.file if you click on the **Save as File** button
          - there is also a Text-to-Speech option, where if you click on **Play** it will read the summary for you, other buttons are **Pause** and **Stop**


**static folder**
  - this is where the logo is saved
  - this is also where the **summary.txt** is saved, which gives the user the option to download the summary as a txt file
      
**demo folder**
  - you can find some txt files in this folder which are actually from news articles, this is only used to demonstrate how the **Upload tab** works 
______________________________________________________________________________________________________________________________________________________

## Libraries Used For This Project


**Hugging Face 🤗 Transformers**  https://huggingface.co/transformers/
  - Hugging Face is an NLP-focused startup with a large open-source community, in particular around the Transformers library. 
  - 🤗 Transformers is a python-based library that exposes an API to use many well-known transformer architectures, such as BERT, RoBERTa, GPT-2 or DistilBERT, that obtain state-of-the-art results on a variety of NLP tasks like text classification, information extraction, question answering, and text generation. 
  - Those architectures come pre-trained with several sets of weights. 
  - In this project, transformers pipeline is used to summarize the text


**Flask** https://flask.palletsprojects.com/en/1.1.x/
  - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries
  - In this project, flask is used to create the web dashboard application 



**Pandas** https://pypi.org/project/pandas/
  - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
  - In this project, pandas is used convert a list to create a dataframe 


**Requests** https://docs.python-requests.org/en/master/
  - Requests is an HTTP library, written in Python, for human beings.
  - In this project, requests is used to send an HTTP request


**BeautifulSoup** https://pypi.org/project/beautifulsoup4/
  - Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
  - In this project, Beautiful Soup is used to scrape the Project Gutenberg e-books and also to scrape article links that is provided by the users


**Time** https://docs.python.org/3/library/time.html
  - Time module handles time-related tasks.
  - In this project, time is used to calculate the total time the code runs.


**Typing** https://docs.python.org/3/library/typing.html
  - Typing defines a standard notation for Python function and variable type annotations.
  - In this project, typing is used to help document the code properly.

**Heroku** //www.heroku.com
  - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
  - In this project, Heroku is used to deploy the app but due to limited GB since we are only using the free version, it was returning an error that the slug size is too big.
  - As free users of Heroku, we are only allowed of up to 500MB slug size.
  - Everything is already in the repository, the Procfile and the requirements.txt, we just need a bigger slug size to deploy it
![image](https://user-images.githubusercontent.com/60827480/117362204-42564700-aebb-11eb-805d-442270ebe792.png)


______________________________________________________________________________________________________________________________________________________

## Clone / Fork This Repository
  - If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/fork button and follow the instructions.

## P E N D I N G . . .
  - The Question tab is still in progress.. If you have any suggestions, feel free to contact me. Thank you!

![Thank you](https://static.euronews.com/articles/320895/560x315_320895.jpg?1452514624)
### Thank you for reading. Have fun with the code! 🤗



