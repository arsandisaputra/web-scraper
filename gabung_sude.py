from general import load_data, simpandata, filesInFolder, parse_int_from_string, load1_100_indo

fix_batak_indo_clear_v2 = "kamusbatak/fix_batak_indo_clear_v2.txt"
fix_batak_clear_v2 = "kamusbatak/fix_batak_clear_v2.txt"
fix_indo_clear_v2 = "kamusbatak/fix_indo_clear_v2.txt"
kata_indo_batak = "kamusbatak/kata_indo_batak.txt"
kata_batak_indo = "kamusbatak/kata_batak_indo.txt"
fix_kata_indo_batak = "kamusbatak/fix_kata_indo_batak.txt"

flag = "angkuh~teal"
set_batak_indo = set()
list_batak = []
list_indo = []

if __name__ == "__main__":

    # batak_indo = load_data(kata_batak_indo)
    # total = 0
    # terbuang = 0
    # for line in batak_indo:
    #     batak, indo = line.split('~')

    #     len_batak = len(batak.split())
    #     len_indo = len(indo.split())

    #     if len_indo - 1 <= len_batak:
    #         batak = ' '.join(batak.split())
    #         indo = ' '.join(indo.split())
    #         bersih = batak + '~' + indo
    #         simpandata(fix_batak_indo_clear_v2, bersih)

    lines = load_data(fix_batak_indo_clear_v2)

    for line in lines:
        batak, indo = line.split('~')
        batak = ' '.join(batak.split())
        indo = ' '.join(indo.split())
        list_batak.append(batak)
        list_indo.append(indo)
        # bersih = batak + '~' + indo
        # set_batak_indo.add(bersih)

    simpandata(fix_batak_clear_v2, list_batak, 'w')
    simpandata(fix_indo_clear_v2, list_indo, 'w')

    # simpandata(fix_batak_indo_clear_v2, sorted(set_batak_indo), 'w')

    print("Selesai.")
