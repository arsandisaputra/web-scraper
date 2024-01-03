import requests
from bs4 import BeautifulSoup
import os
import glob
import re
from general import load_data, simpandata

url_web = "https://www.kamusbatak.com/indonesia/"

scraped = set()
new_scraped = set()
list_baris = []
batak_indo = {}
folder = "kamusbatak"
sub_folder = "kamusbatak/contoh_kalimat"
dir_fix_pas = "kamusbatak/fix_format_indo_batak"
init_word = "abara"
file_batak_indo = "batak_indo.txt"
file_kata_batak = "kata_batak.txt"
file_indo_batak = "kamusbatak/indo_batak.txt"
kalimat_batak = "kalimat_batak.txt"
kalimat_indo = "kalimat_indo.txt"
kalimat_inggris= "kalimat_inggris.txt"
kata_indo = "kata_indo.txt"
kata_batak = "kamusbatak/batak.txt"
kata_batak_indo = "kamusbatak/kata_batak_indo.txt"


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
        simpandata(kata_indo, word)

    return contents


def bongkar(word, contents=[], scrape_contoh_kalimat=True):
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
                    
                    # indo = temp.strip().split("/")[0]
                    indos = temp.strip().split("/")
                    for indo in indos:
                        baris = word + "~" + indo
                        if baris not in list_baris:
                            # list_baris.append(baris)
                            # simpandata(file_batak_indo, baris)
                            # simpandata(kalimat_indo, indo)
                            simpandata(kata_batak_indo, baris)
                
                # if i > 0:
                #     temp = c.text.replace("Contoh Kalimat:", "")
                #     temp = temp.strip()
                #     temp = temp.lower()
                #     filename = word + ".txt";
                #     simpandata(filename, temp, 'w')

                #     for btk_indo in temp.split("\n"):
                #         text = btk_indo.split("=")
                #         batak = re.sub(r'[^a-zA-Z\s]', '', text[0])
                #         indo = text[1].strip()
                #         baris = batak.strip() + "~" + indo
                #         if baris not in list_baris:
                #             list_baris.append(baris)
                #             simpandata(file_batak_indo, baris)
                #             simpandata(kalimat_indo, indo)
                #             if scrape_contoh_kalimat:
                #                 for btk in batak.split():
                #                     contents = scrape(btk)
                #                     bongkar(btk, contents)


def bersihkan(kata):
    # Gunakan ekspresi reguler untuk menyaring hanya huruf alfabet
    kata_bersih = re.sub(r'[^a-zA-Z]', '', kata)
    return kata_bersih

if __name__ == "__main__": 
    mulai = False
    mulai_dari = "tampar"
    bataks = load_data(kata_batak)

    for batak in bataks:
        batak = bersihkan(batak)
        if len(batak) > 0:
            if batak == mulai_dari or mulai:
                contents = scrape(batak)
                bongkar(batak, contents)
                mulai = True
   
    print("Selesai.")
