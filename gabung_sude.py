from general import load_data, simpandata, filesInFolder, parse_int_from_string, load1_100_indo

fix_batak_indo_clear_v2 = "kamusbatak/fix_batak_indo_clear_v2.txt"
kata_indo_batak = "kamusbatak/kata_indo_batak.txt"
fix_kata_indo_batak = "kamusbatak/fix_kata_indo_batak.txt"

flag = "angkuh~teal"
set_batak_indo = set()

if __name__ == "__main__":
    lines = load_data(fix_batak_indo_clear_v2)

    for line in lines:
        batak, indo = line.split('~')
        batak = ' '.join(batak.split())
        indo = ' '.join(indo.split())
        bersih = batak + '~' + indo
        set_batak_indo.add(bersih)
    
    simpandata(fix_batak_indo_clear_v2, sorted(set_batak_indo), 'w')