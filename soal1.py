def tambahAnggota(nama, anggota=[]):
    anggota.append(nama)
    return anggota
def kurangAnggota(nama, anggota=[]):
    anggota.remove(nama)
    return anggota
def tampilkanAnggota(anggota=[]):
    print(anggota)

print("="*42)
print("*"*13, "Justice League", "*"*13)
print("="*42)

b = ["brucewyne", "victorstone", "ciscoramon"]
n = str(input("Masukan username anda: "))
j = []
if n in b:
    while True:
        print("="*5,f"WELCOME {n}","="*5)
        print("1. Tambah Anggota Justice League")
        print("2. Hapus Anggota Justice League")
        print("3. Tampilkan Anggota Justice League")
        print("4. Exit")
        l = int(input("Masukan pilihan anda : "))
        if l == 1:
            j = input("Nama Anggota baru : ")
            tambahAnggota(j)
            print(f"data '{j}' berhasil ditambahkan")
        elif l == 2:
            if l not in anggota:
                print(f"data '{j}' tidak ditemukan")
            anggota.remove(j)
            print(f"'{j}' berhasil dihapus")
        elif l == 3:
            print(anggota)
        elif l == 4:
            print(f"see u next time MR. {n} ,GLHF")
            break
else:
    print("Access Denied")