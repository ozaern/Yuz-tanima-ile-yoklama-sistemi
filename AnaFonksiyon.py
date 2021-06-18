# ana fonksiyon py dosyası bende hata verdi. format atmıştım pc ye virüsten dolayı;
# sorun sebepleri python programı ile kurulu kütüphanelerin uyumsuz olması,
# python33.dll dosyasının eksik olması
# veya benim pc ile alakalı. çünkü os kütüphanesi kullandım ana fonksiyonda!
# ---------------------------------------------------------------------------------
# TEŞEKKÜR EDERİM

import os
from yuzogrenmesistemi import ogrenme
from yuztanimasistemi import tanima
from yuztaramasistemi import tarama

def title_bar():
    os.system('cls')  # pencere

    print("\t**************************************************")
    print("\t***** yuz tanıma sistemi ile yoklama sistemi *****")
    print("\t**************************************************")

def mainMenu():
    title_bar()
    print(10 * "*", "MENUYE HOŞGELDİNİZ", 10 * "*")
    print("[1] Yüz Tarama")
    print("[2] Yüzleri Öğrenme")
    print("[3] Yüzleri Tanıma")
    print("[4] Çıkış")

    while True:
        try:
            choice = int(input("İşlem seç: "))

            if choice == 1:
                tarama()
                mainMenu()
                break
            elif choice == 2:
                ogrenme()
                mainMenu()
                break
            elif choice == 3:
                tanima()
                mainMenu()
                break
            elif choice == 4:
                print("Teşekkür ederim")
                break
            else:
                print("\n1-4 arasında seçim yapın!")
                mainMenu()
        except ValueError:
            print("1-4 arasında seçim yapın!\n Tekrar deneyin!")
    exit

# ---------------ana menuye dön ------------------
mainMenu()