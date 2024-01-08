import os
import glob
import re


def simpandata(file_path, data, writemode='a'):
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


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data_list = file.readlines()

    data_list = [line.strip() for line in data_list]
    return data_list


def filesInFolder(dir_path):
    files = glob.glob(os.path.join(dir_path, "*"))
    return sorted(files)


def parse_int_from_string(input_string):
    # Use a regular expression to find all integers in the string
    integers = re.findall(r'\b\d+\b', input_string)

    # Convert the found strings to integers
    # integers = [int(num) for num in integers]

    return integers


def load1_100_indo():
    sebutan1_100 = {}
    lines = load_data("angka_indo.txt")
    for line in lines:
        x, y = line.split('-')
        sebutan1_100[x] = y.lower()
    return sebutan1_100


def bersihkan_kata(kata):
    bersih = re.sub(r'[^a-zA-Z]', '', kata)
    return bersih
