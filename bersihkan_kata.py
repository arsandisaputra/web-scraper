from general import load_data, simpandata, filesInFolder, parse_int_from_string, load1_100_indo

dict_btk_indo = {}
set_btk_indo_clear = set()
fix_batak_indo = "kamusbatak/fix_batak_indo.txt"
fix_batak_indo_clear = "kamusbatak/fix_batak_indo_clear.txt"
fix_batak_indo_clear_v2 = "kamusbatak/fix_batak_indo_clear_v2.txt"
flag = "daulat ma di ahu~setialah padaku"

if __name__ == "__main__":
    # str_cari = "bahasa batak"
    # lines = load_data(fix_batak_indo)
    # lanjut = False
    # for i, line in enumerate(lines):
    #     if line == flag or lanjut:
    #         lanjut = True
    #         batak, indo = line.split('~')

    #         if str_cari in indo and str_cari not in batak:
    #             print(line)
    #             while True:
    #                 dialog = "Hapus " + str_cari+" di baris ke " + str(i) + " ? (y/n): "
    #                 tanya = input(dialog)

    #                 if tanya == 'y':
    #                     indo = indo.replace(str_cari, '')
    #                     break
    #                 elif tanya == 'n':
    #                     break
    #         fix = batak + '~'+indo
    #         simpandata(fix_batak_indo_clear, fix)


    # Saatnya men-distinct kalimatnya
    batak_indo_clear = load_data(fix_batak_indo_clear)

    for line in batak_indo_clear:
        kalimat_bersih = ' '.join(line.split())
        set_btk_indo_clear.add(kalimat_bersih)
    simpandata(fix_batak_indo_clear_v2, sorted(set_btk_indo_clear), 'w')
    print("Selesai.")
