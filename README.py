 # post test nim genap

# opening/judul
print(52*"=")
print("menghitung nilai konversi satuan massa kilogram (kg)") 
print(52*"=",)

# masukan login sederhana berupa nama, nim dan prodi
nama = input("masukan nama: ")
nim = input("masukan nim: ")
prodi = input ("masukan prodi: ")
print(62*"_")

# penjelasan dan perintah untuk input angka yang akan di eksekusi oleh program yang sudah dibuat dengan satuan yang diinginkan
print("hari ini kita akan melaksanakan operasi konversi satuan massa.")
print("-")
print("silahkan masukan massa!")

print("\n")

# konversi satuan massa
# masukan angka (kg)

angka_1 = float(input("masukan angka (kg) = "))
operator = input ("satuan (pound,ounce,g) : ")

#percabangan dari program yang kita kerjakan

if operator == "pound":
    hasil = angka_1 * 2.20462
    print(f"hasilnya adalah {hasil} lb")
elif operator == "ounce":
    hasil = angka_1 * 35.274
    print(f"hasilnya adalah {hasil} ons")
elif operator == "g":
    hasil = angka_1 * 1000
    print(f"hasilnya adalah {hasil} g")

# selesai.
