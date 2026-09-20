class Karakter:
    nama_game = "Street Fighter"
    jumlah_karakter = 0
    versi_game = "Street Fighter 6"

    def __init__(self, nama, archtype, health, tier):
        self.nama = nama
        self.archtype = archtype
        self.__health = health
        self.__tier = tier
        Karakter.jumlah_karakter += 1

    def tampilkan_info(self):
        print(f"Nama           : {self.nama}")
        print(f"Gaya Bermain   : {self.archtype}")
        print(f"Health         : {self.__health}")
        print(f"Tier           : {self.__tier}\n")

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, nilai):
        if nilai >= 0:
            self.__health = nilai
            print("Health berhasil diubah.")
        else:
            print(f"Health tidak boleh negatif! Perubahan Health {self.nama} dibatalkan.")

    @property
    def tier(self):
        return self.__tier

    @tier.setter
    def tier(self, nilai):
        if nilai in ["S", "A", "B", "C", "D"]:
            self.__tier = nilai
            print("Tier berhasil diubah.")
        else:
            print("Tier harus S, A, B, C, atau D!\n")

    @classmethod
    def tampilkan_jumlah_karakter(cls):
        print(f"Jumlah karakter : {cls.jumlah_karakter}")

    @staticmethod
    def validasi_nama(nama):
        if nama.strip() == "":
            return False
        return True


class TierList:
    jumlah_tier = 5
    tier_tertinggi = "S"

    def __init__(self, nama_tier, karakter):
        self.nama_tier = nama_tier
        self.karakter = karakter

    def tampilkan_tier(self):
        print(f"\nTier: {self.nama_tier}")
        if len(self.karakter) == 0:
            print("Karakter: -")
        else:
            for karakter in self.karakter:
                print(f"- {karakter.nama}")

    @classmethod
    def tampilkan_info_tier(cls):
        print("Info Tier")
        print(f"\nJumlah Tier     : {cls.jumlah_tier}")
        print(f"Tier Tertinggi  : {cls.tier_tertinggi}\n")


class Pertandingan:
    nama_game = "Street Fighter"
    jumlah_pertandingan = 0
    format_pertandingan = "1 vs 1"

    def __init__(self, karakter1, karakter2, pemenang):
        self.karakter1 = karakter1
        self.karakter2 = karakter2
        self.pemenang = pemenang
        Pertandingan.jumlah_pertandingan += 1

    def tampilkan_pertandingan(self):
        print(self.karakter1.nama, "VS", self.karakter2.nama)
        print(f"Pemenang : {self.pemenang}\n")

    @classmethod
    def tampilkan_jumlah_pertandingan(cls):
        print(f"Jumlah pertandingan : {cls.jumlah_pertandingan}\n")

print("==============================================")
print(" SISTEM MANAJEMEN TIER LIST STREET FIGHTER")
print("==============================================")

ryu = Karakter("Ryu", "Shoto", 1000, "S")
ken = Karakter("Ken", "Rushdown", 1000, "S")
akuma = Karakter("Akuma", "Shoto", 900, "S")

tier_s = TierList("S", [ryu, ken, akuma])
tier_a = TierList("A", [])
tier_b = TierList("B", [])
tier_c = TierList("C", [])
tier_d = TierList("D", [])

p1 = Pertandingan(ryu, ken, "Ryu")
p2 = Pertandingan(ryu, akuma, "Akuma")

print("\n=== KARAKTER ===") #instance Method
Karakter.tampilkan_jumlah_karakter() #Class Method
ryu.tampilkan_info()
ken.tampilkan_info()

print("\n=== Mengubah Health ===") #Setters

print(f"Health Ryu : {ryu.health}")
ryu.health = 900
print(f"Health Ryu : {ryu.health}\n")

print(f"Health Ken : {ken.health}")
ken.health = -100
print(f"Health Ken : {ken.health}\n")


print("\n=== CEK KARAKTER ===") #Static method
print(f"Apakah Ryu ada? {Karakter.validasi_nama("Ryu")}")
print(f"Apakah Chun-Li ada? {Karakter.validasi_nama("Chun-Li")}")

tier_s = TierList("S", [ryu, ken])
tier_a = TierList("A", [])
tier_b = TierList("B", [])
tier_c = TierList("C", [])
tier_d = TierList("D", [])

print("\n=== TIER LIST ===")
tier_s.tampilkan_tier()
tier_a.tampilkan_tier()
tier_b.tampilkan_tier()
tier_c.tampilkan_tier()
tier_d.tampilkan_tier()

TierList.tampilkan_info_tier()

p1.tampilkan_pertandingan()
p2.tampilkan_pertandingan()

Pertandingan.tampilkan_jumlah_pertandingan()