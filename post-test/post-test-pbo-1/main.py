class Statistik:
    def __init__(self, power, speed):
        self.power = power
        self.speed = speed

    def tampilkan_stat(self):
        return f"Power: {self.power}/10 | Speed: {self.speed}/10"

class Pemain:
    def __init__(self, nama_pemain):
        self.nama_pemain = nama_pemain

    def pilih_karakter(self, karakter):
        print(f"Pemain [{self.nama_pemain}] telah memilih {karakter.nama} untuk bertarung!")

class Karakter:
    nama_game = "Street Fighter"
    jumlah_karakter = 0
    versi_game = "Street Fighter 6"

    def __init__(self, nama, archtype, health, tier, power, speed):
        self._nama = nama
        self._archtype = archtype
        self.__health = health
        self.__tier = tier
        self.statistik = Statistik(power, speed)
        Karakter.jumlah_karakter += 1

    @property
    def nama(self):
        return self._nama

    def tampilkan_info(self):
        print(f"Nama           : {self._nama}")
        print(f"Gaya Bermain   : {self._archtype}")
        print(f"Health         : {self.__health}")
        print(f"Tier           : {self.__tier}\n")
        print(f"Statistik      : {self.statistik.tampilkan_stat()}")

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

class Shoto(Karakter):
    def __init__(self, nama, health, tier, power, speed, tipe_proyektil):
        super().__init__(nama, "Shoto", health, tier, power, speed)
        
        self.tipe_proyektil = tipe_proyektil

    def tampilkan_info(self):
        print(">>> [Tipe: SHOTO] <<<")
        super().tampilkan_info()
        print(f"Proyektil {self._nama} : {self.tipe_proyektil}\n")

class Grappler(Karakter):
    def __init__(self, nama, health, tier, power, speed, daya_banting):
        super().__init__(nama, "Grappler", health, tier, power, speed)
        
        self.daya_banting = daya_banting

    def tampilkan_info(self):
        print(">>> [Tipe: GRAPPLER] <<<")
        super().tampilkan_info()
        print(f"Daya Banting {self._nama}: {self.daya_banting} DMG\n")

class TierList:
    jumlah_tier = 5
    tier_tertinggi = "S"

    def __init__(self, nama_tier, karakter_list):
        self.nama_tier = nama_tier
        self.karakter = karakter_list

    def tampilkan_tier(self):
        print(f"Tier: {self.nama_tier}")
        if len(self.karakter) == 0:
            print("Karakter: -")
        else:
            for k in self.karakter:
                print(f"- {k.nama}")
        print()

    @classmethod
    def tampilkan_info_tier(cls):
        print("--- Info Tier ---")
        print(f"Jumlah Tier    : {cls.jumlah_tier}")
        print(f"Tier Tertinggi : {cls.tier_tertinggi}\n")


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
        print(f"{self.karakter1.nama} VS {self.karakter2.nama}")
        nama_menang = self.pemenang.nama if hasattr(self.pemenang, 'nama') else self.pemenang
        print(f"Pemenang : {nama_menang}\n")

    @classmethod
    def tampilkan_jumlah_pertandingan(cls):
        print(f"Jumlah pertandingan : {cls.jumlah_pertandingan}\n")

if __name__ == "__main__":
    print("\n==============================================")
    print(" SISTEM MANAJEMEN TIER LIST STREET FIGHTER")
    print("==============================================\n")

    ryu = Shoto("Ryu", 1000, "S", power=8, speed=7, tipe_proyektil="Hadouken")
    ken = Shoto("Ken", 1000, "S", power=8, speed=8, tipe_proyektil="Shoryuken Api")
    zangief = Grappler("Zangief", 1100, "A", power=10, speed=3, daya_banting=3500)

    Karakter.tampilkan_jumlah_karakter()
    print()
    ryu.tampilkan_info()
    ken.tampilkan_info()
    zangief.tampilkan_info()

    print("=== MENGUBAH HEALTH ===")
    print(f"Health Ryu awal : {ryu.health}")
    ryu.health = 900
    print(f"Health Ryu baru : {ryu.health}\n")

    print(f"Health Ken awal : {ken.health}")
    ken.health = -100
    print(f"Health Ken baru : {ken.health}\n")

    player1 = Pemain("Tokido")
    player2 = Pemain("Daigo Umehara")
    player1.pilih_karakter(ryu)
    player2.pilih_karakter(zangief)
    print()

    print("=== RELASI AGREGASI (TIER LIST) ===")
    tier_s = TierList("S", [ryu, ken])
    tier_a = TierList("A", [zangief])
    tier_b = TierList("B", [])
    
    tier_s.tampilkan_tier()
    tier_a.tampilkan_tier()
    tier_b.tampilkan_tier()

    print("=== PERTANDINGAN ===")
    p1 = Pertandingan(ryu, ken, ryu)
    p2 = Pertandingan(ryu, zangief, zangief)

    p1.tampilkan_pertandingan()
    p2.tampilkan_pertandingan()
    Pertandingan.tampilkan_jumlah_pertandingan()