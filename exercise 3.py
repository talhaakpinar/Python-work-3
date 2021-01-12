class Ogrenci:
    ogrenciAdı = input("Öğrenci Adını Giriniz: ")
    ogrenciSoyadı = input("Öğrenci Soyadını Giriniz: ")
    ogrenciSınıf = input("Öğrenci Sınıfını Giriniz: ")


class Soru:
    def NetSayısı(dogru_sayisi, yanlis_sayisi):
        return dogru_sayisi - (yanlis_sayisi / 4)
    def Hesapla(net_sayisi):
        return net_sayisi * 2


dogru_sayisi = int(input("Dogru Sayısı: "))
yanlis_sayisi = int(input("Yanlis Sayısı: "))
net_sayisi = Soru.NetSayısı(dogru_sayisi, yanlis_sayisi)
puan = Soru.Hesapla(net_sayisi)
print("Ogrenci : " + Ogrenci.ogrenciAdı + " " + Ogrenci.ogrenciSoyadı + "\nSinif : " + Ogrenci.ogrenciSınıf + "\nPuan : " + str(puan))
