from general import load_data, simpandata

fix_btk = "kamusbatak/fix_batak_clear_v2.txt"
fix_eng = "kamusbatak/fix_ing_clear_v2.txt"
fix_btk_eng = "kamusbatak/fix_btk_eng_clear_v2.txt"

if __name__ == "__main__":
    btk = load_data(fix_btk)
    eng = load_data(fix_eng)

    for btk, eng in zip(btk, eng):
        btk = ' '.join(btk.split())
        eng = ' '.join(eng.split())
        bersih = btk + '~' + eng
        simpandata(fix_btk_eng, bersih)

    print("Selesai.")