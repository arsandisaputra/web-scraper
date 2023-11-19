import requests
import json
from bs4 import BeautifulSoup
import string
import os

url_web = "https://www.kamusbatak.com/indonesia/"

scraped = set()
batak = []
batak_indo = {}
init_word = "abara"
file_kalimat = "batak_indo.txt"
file_kata = "batak.txt"
file_kata_indo = "indo.txt"

def scrape(word):
    if word not in scraped:
        print("Scraping kata", word, ". . .")
        URL = url_web + word + ".html"
        response = requests.get(URL)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        contents = soup.find_all('div', class_='panel panel-default')
        scraped.add(word)
        simpanbaris(file_kata, word)

        return contents
    else:
        print("Kata", word, "sudah pernah di-scrape.")
        return []


def bongkar(word, contents = []):
    # print(contents)
    if len(contents) > 0:
        if "404" in contents[0].text:
            print("Kata", word, "tidak diindex!")
        else:
            for i, c in enumerate(contents):
                if i == 0:
                    temp = c.text.replace("(Bahasa Indonesia) -", "")
                    temp = temp.replace("\n", "")
                    temp = temp.replace("\t", "")
                    temp = temp.replace("\xa0", "")
                    temp = temp.lower()
                    # batak_indo[word] = temp.strip().split("/")[0]
                    indo = temp.strip().split("/")[0]
                    baris = word+ "~"+ indo
                    simpanbaris(file_kalimat, baris)
                    simpanbaris(file_kata_indo, indo)
                else:
                    temp = c.text.replace("Contoh Kalimat:", "")
                    temp = temp.strip()
                    temp = temp.lower()
                    for btk_indo in temp.split("\n"):
                        text = btk_indo.split("=")
                        # batak_indo[text[0]] = text[1]
                        indo = text[1].strip()
                        baris = text[0].strip()+ "~"+ indo
                        simpanbaris(file_kalimat, baris)
                        simpanbaris(file_kata_indo, indo)
                        for btk in text[0].split():
                            contents = scrape(btk)
                            bongkar(btk, contents)


def simpanbaris(file, baris):
    with open(file, 'a') as file:
        baris = baris + "\n"
        file.write(baris)


if __name__ == "__main__":
    contents = scrape(init_word)
    bongkar(init_word, contents)
    print("Selesai.")


