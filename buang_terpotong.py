from general import load_data, simpandata

fix_batak = "kamusbatak/fix_batak_clear_v2.txt"
fix_indo = "kamusbatak/fix_indo_clear_v2.txt"

indo_80 = "kamusbatak/indo_80.txt"
batak_80 = "kamusbatak/batak_80.txt"

if __name__ == "__main__":
    batak = load_data(fix_batak)
    indo = load_data(fix_indo)

    list_batak = []
    list_indo = []

    for i, (batak, indo) in enumerate(zip(batak, indo)):
        print(i, batak, indo)
        if len(indo) == 80:
            simpandata(indo_80, indo)
            simpandata(batak_80, batak)
        else:
            list_batak.append(batak)
            list_indo.append(indo)
        
    simpandata(fix_batak, list_batak, 'w')
    simpandata(fix_indo, list_indo, 'w')
    print("Selesai.")