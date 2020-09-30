import random

print("KTU ögrenci sistemine hoşgeldiniz")

print("giriş için kayıt yaptırınız")

Name = input("adınız:")
Surname = input("Soyadınız:")
Class = input("Sınıfınız:")
Number = random.randrange(10000)

print("\nSayın ",Name,Surname,"sistemimize hoşgeldiniz! numaranız ",Number, " dır.")

print("\nKaydınız başarıyla alınmıştır teşekkür ederiz..")

control = True
while control:
    login = int(input("lütfen giriş için numaranızı giriniz:"))

    if login == Number :
        print("girişiniz başarıyla gerçekleşti başarılar dileriz.")
        input("\nçıkmak için bir tuşa basınız.")
        control = False

    elif type(login) != int:
        print("lütfen kayıt esnasında size verilen numarayı giriniz!!")
    
    else:
        print("hatalı ögrenci numarası !! ")
        control = False
        input("çıkmak için bir tuşa basınız.")

