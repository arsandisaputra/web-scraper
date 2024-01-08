from general import load_data, simpandata, bersihkan_kata

btk_eng = "kamusbatak/fix_btk_eng_clear_v3.txt"
btk1kata = "kamusbatak/batak1kata.txt"
eng1kata = "kamusbatak/eng1kata.txt"
btk_engv4 = "kamusbatak/btk_eng_v4_byBtk.txt"

index_len_btk = {}
set_btk1 = set()
set_eng1 = set()
referenced = []
if __name__ == "__main__":

    lines = load_data(btk_engv4)
    sumber = set(load_data(eng1kata))

    btk_eng = [line.split('~') for line in lines]
    # for btk, eng in btk_eng:
    #     if len(btk.split()) == 1:
    #         for kata in eng.split():
    #             bersih = bersihkan_kata(kata)
    #             if len(bersih) > 0:
    #                 set_eng1.add(bersih)
    #     else:
    #         break

    # simpandata(eng1kata, sorted(set_eng1), 'w')

    for btk, eng in btk_eng:
        pecah = eng.split()
        bersumber = True
        for kata in pecah:
            if bersihkan_kata(kata) not in sumber:
                bersumber = False
                break

        if bersumber:
            gabung = btk + '~' + eng
            simpandata("kamusbatak/btk_eng_v4_byEng.txt", gabung)

    print("Selesai.")
