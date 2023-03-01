kalimat = str(input("Masukkan sebuah kalimat : "))

def katapanjang(kalimat):
    kata = kalimat.split()
    panjang = max(kata, key=len)
    return panjang

print(f"Kata terpanjang dalam kalimat tersebut adalah : {katapanjang(kalimat)}")