# program penghitung Rata-rata Nilai mahasiswa (versi dasar)

print("--- program perhitungan nilai mahasiswa ---")

# memasukkan jumlah mahasiswa
jumlah = int(input("masukkan jumlah mahasiswa : "))

# menyiapkan variabel untuk menampung total nilai
total = 0

# Perulangan untuk meminta input nilai satu per satu    
for i in range(1, jumlah + 1):
    print("masukkan nilai mahasiswa", i, ": ", end="")
    nilai = float(input())
    total = total + nilai 

# menghitung rata-rata
rata_rata = total / jumlah

# menampilkan hasil
print("rata rata :", rata_rata)
