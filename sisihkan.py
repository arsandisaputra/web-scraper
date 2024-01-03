import os
import glob
import shutil
from general import load_data, simpandata

dir_contoh_kalimat = "kamusbatak/contoh_kalimat"
dir_fix_pas = "kamusbatak/fix_format_indo_batak"
dir_fix_terbalik = "kamusbatak/fix_format_terbalik"
dir_fix_campur = "kamusbatak/fix_format_campur"
if __name__ == "__main__":
    files = glob.glob(os.path.join(dir_contoh_kalimat, "*"))

    for file_path in sorted(files):
        with open(file_path, 'r') as file:
            print(f"File: {file_path}")
            print("-" * 50)
            file_content = file.read()
            print(f"{file_content}")
            print("-" * 50)
        status = input("Apakah SEMUA contoh kalimat sudah dalam format Indonesia-Batak? (y/n): ")
        if status == 'y':
            shutil.move(file_path, dir_fix_pas)
        elif status == 'n':
            terbalik = input("Apakah SEMUA contoh kalimat dalam format TERBALIK (Batak-Indonesia)? (y/n): ")
            if terbalik == 'y':
                shutil.move(file_path, dir_fix_terbalik)
            else:
                shutil.move(file_path, dir_fix_campur)
        else:
            shutil.move(file_path, dir_fix_campur)
        print("=" * 50)
        
    print("Selesai.")
    # bataks = load_data("D:\Codes\Python\Web Scraper\kamusbatak\kata_batak.txt")
    

