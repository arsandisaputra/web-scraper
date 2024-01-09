from general import load_data, bersihkan, simpandata

fix_indo = "kamusbatak/fix_indo_clear_v2.txt"
set_kata_indo = set()
set_jlh_1 = set()
dict_kata_jlh = {}


if __name__ == "__main__":
    indos = load_data(fix_indo)

    for line in indos:
        for kata in line.split():
            kata = bersihkan(kata)
            set_kata_indo.add(kata)
            if kata not in dict_kata_jlh:
                dict_kata_jlh[kata] = 1
            else:
                dict_kata_jlh[kata] += 1
    sorted_dict_kata_jlh = dict(sorted(dict_kata_jlh.items(), key=lambda item: item[1]))
    
    for key, value in sorted_dict_kata_jlh.items():
        if value == 1:
            set_jlh_1.add(key)
    
    simpandata("jumlah_1_indo.txt", sorted(set_jlh_1), 'w')
    print("Selesai")