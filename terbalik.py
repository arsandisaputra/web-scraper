import os
import glob
import shutil
from general import load_data, simpandata

dir_terbalik = "kamusbatak/fix_format_terbalik"
dir_fix_pas = "kamusbatak/fix_format_indo_batak"

if __name__ == "__main__":
    files = glob.glob(os.path.join(dir_terbalik, "*"))
    
    for file_path in files:
        print(f"File: {file_path}")
        print("-"*75)
        with open(file_path, 'r') as file:
            file_content = file.read()
            print(f"{file_content}")
        print("-"*75)
        input_serah = input("Tekan Enter Aja.")
        print("="*75)
