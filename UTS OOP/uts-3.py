class Laptop:
    def __init__(self, merk, ram, processor):
        # Constructor untuk menginisialisasi atribut
        self.merk = merk
        self.ram = ram
        self.processor = processor
        print(f"Laptop {self.merk} dengan RAM {self.ram} GB dan processor {self.processor} telah dibuat.")
    
    def __del__(self):
        # Destructor untuk mencetak pesan saat objek dihancurkan
        print(f"Laptop {self.merk} sedang dihancurkan.")

# Membuat objek Laptop
laptop1 = Laptop("Dell", 8, "Intel i5")
laptop2 = Laptop("HP", 16, "AMD Ryzen 7")

# Menampilkan atribut
print(f"Merk: {laptop1.merk}, RAM: {laptop1.ram} GB, Processor: {laptop1.processor}")
print(f"Merk: {laptop2.merk}, RAM: {laptop2.ram} GB, Processor: {laptop2.processor}")

# Menghapus objek
del laptop1
del laptop2
