import requests
from bs4 import BeautifulSoup
import os
import glob
import re
from general import load_data, simpandata

url_web = "https://www.kamusbatak.com/batak/"

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
                    temp = c.text.replace("(Bahasa Batak) -", "")
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
                            list_baris.append(baris)
                            # simpandata(file_batak_indo, baris)
                            # simpandata(kalimat_indo, indo)
                            simpandata(file_indo_batak, baris)
                
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
    mulai_dari = "terpijak"
    files = glob.glob(os.path.join(dir_fix_pas, "*"))

    for file_path in sorted(files):
        file_name, ext = os.path.splitext(os.path.basename(file_path))
        if file_name == mulai_dari or mulai:
            contents = scrape(file_name)
            bongkar(file_name, contents)
            mulai = True
        # break
        # break
    

    # indos = load_data(kata_indo)
    # for kata in indos:
    #     indo = bersihkan(kata)
    #     contents = scrape(indo)
    #     bongkar(indo, contents)
        # break
    # kalimat = [x.split('~') for x in batak_indo]
    # kalimat_batak = [x[0] for x in kalimat]
    # kalimat_indo = [x[1] for x in kalimat] 
   
    print("Selesai.")
