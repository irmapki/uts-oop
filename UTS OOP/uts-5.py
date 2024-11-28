# Superclass (Kelas Induk)
class Hewan:
    def suara(self):
        return "Hewan mengeluarkan suara"

# Subclass (Kucing)
class Kucing(Hewan):
    def suara(self):  # Method overriding
        return "Meow"

# Subclass (Anjing)
class Anjing(Hewan):
    def suara(self):  # Method overriding
        return "Woof"

# Membuat objek dari masing-masing kelas
hewan1 = Hewan()
kucing1 = Kucing()
anjing1 = Anjing()

# Memanggil metode suara() pada setiap objek
print("Suara Hewan:", hewan1.suara())  # Output: Hewan mengeluarkan suara
print("Suara Kucing:", kucing1.suara())  # Output: Meow
print("Suara Anjing:", anjing1.suara())  # Output: Woof
