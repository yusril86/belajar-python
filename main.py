# angka = 2 
print("=================================================")
print("Selamat datang di program kalkulator sederhana!")
print("=================================================")
print("Silakan pilih operasi yang ingin dilakukan:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
operasi = int(input("Pilih operasi matematika: "))

angka= int(input("Masukkan sebuah angka: "))
angka2 = int(input("Masukkan angka kedua: "))



# print("Angka yang dimasukkan adalah:", angka, "dan", angka2)
# print(f"ini adalah angka" + str(angka) + " dan " + str(angka2))


if operasi == 1:
    hasil = angka + angka2
    print("Hasil penjumlahan:", hasil)
elif operasi == 2:
    hasil = angka - angka2
    print("Hasil pengurangan:", hasil)
elif operasi == 3:
    hasil = angka * angka2
    print("Hasil perkalian:", hasil)
elif operasi == 4: 
        hasil = angka / angka2
        print("Hasil pembagian:", hasil) 
else:
    print("Operasi Matematika tidak valid. Silakan pilih 1, 2, 3, atau 4.")