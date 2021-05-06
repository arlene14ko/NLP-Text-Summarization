# importing the necessary libraries
from transformers import pipeline
from bs4 import BeautifulSoup
import pandas as pd
from typing import Dict
import requests
import time


class Request:
    """
    Class Request contains all the functions for requesting 
    and summarizing the text
    """


    def summarize(text: str) -> str:
        """
        Function summarize will summarize the text 
        using the transformers pipeline summarizer
        It needs the text as a parameter
        :attrib summarizer contains the pipeline summarization
        :attrib summary will contain the parameters of summarizer
        It will then return the summary 
        """
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
        return summary


    def soup(url: str):
        """
        Function soup will scrape the website using BeautifulSoup
        It would need the url as a parameter
        :attrib r will contain the requests url
        :attrib soup will contain the scraped information
        This function returned the scrape information
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        time.sleep(3)
        return soup

    def book_summary(code: str) -> Dict[str,str]:
        """
        Function book_summary will summarize the book by chapter
        :parameter code will contain the code of the book
        :attrib link will contain the TXT link of the book
        :attrib results will contain the results of the scraped info
        :attrib chapters will contain the chapters of the book 
        :attrib book_summary will contain the summarized version of each chapter
        This function will return the book_summary
        """
        link = f'https://www.gutenberg.org/cache/epub/{code}/pg{code}.txt'
        print(f"Txt file of the book link: {link}")
        soup = Request.soup(link)
        results = str(soup)
        res = results.split("End of Project Gutenberg")[0]
        chapters = res.split("Chapter ")[1:]
        print(f"Chapters: {len(chapters)}")
        book_summ = []
        for i in chapters:
            book_summ.append(Request.chunks(i))

        book_summary = {}   
        for i in range(len(book_summ)):
            book_summary[f'Chapter {i+1}'] = book_summ[i]
        return book_summary


    def clean(name: str) -> str:
        """
        Function clean will remove the unnecessary characters from the name
        :parameter name is needed for this function
        :attrib clean_name contains the cleaned name version
        This function returns the cleaned name 
        """
        if str(name) == "[]":
            return "None"
        else: 
            str_name = str(name)
            clean_n = str_name.split(">")[1]
            clean_name = clean_n.split("<")[0]
            return clean_name


    def search(book: str):
        """
        Function search will search all the books depending on the user input
        :parameter book will contain the user input on the search tab
        :attrib url will contain the url of the search query
        :attrib results will contain the results of the search
        :attrib df will contain the converted results to a dataframe
        This function will return the dataframe

        """
        url = "https://www.gutenberg.org/ebooks/search/?query=" + str(book)
        print(f"Search book name: {url}")
        soup = Request.soup(url)
        results = []
        for match in soup.find_all('li', class_='booklink'):
            ebook = match.a.get('href')
            title = match("span", {"class":"title"})
            author = match("span", {"class":"subtitle"})
            dl = match("span", {"class":"extra"})
            link = "https://www.gutenberg.org" + str(ebook) 
            res = [title, author, link, dl]
            results.append(res)

        df = pd.DataFrame(results, columns =['Title', 'Author', 'Link', 'Downloads'])
        df['Title'] = df['Title'].apply(Request.clean)
        df['Author'] = df['Author'].apply(Request.clean)
        df['Downloads'] = df['Downloads'].apply(Request.clean)
        df['Summarize'] = df['Link'].apply(lambda x: x.split("/")[-1])
        df.index = df.index + 1 
        return df


    def article(url: str) -> str:
        """
        Function article will scrape the information of the article link
        :parameter url contains the article link  given by the user input
        :attrib text will contain all the results from the scraped info
        :attrib text_results will contain all the results from text
        This function will return the text_results  
        """
        soup = Request.soup(url)
        results = soup.find_all(["h1", "p"])
        text = [result.text for result in results]
        text_results = " ".join(text)
        return text_results

    def chunks(article):
        """
        Function chunks will divide the article by chunks and then summarize it
        :parameter article contains the text you want to summarize
        :attrib max_chunk is the maximum chunks per sentence
        :attrib sentenses will contain the split article
        :attrib chunks will contain the chunks of the sentence
        :attrib res will contain the summarized chunks
        :attrib summary will contain the joined summary text in res
        This function returns the summary
        """
        max_chunk = 500
        article = article.replace(".", ".<eos>")
        article = article.replace("?", "?<eos>")
        article = article.replace("!", "!<eos>")

        sentences = article.split("<eos>")
        current_chunk = 0
        chunks = []
        for sentence in sentences:
            if len(chunks) == current_chunk + 1:
                if len(chunks[current_chunk]) + len(sentence.split(" ")) <= max_chunk:
                    chunks[current_chunk].extend(sentence.split(" "))
                else:
                    current_chunk += 1
                    chunks.append(sentence.split(" "))
            else:
                print(current_chunk)
                chunks.append(sentence.split(" "))

        for chunk_id in range(len(chunks)):
            chunks[chunk_id] = " ".join(chunks[chunk_id])

        res = Request.summarize(chunks)
        summary = " ".join([summ["summary_text"] for summ in res])
        return summary

    def save_file(summary):
        """
        Function save_file will save the summary to a txt file
        This will allow the user to save the summary as a txt file
        """
        with open("./static/summary.txt", "w") as file:
            file.write(summary)
        print("Successfully saved the summary!")
        