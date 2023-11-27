import requests
from bs4 import BeautifulSoup
import os
import re

url_web = "https://www.kamusbatak.com/indonesia/"

scraped = set()
new_scraped = set()
list_baris = []
batak_indo = {}
folder = "kamusbatak"
init_word = "abara"
file_batak_indo = "batak_indo.txt"
file_kata_batak = "kata_batak.txt"
kalimat_batak = "kalimat_batak.txt"
kalimat_indo = "kalimat_indo.txt"
kalimat_inggris= "kalimat_inggris.txt"



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
        simpandata(file_kata_batak, word)

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
                            list_baris.append(baris)
                            simpandata(file_batak_indo, baris)
                            simpandata(kalimat_indo, indo)
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
                            simpandata(file_batak_indo, baris)
                            simpandata(kalimat_indo, indo)
                            if scrape_contoh_kalimat:
                                for btk in batak.split():
                                    contents = scrape(btk)
                                    bongkar(btk, contents)

def simpandata(file_name, data, writemode='a'):
    file_path = os.path.join(folder, file_name)

    with open(file_path, writemode, encoding='utf-8') as file:
        if isinstance(data, dict):
            for key, val in data.items():
                if isinstance(val, list):
                    for v in val:
                        baris = key + "~" + v + "\n"
                        file.write(baris)
                else:
                    if isinstance(key, int):
                        baris = str(key+1) + "~" + val + "\n"
                    else:
                        baris = key + "~" + val + "\n"
                    file.write(baris)
        elif isinstance(data, (set, list)):
            for d in data:
                baris = d + "\n"
                file.write(baris)
        elif isinstance(data, str):
            baris = data + "\n"
            file.write(baris)


def load_data(filename):
    file_path = os.path.join(folder, filename)
    with open(file_path, 'r') as file:
        data_list = file.readlines()

    data_list = [line.strip() for line in data_list]
    return data_list

def terindikasi(kb, ki, be, ie):
    be_in_btk = 0
    ki_in_ind = 0

    kb = kb.lower()
    kbs = kb.split()
    for x in be.split():
        if x.lower() in kbs:
            be_in_btk += 1
    
    ki = ki.lower()
    kis = ki.split()
    for y in ie.split():
        if y.lower() in kis:
            ki_in_ind += 1
    
    if ki_in_ind/len(kis) >= be_in_btk/len(kbs):
        return True
    return False



if __name__ == "__main__":
    
    batak_indo = load_data(file_batak_indo)
    kalimat = [x.split('~') for x in batak_indo]
    kalimat_batak = [x[0] for x in kalimat]
    kalimat_indo = [x[1] for x in kalimat]

    batak_english = load_data("batak_english.txt")
    indo_english = load_data("indo_english.txt")

    for i, (btk, indo, be, ie) in enumerate(zip(kalimat_batak, kalimat_indo, batak_english, indo_english )):
        # print(i+1, btk, indo, be, ie)
        if terindikasi(btk, indo, be, ie):
            print(i+1, btk, indo)
        if i == 100:
            break
    # list_baris = load_data(file_batak_indo)
    # for bi in list_baris:
    #     kalimat = bi.split('~')
    #     batak = ' '.join(kalimat[0].split())
    #     indo = ' '.join(kalimat[1].split())
    #     simpandata(kalimat_batak, batak, 'a')
    #     simpandata(kalimat_indo, indo, 'a')
        # if kalimat[0] in batak_indo.keys():
        #     batak_indo[kalimat[0]].append(kalimat[1])
        # else:
        #     batak_indo[kalimat[0]] = [kalimat[1]]
    # batak_indo = dict(sorted(batak_indo.items()))
    # simpandata("sorted_batak_indo.txt", batak_indo, 'w')
    
    
    # indo = load_data(kalimat_indo)
    # eng = load_data("english.txt")
    # sama = {}
    # for i in range(len(indo)):
    #     if indo[i]==eng[i]:
    #         sama[i] = indo[i]
    #     else:
    #         indikasi = 0
    #         total_kata_ind = len(indo[i].split())
    #         for en in eng[i].split():
    #             if en in indo[i]:
    #                 indikasi+=1
    #         if indikasi == (total_kata_ind / 2):
    #             sama[i] = indo[i] + " (terindikasi)"

    #     i+=1
    # # print(set(sama.values()))
    # simpandata("sama.txt", sama, 'w')



    # scraped = sorted(set(load_data(file_kata_batak)))

    # simpandata(file_kata_batak, scraped, 'w')
    # list_baris = sorted(load_data(file_batak_indo))
    # print(list_baris[0:50])
    # for l in list_baris:
    #     kata = l.split('~')
    
    

    # batak_indo = dict(sorted(batak_indo.items()))


    
    # check = "tardok"
    # start = False
    # for btk in scraped:
    #     if btk == check:
    #         start = True
    #     if start:
    #         contents = scrape(btk)
    #         bongkar(btk, contents, False)

    print("Selesai.")
