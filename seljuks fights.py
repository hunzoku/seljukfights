import random

class Karakter:
    def __init__(self, isim, saldiri, savunma, millet, seviye=1):
        self.isim = isim
        self.saldiri = saldiri
        self.savunma = savunma
        self.millet = millet
        self.seviye = seviye
        self.ozel_yetenekler = {
            "Guc_Vurusu": 15,  # Özel yeteneklerin saldırı gücünü belirtin
            "Hizli_Saldiri": 8
        }

    def saldir(self, dusman):
        secim = input("Saldırı türü seçin: Normal (N), Güç Vuruşu (G) veya Hızlı Saldırı (H): ").upper()
        if secim == "N":
            hasar = self.saldiri
        elif secim == "G":
            hasar = self.guc_vurusu(dusman)
        elif secim == "H":
            hasar = self.hizli_saldiri(dusman)
        else:
            print("Geçersiz seçim, normal saldırı yapılıyor.")
            hasar = self.saldiri
        dusman.hasar_al(hasar)
        return hasar

    def guc_vurusu(self, dusman):
        hasar = self.ozel_yetenekler["Guc_Vurusu"]
        dusman.hasar_al(hasar)
        return hasar

    def hizli_saldiri(self, dusman):
        hasar = self.ozel_yetenekler["Hizli_Saldiri"]
        dusman.hasar_al(hasar)
        return hasar

    def hasar_al(self, saldiri_miktari):
        self.savunma -= saldiri_miktari
        if self.savunma <= 0:
            self.savunma = 0
            print(f"{self.isim} ({self.millet}) öldü!")

    def seviye_arttir(self):
        self.seviye += 1
        self.saldiri += 2
        self.savunma += 1


class Dusman:
    def __init__(self, isim, seviye, saldiri, savunma, esyalar=None, millet="Bilinmeyen"):
        self.isim = isim
        self.seviye = seviye
        self.saldiri = saldiri
        self.savunma = savunma
        self.millet = millet
        if esyalar is None:
            self.esyalar = self.rastgele_esyalar_olustur()
        else:
            self.esyalar = esyalar
        self.ozel_yetenekler = {
            "Guc_Vurusu": 15,  # Özel yeteneklerin saldırı gücünü belirtin
            "Hizli_Saldiri": 8
        }

    def hasar_al(self, saldiri_miktari):
        self.savunma -= saldiri_miktari
        if self.savunma <= 0:
            self.savunma = 0
            print(f"{self.isim} ({self.millet}) öldü!")

    def konus(self, oyuncu):
        sozler = [
            f"{self.isim} ({self.millet}): Senin gibi zayıf biriyle kolayca başa çıkabilirim!",
            f"{self.isim} ({self.millet}): Gücümü hafife alma! Sana göstereceğim!",
            f"{self.isim} ({self.millet}): Sana burada dersini vereceğim, hazır ol!"
        ]
        print(random.choice(sozler))

    def olum(self):
        tepkiler = [
            "Ah! Ben yenildim...",
            "Gücünü kabul ediyorum. Ama bir gün intikamımı alacağım!",
            "Sana saygı duyuyorum. Ama unutma, bu sadece başlangıç!",
            "Eğer beni öldürdüysen, diğerleriyle başa çıkmak zor olacak!"
        ]
        print(f"{self.isim} ({self.millet}): {random.choice(tepkiler)}")

    def rastgele_esyalar_olustur(self):
        esyalar = {
            "Kılıç": random.randint(1, 5) * self.seviye,
            "Kalkan": random.randint(1, 5) * self.seviye
        }
        return esyalar


class DusmanFactory:
    def dusman_olustur(self, seviye, saldiri, savunma, oyuncu_millet):
        # Düşman özelliklerini belirleyin, bu örnek için basitçe rastgele değerler seçelim
        dusman_isimleri = {
            "Türk": ["Hasan", "Mehmet", "Ahmet", "Ali", "Ayşe", "Fatma", "Emine", "Mustafa", "Osman", "Zeynep"],
            "Yunan": ["Yiannis", "Dimitri", "Nikos", "Costas", "Kostis", "Panagiotis", "Sokratis", "Stavros", "Yannis"],
            "Ermeni": ["Sarkis", "Krikor", "Garabed", "Hovhannes", "Bedros", "Dikran", "Tavit", "Vartan", "Aram", "Kevork"],
            "Arap": ["Ahmad", "Mahmoud", "Hassan", "Hussein", "Khalid", "Said", "Omar", "Ali", "Abdullah", "Nasser"]
        }
        dusman_milletleri = ["Türk", "Yunan", "Ermeni", "Arap"]
        secilen_millet = random.choice(dusman_milletleri)
        secilen_isim = random.choice(dusman_isimleri[secilen_millet])
        dusman_seviye = random.randint(max(1, seviye - 1), seviye + 1)
        dusman_saldiri = random.randint(1, dusman_seviye * 2)
        dusman_savunma = random.randint(1, dusman_seviye * 2)

        return Dusman(secilen_isim, dusman_seviye, dusman_saldiri, dusman_savunma, millet=secilen_millet)


# Oyuncudan isim ve millet al
oyuncu_isim = input("Karakteriniz için bir isim girin: ")
oyuncu_millet = input("Karakterinizin milletini seçin (Türk, Yunan, Ermeni, Arap): ")

# Oyuncu ve düşman oluşturma
oyuncu = Karakter(oyuncu_isim, 10, 5, oyuncu_millet)
dusman_factory = DusmanFactory()
dusman = dusman_factory.dusman_olustur(oyuncu.seviye, oyuncu.saldiri, oyuncu.savunma, oyuncu_millet)

# Dövüş mekanizması
while True:
    # Düşmanla dövüşmeden önce konuşma sahnesi
    dusman.konus(oyuncu)

    # Dövüş başlasın
    while dusman.savunma > 0 and oyuncu.savunma > 0:
        hasar = oyuncu.saldir(dusman)
        print(f"{oyuncu.isim} ({oyuncu.millet}) düşmana {hasar} hasar verdi!")
        if dusman.savunma > 0:
            hasar = dusman.saldir(oyuncu)
            print(f"{dusman.isim} ({dusman.millet}) oyuncuya {hasar} hasar verdi!")

    # Düşman yendiğinde elde edilen eşyaları göster
    if dusman.savunma <= 0:
        print(f"{dusman.isim} ({dusman.millet}) yenildi! Elde edilen eşyalar: {dusman.esyalar}")

        # Düşman öldüğünde tepki verme
        dusman.olum()

        # Oyuncunun seviyesini artır
        oyuncu.seviye_arttir()

    # Yeni düşman oluştur
    dusman = dusman_factory.dusman_olustur(oyuncu.seviye, oyuncu.saldiri, oyuncu.savunma, oyuncu_millet)

    devam_et = input("Devam etmek istiyor musunuz? (E/H): ")
    if devam_et.upper() != "E":
        break
