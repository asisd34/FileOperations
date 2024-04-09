# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:13:56 2024

@author: Dasis
"""

def dosya_olustur():
    dosya_adi = input("Dosya adını girin: ")
    icerik = input("Dosya içeriğini girin: ")

    with open(dosya_adi, "w") as dosya:
        dosya.write(icerik)

    print(f"{dosya_adi} adlı dosya oluşturuldu ve içeriği yazıldı.")


def dosya_oku():
    dosya_adi = input("Okunacak dosya adını girin: ")

    try:
        with open(dosya_adi, "r") as dosya:
            icerik = dosya.read()
            print(f"\n{dosya_adi} dosyasının içeriği:")
            print(icerik)
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")


def dosyaya_yaz():
    dosya_adi = input("Yazılacak dosya adını girin: ")
    icerik = input("Dosyaya yazılacak içeriği girin: ")

    with open(dosya_adi, "w") as dosya:
        dosya.write(icerik)

    print(f"{dosya_adi} dosyasına yeni içerik yazıldı.")


def dosyaya_ekle():
    dosya_adi = input("Eklenecek dosya adını girin: ")
    icerik = input("Dosyaya eklenecek içeriği girin: ")

    with open(dosya_adi, "a") as dosya:
        dosya.write(icerik)

    print(f"{dosya_adi} dosyasına yeni içerik eklendi.")


def main():
    print("1. Dosya Oluşturma")
    print("2. Dosya Okuma")
    print("3. Dosyaya Yazma")
    print("4. Dosyaya Ekleme")

    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")

    if secim == "1":
        dosya_olustur()
    elif secim == "2":
        dosya_oku()
    elif secim == "3":
        dosyaya_yaz()
    elif secim == "4":
        dosyaya_ekle()
    else:
        print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
