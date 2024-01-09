from general import load_data, simpandata

# list_batak = []
# list_indo = []
fix_btk = "kamusbatak/fix_batak_clear_v2.txt"
fix_eng = "kamusbatak/fix_eng_clear_v2.txt"
fix_join = "kamusbatak/fix_btk_eng_clear_v3.txt"
dict_kl_btk = {}
dict_index_btk = {}
dict_temp = {}
list_semua = []

if __name__ == "__main__":
    btks = load_data(fix_btk)
    engs = load_data(fix_eng)

    for i, btk in enumerate(btks):
        dict_index_btk[i] = btk
        dict_kl_btk[i] = len(btk.split())

    sorted_kl_btk = dict(sorted(dict_kl_btk.items(), key=lambda item:item[1]))
    # print(sorted_kl_btk)

    jlh_kata = 1
    list_btk_eng = []

    for index, jlh in sorted_kl_btk.items():
        if jlh == jlh_kata:
            dict_temp[index] = dict_index_btk[index]
        else:
            sorted_dict_temp = dict(sorted(dict_temp.items(), key=lambda item:item[1]))
            for index, btk in sorted_dict_temp.items():
                gabung = btk + '~' + engs[index]
                list_semua.append(gabung)
            dict_temp = {}
            jlh_kata = jlh
            dict_temp[index] = dict_index_btk[index]
    
    simpandata(fix_join, list_semua, 'w')
    print("Selesai.")