# import random
# rastgelesayi=(random.randint(1,100))
# cevap=int(input("Kaç hak istiyorsunuz?:"))
# hak=cevap
# baslangicpuani=100
# eksipuan=baslangicpuani/cevap
# kazanilanpuan=baslangicpuani
# while hak>0:
#     tahmin=int(input("Tahmin ettiğiniz sayı kaç?:"))
#     hak-=1
#     if tahmin<rastgelesayi:
#         kazanilanpuan-=eksipuan
#         if kazanilanpuan<0:
#              kazanilanpuan=0
#         print("Yukarı")
#     elif tahmin>rastgelesayi:
#         if kazanilanpuan<0:
#              kazanilanpuan=0
#         kazanilanpuan-=eksipuan
#         print("Aşağı")
#     elif tahmin==rastgelesayi:
#         print(f"Doğru bildiniz! Puanınız:{kazanilanpuan}")
#         break
# else:
#         print(f"Hakkınız bitti.Sayı {rastgelesayi} idi.Puanınız:{kazanilanpuan}")
#asıl
import random
sayi=random.randint(1,10)
can=int(input("Kaç hak istiyorsunuz?:"))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input("Tahmin:"))
    if sayi==tahmin:
        print(f"Tebrikler! {sayac}. defada bildiniz. Toplam puanınız:{100-(100/can)*(sayac-1)}")
        break
    elif sayi>tahmin:
        print("Yukarı")
    elif sayi<tahmin:
        print("Aşağı")
    else:
        print("Lütfen geçerli bir değer giriniz.")
    if hak==0:
        print(f"Hakkınız bitti. Rastgele üretilen sayı {sayi} idi.")

