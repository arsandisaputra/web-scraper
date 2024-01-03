import shutil
from general import load_data, simpandata, filesInFolder, parse_int_from_string, load1_100_indo

dir_indo_batak = "kamusbatak/fix_format_indo_batak"
dir_terbalik = "kamusbatak/fix_format_terbalik"
dir_merged = "kamusbatak/merged"
sebutan = load1_100_indo()

if __name__ == "__main__":
    print("Saatnya bersih-bersih data . . .")
    files = filesInFolder(dir_indo_batak)

    for file_path in files:
        lines = load_data(file_path)
        for i, line in enumerate(lines):
            indo, batak = line.split("=")
            getIntIndo = parse_int_from_string(indo)
            getIntBatak = parse_int_from_string(batak)

            if getIntIndo:
                print("-" * 50)
                print(f"Di dalam file: {file_path} baris ke {i+1}")
                print(line)
                print(getIntIndo, ' <-> ', getIntBatak)

                ubah = 'n'
                if len(getIntBatak) > 0:
                    ubah = input("Ubah? (y/n): ")

                if ubah == 'y' or len(getIntBatak) == 0:
                    if getIntIndo:
                        for angka in getIntIndo:
                            if angka in sebutan:
                                ganti = sebutan[angka]
                            else:
                                dialog = "Masukkan text pengganti " + angka + " : "
                                ganti = input(dialog)
                                sebutan[angka] = ganti
                            indo = indo.replace(angka, ganti, 1)

                    # if getIntBatak:
                    #     for angka in getIntBatak:
                    #         dialog = "Masukkan text pengganti "+ angka+ " : "
                    #         ganti = input(dialog)
                    #         batak = batak.replace(angka, ganti)

            gabung = batak.strip() + '~' + indo.strip()
            simpandata('kamusbatak/fix_batak_indo.txt', gabung)
        shutil.move(file_path, dir_merged)

    print("Selesai.")
