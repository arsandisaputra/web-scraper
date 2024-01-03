import requests
from bs4 import BeautifulSoup
import os
import re

folder = "kamusbatak"
file_batak_indo = "fix_batak_indo.txt"
indos = set()
btks = set()

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

if __name__ == "__main__":
    batak_indo = load_data(file_batak_indo)
    kalimat = [x.split('~') for x in batak_indo]
    kalimat_batak = [x[0] for x in kalimat]
    kalimat_indo = [x[1] for x in kalimat]

    # for kalimat in kalimat_indo:
    #     for kata in kalimat.split(' '):
    #         indos.add(kata)
    # simpandata('kata_indo.txt', indos, 'w')
    for kalimat in kalimat_batak:
        for kata in kalimat.split(' '):
            btks.add(kata)
    simpandata('kata_batak.txt', btks, 'w')
    
    
