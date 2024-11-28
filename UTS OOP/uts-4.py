class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.nomor_rekening = nomor_rekening
        self.__saldo = saldo  # Atribut saldo dibuat privat untuk keamanan

    # Getter untuk saldo
    def get_saldo(self):
        return self.__saldo

    # Setter untuk saldo
    def set_saldo(self, saldo_baru):
        if saldo_baru >= 0:  # Validasi agar saldo tidak negatif
            self.__saldo = saldo_baru
        else:
            print("Saldo tidak bisa bernilai negatif!")

    # Metode untuk menambahkan saldo
    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Saldo bertambah sebesar {jumlah}. Saldo saat ini: {self.__saldo}")
        else:
            print("Jumlah yang ditambahkan harus lebih dari 0.")

    # Metode untuk menarik saldo
    def tarik_saldo(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Saldo sebesar {jumlah} telah ditarik. Saldo saat ini: {self.__saldo}")
        elif jumlah > self.__saldo:
            print("Saldo tidak mencukupi!")
        else:
            print("Jumlah yang ditarik harus lebih dari 0.")

# Membuat objek AkunBank
akun1 = AkunBank("1234567890", 500000)

# Menggunakan setter dan getter
print(f"Saldo awal: {akun1.get_saldo()}")  # Mengambil saldo
akun1.set_saldo(700000)  # Mengatur saldo baru
print(f"Saldo setelah set: {akun1.get_saldo()}")

# Menambah dan menarik saldo
akun1.tambah_saldo(300000)
akun1.tarik_saldo(200000)
