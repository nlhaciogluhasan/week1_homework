print("***************************************************")
print("***************************************************")
ad=input("Adinizi girin : ")
soyad=input("Soyadinizi girin : ")
numara=input("Numaranizi girin : ")
ders=["","","",""]
vize=["","","",""]
final=["","","",""]
ortalama=["","","",""]
for i in range(4):
    print((i+1),". Dersin Adini Giriniz :  ")
    ders[i]=input()    
    vize[i]=float(input("Bu dersin vizesini giriniz :"))
    while (vize[i]>100 or vize[i]<0):
        print("Gecersiz Not..")
        vize[i]=float(input("Gecerli Bir Not Giriniz: "))
    final[i]=float(input("Bu dersin finalini giriniz :"))
    while (final[i]>100 or final[i]<0):
        print("Gecersiz Not..")
        final[i]=float(input("Gecerli Bir Not Giriniz: "))
    ortalama[i]=vize[i]*0.4+final[i]*0.6
print("-------------------------------------------------") 
print("\nÖğrencinin  ;\nAdi: ",ad,"\nSoyadi: ",soyad,"\nNumarasi: ",numara,"\n")       
for i in range(4):
    #print(ders[i],"dersinin ortalamasi :",ortalama[i],"dir.")
    if(ortalama[i]>=50):
        print(ders[i],"Dersini Gectiniz. Tebrikler...")
    else :
        print(ders[i],"Dersinden Kaldıniz:(")