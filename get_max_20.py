from general import load_data


fix_batak_clear_v2 = "kamusbatak/fix_batak_clear_v2.txt"
fix_indo_clear_v2 = "kamusbatak/fix_indo_clear_v2.txt"

if __name__ == "__main__":
    # str_tes = "tetapi pendidikan yang efektif itu membutuhkan gabungan yang efektif juga dari g"
    # print(len(str_tes))
    bataks = load_data(fix_batak_clear_v2)
    indos = load_data(fix_indo_clear_v2)

    total80 = 0
    for i, (batak, indo) in enumerate(zip(bataks, indos)):
        if len(indo) == 80:
            total80 += 1
            print(f"{i}. {indo} ({len(indo)})")
    print(total80)
    # if len(batak) == 80 or len(indo) == 80:
    #     len_batak = len(batak.split())
    #     len_indo = len(indo.split())
    #     print(f"{i}. {batak} ({len(batak)}) <-> {indo} ({len(indo)})")

    # if i == 10:
    #     break
