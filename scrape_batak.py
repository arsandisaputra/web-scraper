import requests
import json
from bs4 import BeautifulSoup
import string
import os
import re

url_web = "https://www.kamusbatak.com/indonesia/"

scraped = set()
new_scraped = set()
list_baris = []
batak_indo = {}
folder = "kamusbatak"
init_word = "abara"
file_kalimat = "batak_indo.txt"
file_kata_batak = "batak.txt"
file_kata_indo = "indo.txt"


def scrape(word):
    contents = []
    print("Scraping kata", word, ". . .")

    if word not in new_scraped:
        URL = url_web + word + ".html"
        response = requests.get(URL)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        contents = soup.find_all('div', class_='panel panel-default')
        new_scraped.add(word)
        simpanbaris(file_kata_batak, word)
    
    return contents


def bongkar(word, contents=[]):
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
                    baris = word + "~" + indo
                    if baris not in list_baris:
                        list_baris.append(baris)
                        simpanbaris(file_kalimat, baris)
                        simpanbaris(file_kata_indo, indo)
                else:
                    temp = c.text.replace("Contoh Kalimat:", "")
                    temp = temp.strip()
                    temp = temp.lower()
                    for btk_indo in temp.split("\n"):
                        text = btk_indo.split("=")
                        batak = re.sub(r'[^a-zA-Z\s]', '', text[0])
                        indo = text[1].strip()
                        baris = batak.strip() + "~" + indo
                        if baris not in list_baris:
                            list_baris.append(baris)
                            simpanbaris(file_kalimat, baris)
                            simpanbaris(file_kata_indo, indo)
                            for btk in batak.split():
                                contents = scrape(btk)
                                bongkar(btk, contents)


def simpanbaris(file_name, baris):
    file_path = os.path.join(folder, file_name)
    with open(file_path, 'a', encoding='utf-8') as file:
        baris = baris + "\n"
        file.write(baris)

def load_data(filename):
    file_path = os.path.join(folder, filename)
    with open(file_path, 'r') as file:
        data_list = file.readlines()

    data_list = [line.strip() for line in data_list]
    return data_list

if __name__ == "__main__":    
    
    # list_baris = load_data(file_kalimat)
    # for l in list_baris:
    #     kata = l.split('~')
    #     if len(kata[0].split()) == 1:
    #         scraped.add(kata[0])
    #         simpanbaris(file_kata_batak, kata[0])
    
    # sorted_scraped = sorted(list(scraped))
    # for s in sorted_scraped:
    #     simpanbaris(file_kata_batak, s)
    #     print('---> ',s)
    #     contents = scrape(s) 
    #     bongkar(s, contents)
    
    print("Selesai.")
