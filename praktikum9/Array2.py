# Deklarasi matrix pertama dan kedua 
matrix1 = []
matrix2 = []

# Meminta input untuk matrix pertama 
print("Masukkan elemen untuk matrix pertama (3x3):")
for i in range(3):
    baris = []
    for j in range (3):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matrix1.append(baris)
    
# Meminta input untuk matrix kedua
print("\nMasukkan elemen untuk matrix kedua (3x3):")
for i in range(3):
    baris = []
    for j in range (3):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matrix2.append(baris)
    
# Meminta input jenis operasi 
operasi = input("\nPilih operasi (penjumlahan/pengurangan/perkalian): ").lower()

# Melakukan operasi berdasarkan pilihan
hasil = []
if operasi == 'penjumlahan':
    for i in range(3):
        baris= []
        for j in range(3):
            baris.append(matrix1[i][j] + matrix2 [i][j])
        hasil.append(baris)
elif operasi == 'pengurangan':
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matrix1[i][j] - matrix2[i][j])
        hasil.append(baris)
elif operasi == 'perkalian':
    for i in range(3):
        baris = []
        for j in range(3):
            nilai = 0
            for k in range(3):
                nilai += matrix1[i][k] * matrix2[k][j]
            baris.append(nilai)
        hasil.append(baris)
else:
    print("operasi tidak valid.")
    
# Menampilkan hasil operasi 
if hasil:
    print(f"\nhasil {operasi} matrix:")
    for baris in hasil:
        print(baris)                                                                    