print("========== BARIS ARITMATIKA ==========")
awall = int(input("Masukkan bilangan awal : "))
selisihh = int(input("Masukkan selisih bilangan : "))
sukuu = int(input("Masukkan banyaknya suku : "))


def aritmatika(awall, selisihh, sukuu):
    total = (sukuu/2)*(2*awall+(sukuu-1)*selisihh)
    return total


print (f"Total dari deret aritmatika tersebut adalah : {aritmatika(awall, selisihh, sukuu)}")