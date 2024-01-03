from general import load_data, simpandata, filesInFolder, parse_int_from_string, load1_100_indo

dict_btk_indo = {}
fix_batak_indo = "kamusbatak/fix_batak_indo.txt"
fix_batak_indo_clear = "kamusbatak/fix_batak_indo_clear.txt"
flag = "hordit~bahasa batak getar"

if __name__ == "__main__":
    str_cari = "bahasa batak"
    lines = load_data(fix_batak_indo)
    lanjut = False
    for line in lines:
        if line == flag or lanjut:
            lanjut = True
            batak, indo = line.split('~')

            if str_cari in indo and str_cari not in batak:
                print(line)
                while True:
                    dialog = "Hapus " + str_cari+"? (y/n): "
                    tanya = input(dialog)

                    if tanya == 'y':
                        indo = indo.replace(str_cari, '')
                        break
                    elif tanya == 'n':
                        break
            fix = batak + '~'+indo
            simpandata(fix_batak_indo_clear, fix)
    # simpandata(fix_batak_indo_clear, dict_btk_indo, 'w')
    print("Selesai.")
