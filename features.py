from transformers import pipeline
from bs4 import BeautifulSoup
import requests


class Request:
    def summarize(text):
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
        return summary

    def request(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all(["h1", "p"])
        text = [result.text for result in results]
        ARTICLE = " ".join(text)

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
