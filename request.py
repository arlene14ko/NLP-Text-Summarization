from transformers import pipeline
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time



class Request:
    def summarize(text):
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
        return summary

    def soup(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        time.sleep(3)
        return soup
    

    def clean(name):
        if str(name) == "[]":
            return "None"
        else: 
            n = str(name)
            a = n.split(">")[1]
            m = a.split("<")[0]
            return m


    def search(book):
        url = "https://www.gutenberg.org/ebooks/search/?query=" + str(book)
        soup = Request.soup(url)
        results = []
        for match in soup.find_all('li', class_='booklink'):
            link = match.a.get('href')
            title = match("span", {"class":"title"})
            author = match("span", {"class":"subtitle"})
            dl = match("span", {"class":"extra"})
            res = [title, author, link, dl]
            results.append(res)

        df = pd.DataFrame(results, columns =['Title', 'Author', 'Link', 'Downloads'])
        df['Link'] = df['Link'].apply(lambda x: "https://www.gutenberg.org" + x)
        df['Title'] = df['Title'].apply(Request.clean)
        df['Author'] = df['Author'].apply(Request.clean)
        df['Downloads'] = df['Downloads'].apply(Request.clean)
        df['Summarize'] = df['Link']
        df.index = df.index + 1 
        return df


    def article(url):
        soup = Request.soup(url)
        results = soup.find_all(["h1", "p"])
        text = [result.text for result in results]
        ARTICLE = " ".join(text)
        return ARTICLE

    def chunks(ARTICLE):
        max_chunk = 500
        ARTICLE = ARTICLE.replace(".", ".<eos>")
        ARTICLE = ARTICLE.replace("?", "?<eos>")
        ARTICLE = ARTICLE.replace("!", "!<eos>")

        sentences = ARTICLE.split("<eos>")
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
        with open("./static/summary.txt", "w") as file:
            file.write(summary)
        print("Successfully saved the summary!")
        