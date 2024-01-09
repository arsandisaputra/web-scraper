from general import load_data, simpandata, bersihkan_kata
import random

btk_eng = "kamusbatak/fix_btk_eng_clear_v3.txt"
btk1kata = "kamusbatak/batak1kata.txt"
eng1kata = "kamusbatak/eng1kata.txt"
# btk_engv4 = "kamusbatak/btk_eng_v4_byBtk.txt"
batak2dst = "kamusbatak/batak2katadst.txt"
btk_engv4 = "kamusbatak/btk_eng_v4.txt"
btk_engv5 = "kamusbatak/btk_eng_v6.txt"
btk_engv7 = "kamusbatak/btk_eng_v7.txt"

index_len_btk = {}
btk_count = {}
set_btk1 = set()
set_eng1 = set()
referenced = []
if __name__ == "__main__":

    lines = load_data(btk_engv7)
    lines = lines * 4
    random.shuffle(lines)
    simpandata(btk_engv5, lines, 'w')

    # # sumber = set(load_data(eng1kata))

    # lines = load_data(btk_engv4)
    # btk_eng = [line.split('~') for line in lines]
    # for btk, eng in btk_eng:
    #     if len(btk.split()) == 1:
    #         for kata in btk.split():
    #             bersih = bersihkan_kata(kata)
    #             if len(bersih) > 0:
    #                 set_eng1.add(bersih)
    #                 btk_count[bersih] = 0
    #     else:
    #         for kata in btk.split():
    #             bersih = bersihkan_kata(kata)
    #             if len(bersih) > 0:
    #                 btk_count[bersih]+=1
    
    # for btk, eng in btk_eng:
    #     if len(btk.split()) == 1:
    #         for kata in btk.split():
    #             bersih = bersihkan_kata(kata)
    #             if len(bersih)>0 and btk_count[bersih] > 20:
    #                 gabung = btk + '~' + eng
    #                 referenced.append(gabung)
    #     else:
    #         lewat = True
    #         for kata in btk.split():
    #             bersih = bersihkan_kata(kata)
    #             if btk_count[bersih] < 10:
    #                 lewat = False
    #                 break
    #         if lewat:
    #             gabung = btk + '~' + eng
    #             referenced.append(gabung)
    
    # simpandata(btk_engv7, referenced, 'w')



    

    # simpandata(eng1kata, sorted(set_eng1), 'w')

    # for btk, eng in btk_eng:
    #     pecah = eng.split()
    #     bersumber = True
    #     for kata in pecah:
    #         if bersihkan_kata(kata) not in sumber:
    #             bersumber = False
    #             break

    #     if bersumber:
    #         gabung = btk + '~' + eng
    #         simpandata("kamusbatak/btk_eng_v4_byEng.txt", gabung)

    print("Selesai.")
