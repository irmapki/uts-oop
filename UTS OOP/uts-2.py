class Mahasiswa:
    pass


mahasiswa1 = Mahasiswa()

mahasiswa1.nama = input("Masukkan Nama Mahasiswa: ")
mahasiswa1.nim = input("Masukkan NIM Mahasiswa: ")
mahasiswa1.programStudi = input("Masukkan Program Studi: ")


print("\nData Mahasiswa:")
print(f"Nama: {mahasiswa1.nama}")
print(f"NIM: {mahasiswa1.nim}")
print(f"Program Studi: {mahasiswa1.programStudi}")
