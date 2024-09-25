from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

# Başlık ve başlangıç ekranı
while True:
    system("cls||clear")
    print()
    print("          /`·.¸")
    print("         /¸...¸`:·")
    print("     ¸.·´  ¸   `·.¸.·´)")
    print("    : © ):´;      ¸  {")
    print("     `·.¸ `·  ¸.·´\\`·¸)")
    print("         `\\´´\\¸.·´")
    print()
    print()
    print()
    print("╭══• ೋ•✧๑♡๑✧•ೋ •══╮")
    print("   by @https://t.me/eakofrc")
    print("╰══• ೋ•✧๑♡๑✧•ೋ •══╯")
    print()
    servisler_sms = [attribute for attribute in dir(SendSms) if callable(getattr(SendSms, attribute)) and not attribute.startswith('__')]

    try:
        menu = input(" 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Hızlı)\n\n 3- Çıkış\n\n Seçim: ")
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print("Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print("Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): ", end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print("Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: ", end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print("Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print("Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue

        system("cls||clear")
        try:
            print("Mail adresi (sadece 'enter' tuşuna basın): ", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise ValueError
        except ValueError:
            system("cls||clear")
            print("Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(f"Kaç adet SMS göndermek istiyorsun {sonsuz}: ", end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print("Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print("Kaç saniye aralıkla göndermek istiyorsun: ", end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print("Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        if kere is None:
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in servisler_sms:
                    exec(f"sms.{attribute}()")
                    sleep(aralik)
        else:
            for i in tel_liste:
                sms = SendSms(i, mail)
                if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in servisler_sms:
                            if sms.adet == kere:
                                break
                            exec(f"sms.{attribute}()")
                            sleep(aralik)

        print("\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 3:
        system("cls||clear")
        print("Çıkış yapılıyor...")
        break

    elif menu == 2:
        system("cls||clear")
        print("Telefon numarasını başında '+90' olmadan yazınız: ", end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print("Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print("Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): ", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise ValueError
        except ValueError:
            system("cls||clear")
            print("Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [
                        executor.submit(getattr(send_sms, attribute)) for attribute in servisler_sms
                    ]
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)
