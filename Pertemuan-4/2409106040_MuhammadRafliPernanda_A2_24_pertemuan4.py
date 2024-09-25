# for j in range(2,12) :
#     print("halo")

# print("********************************")
# print("Menu Rumah Makan Informatika 24: ")
# print("********************************")
# simpan = ["Nasi Padang", "Soto Banjar", "Ayam Bakar", "Lele Goreng", "Sup Badak", "Siput Saos Padang"]
# for i in simpan:
#     print(i)


# print("Menu Rumah Makan Informatika 24: ")
# print("*********************************")
# simpan = ["Nasi Padang", "Soto Banjar", "Ayam Bakar", "Lele Goreng", "Sup Badak", "Siput Saos Padang"]
# for i, menu in enumerate(simpan,start=1):
#     print(f"{i}. {menu}")


# print("Menu Rumah Makan Informatika 24: ")
# print("*********************************")
# simpan = ["Nasi Padang", "Soto Banjar", "Ayam Bakar", "Lele Goreng", "Sup Badak", "Siput Saos Padang"]
# for i in range(len(simpan)):
#     print(f"{i+1}. {simpan[1]}")

# makanan = ["mie", "nasi goreng", "bakso"]
# minuman = ["es teh", "air putih", "es jeruk"]

# for i in makanan:
#     for j in minuman:
#         print(f"{i} & {j}")

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}")

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih Ingin Mengulang? ")
#     if ulang == "tidak" or ulang =="Tidak":
#     break

# print(f"Total Perulangan: {hitung}")


# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih Ingin Lanjut? ")
#     if ulang == "ya" or ulang =="Ya":
#         print
#     continue

# print(f"Total Perulangan: {hitung}")

# print("Daftar bilangan ganjil dari 1-10")
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# total = 0
# while True:
#     angka = int(input("Masukkan angka positif, jika ingin berhenti silahkan masukkan angka negatif: "))
#     if angka < 0:
#         break
#     total += angka

# print("jumlah total adalah", total)


# Meminta input dari pengguna untuk range maksimal
# range_maksimal = int(input("Masukkan range maksimal: "))

# Inisialisasi variabel untuk menyimpan jumlah bilangan prima
# hitung_prima = 0

# Loop untuk memeriksa setiap angka dari 1 hingga range_maksimal
# for angka in range(1, range_maksimal):
#     angka += 1
#     apakah_prima = True  # Anggap angka tersebut prima

    # Cek apakah angka memiliki pembagi selain 1 dan dirinya sendiri
    # for i in range(2, angka):
    #     if angka % i == 0:
    #         apakah_prima = False  # Jika ada pembagi, bukan bilangan prima
            # print(f"{angka} bukan prima")
            # break
    # Jika angka tersebut prima, tambahkan jumlah hitung_prima
    # if apakah_prima == True:
    #     print(f"{angka} prima")
    #     hitung_prima += 1

# output
# print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")
