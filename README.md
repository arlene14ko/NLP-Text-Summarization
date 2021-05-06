______________________________________________________________________________________________________________________________________________________
# NLP Text summarization

- Developer Name: `Arlene Postrado`
- Level: `Junior Data Scientist`
- Duration: `2 weeks`
- Deadline : `07/04/21 9:00 AM`
- Team challenge: `Solo project`
- Type of challenge: `Learning`
- Promotion : `AI Theano 2`
- Team challenge: `Coding Bootcamp: Becode Artificial Intelligence (AI) Bootcamp`

## Mission objectives

- Be able to use of tokenization, stemming and lemmatization for exploration of text-based datasets.
- Be able to explore state-of-the-art algorithms for text summarization.
- Be able to use of HuggingFace transformers.
- Be able to evaluate the performance of pre-trained models.
- Be able to do the development and deployment of the dashboard for text summarization.

____________________________________________________________________________________________________________________________________________

## About the Repository

This is a project about developing a Natural language processing model that is able to summarize a full book and get an overview of the main ideas expressed by the author, this can also be able to summarize a text, an article or any link given by the user input. 

The task is to develop an "AI-powered tool" that can be able to "read" the content of any given book and make a summarization of the text. Also, the tool has to be deployed online and connect it with the database where the books are stored. 

This project currently works with the public-domain books from [Project Gutenberg](https://www.gutenberg.org/) a collection of more than 60,000 e-books. The e-book is available in several formats such as HTML, UTF-8, but on this project, it uses the UTF-8 format.

![image](https://user-images.githubusercontent.com/60827480/117344278-7fafda00-aea5-11eb-8599-74f105ec198b.png)

____________________________________________________________________________________________________________________________________________


## Repository

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
  - python program that will get all the features of the sound files  - 
Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
This Procfile is used to declare a variety of process types, including: the app's web server.

**create_csv.py**
  - python program that will create a dataframe with all the file paths of the sound files

**Datasets folder**
  - this is where all the datasets are saved
  - this has 4 files namely:

      1. **fan_full_features.csv**
          - a csv file containing the all the features extracted for the sound files of fan machines


      2. **pump_full_features.csv**
          - a csv file containing the all the features extracted for the sound files of pump machines


      3. **slider_full_features.csv**
          - a csv file containing the all the features extracted for the sound files of slider machines


      4. **valve_full_features.csv**
          - a csv file containing the all the features extracted for the sound files of valve machines



**Models folder**
  - this is where all the models are saved
  - this has 4 files namely:


      1. **fan_model.sav**
          - the machine learning model created for Fan machines


      2. **pump_model.sav**
          - the machine learning model created for Pump machines


      3. **slider_model.sav**
          - the machine learning model created for Slider machines


      4. **valve_model.sav**
          - the machine learning model created for Valve machines


     
   
**Models Creation folder**
  - this is where all the jupyter notebooks to create the models are saved 
  - this has 4 files namely:


      1. **fan_features.ipynb**
          - the jupyter notebook to create the model for Fan machines


      2. **pump_features.ipynb**
          - the jupyter notebook to create the model for Pump machines


      3. **slider_features.ipynb**
          - the jupyter notebook to create the model for Slider machines


      4. **valve_features.ipyn**
          - the jupyter notebook to create the model for Valve machines
          

**Demo  folder**
  - this is where our demo are saved for our model 
______________________________________________________________________________________________________________________________________________________

## Libraries Used For This Project


**Librosa** https://librosa.org/doc/latest/index.html
  - Librosa is a python package for music and audio analysis. It provides the building blocks necessary to create music information retrieval systems.
  - In this project, librosa is used to extract the features of the sound files.


**Sci-kit Learn** https://scikit-learn.org/stable/
  - Sci-kit learn is a simple and efficient tools for predictive data analysis.
  - In this project, sci-kit learn is used to create the models.


**Pickle** https://docs.python.org/3/library/pickle.html
  - The pickle module implements binary protocols for serializing and de-serializing a Python object structure. 
  - In this project, pickle is used to save and read the models in a `sav` format.


**Pandas** https://pypi.org/project/pandas/
  - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
  - In this project, pandas is used to read the csv files as a dataframe.


**Numpy** https://numpy.org/
  - Numpy is the fundamental package for scientific computing with Python.
  - In this project, numpy is used to get the mean, min, max and std of an array in the features.


**OS** https://docs.python.org/3/library/os.html
  - This module provides a portable way of using operating system dependent functionality.
  - In this project, OS is used to get the list of directories in a file path.


**Time** https://docs.python.org/3/library/time.html
  - Time module handles time-related tasks.
  - In this project, time is used to calculate the total time the code runs.


**Typing** https://docs.python.org/3/library/typing.html
  - Typing defines a standard notation for Python function and variable type annotations.
  - In this project, typing is used to help document the code properly.

______________________________________________________________________________________________________________________________________________________

## Clone/Fork Repository
  - If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/fork button and follow the instructions.

## Pending...
  - The Question tab is still in progress.. If you have any suggestions, feel free to contact me. Thank you!

![Thank you](https://static.euronews.com/articles/320895/560x315_320895.jpg?1452514624)
### Thank you for reading. Have fun with the code!



