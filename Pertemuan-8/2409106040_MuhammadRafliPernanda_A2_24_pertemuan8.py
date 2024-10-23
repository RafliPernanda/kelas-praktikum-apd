# try:
#     angka = int(input("angka: "))
# except ValueError:
#     print("input tidak sesuai (wajib angka!)")
#     angka = int(input("angka: "))

# pilihan = int(input("pilihan: "))

# if pilihan == 1 :
#     print("menu 1")

# elif pilihan == 2 :
#     print("menu 2")

# else :
#     print("pilihan tidak ada")

# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError:
#     print("Input yang anda masukkan bukan angka")
# else:
#     print(f"Angka yang kamu input: {angka}")
# finally:
#     print("Program selesai")

# try:
#     nama = input("Hello, what's your name? ")
#     if len(nama) > 5:
#         raise ValueError("Nama tidak boleh lebih dari 5 karakter")
# except ValueError as e:
#     print(e)

# def menu():
#     print("""
# ====== Menu ======
#     1. Tambah
#     2. Exit
# ==================
#     """)

# def tambah():
#     try:
#         angka1 = int(input("angka 1: "))
#         angka2 = int(input("angka 2: "))

#         print(f"Hasil dari {angka1} + {angka2} adalah {angka1 + angka2}")
#     except ValueError:
#         print("input tidak sesuai")

# while True:
#     try:
#         menu()
#         pilih_menu = int(input("Pilih menu: ")) 
#         if pilih_menu == 1:
#             tambah()
#         elif pilih_menu == 2:
#             print("Terima kasih telah menggunakan program ini")
#             break
#         else:
#             print("pilihan tidak valid")
#             continue
#     except ValueError:
#         print("Pilihan tidak sesuai")

