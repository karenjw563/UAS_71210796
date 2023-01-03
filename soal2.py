print("="*5,"Selamat datang di XXV","="*5)
n = int(input("Masukkan tanggal hari ini: "))

print("="*2,"Berikut genre film yang tersedia","="*2)
print("1. Horor")
print("2. Action")

l = int(input("Silahkan pilih mau nonton film genre apa : "))
if l == 1:
    print("1. The Devil's Light")
    print("2. Pengabdi Setan")
    j = int(input("Silahkan pilih mau nonton film apa : "))
    k = int(input("Mau memesan tiket sebanyak : "))
    awal = 25000*k
    if n % 2 == 0:
        diskon = awal*0.02
        print(f"Total yang harus dibayar adalah Rp. {awal-diskon}")
    else:
        print(f"Total yang harus dibayar adalah Rp. {awal}")
elif l == 2:
    print("1. Black Panther: Wakanda Forever")
    print("2. Avatar: The Way of Waater")
    j = int(input("Silahkan pilih mau nonton film apa : "))
    k = int(input("Mau memesan tiket sebanyak : "))
    awal = 25000*k
    if k > 4:
        diskon = awal*0.05
        print(f"Total yang harus dibayar adalah Rp. {awal-diskon}")
    else:
        print(f"Total yang harus dibayar adalah Rp. {awal}")
else:
    print("Pilihan yang anda pilih tidak tersedia di bioskop ini")