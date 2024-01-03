import os
import glob
import shutil
from general import load_data, simpandata

dir_fix_campur = "kamusbatak/fix_format_campur"
dir_fix_pas = "kamusbatak/fix_format_indo_batak"

if __name__ == "__main__":
    files = glob.glob(os.path.join(dir_fix_campur, "*"))
    
    for file_path in sorted(files):
        print(f"File: {file_path}")
        print("-"*75)
        content = load_data(file_path)
        for i, line in enumerate(content):
            print(i+1, "-", line)
        print("-"*75)

        input_baris = input("Masukkan Index kalimat yang tidak berformat Indonesia-Batak: ")

        # Memisahkan angka menggunakan spasi sebagai delimiter
        indexes = [int(x) for x in input_baris.split()]
        for i in indexes:
            if 0 <= i <= len(content):
                salah = content[i-1].split("=")
                perbaiki = salah[1].strip() + " = " + salah[0].strip()
                content[i-1] = perbaiki
            else:
                print("Index di luar jumlah baris.")
        
        simpandata(file_path, content, 'w')
        shutil.move(file_path, dir_fix_pas)

    print("Selesai.")