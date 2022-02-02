import random
liste=["t","k","m"]
print("-------------------------------------------\nBilgisayarla Taş Kağıt Makas Oyununa Hosgeldiniz")
print("Bu Oyunda Bilgisayara Karşı Oynayacaksınız. 10 El Sonunda Kazanan Belli Olacak... ")
isim=input("İsminizi Girin : ")
print("********Taş seçmek için 't', kağıt seçmek için 'k',makas seçmek için 'm' yaziniz...********")
print("Oyun Başlıyor, Başarılar................")

ad_glp=0
pc_glp=0
tur=1
while tur<11:
    pc=random.choice(liste)
    ad=input("\nt,k yada m yaziniz. ")
    print(isim," : ",ad,"sectin.","Bilgisayar ",pc,"Seçmişti")
    if (ad=='t' and pc=='k'):
        pc_glp+=1 
        print(isim," : ",ad_glp," Bilgisayar: ",pc_glp)   
    elif (ad=='t' and pc=='m'):
        ad_glp+=1
        print(isim," : ",ad_glp," Bilgisayar: ",pc_glp)   
    elif(ad=='t' and pc=='t'):
        print(isim, " : ",ad_glp," Bilgisayar: ",pc_glp)  
    elif(ad=='k' and pc=='t'):
        ad_glp+=1
        print(isim," : ",ad_glp," Bilgisayar: ",pc_glp)
    elif (ad=='k' and pc== 'm'):
        pc_glp+=1
        print(isim," : ",ad_glp," Bilgisayar: ",pc_glp)
    elif (ad=='k' and pc=='k'):
        print(isim," : ",ad_glp," Bilgisayar: ",pc_glp)  
    elif (ad=='m' and pc=='t'):
        pc_glp+=1
        print(isim, " : ",ad_glp," Bilgisayar: ",pc_glp)
    elif (ad=='m' and pc=='k'):
        ad_glp+=1
        print(isim," : ",ad_glp," Bilgisayar: ",pc_glp)
    elif (ad=='m' and pc=='m'):
        print(isim, " : ",ad_glp," Bilgisayar: ",pc_glp)    
    tur+=1
print("\n***Son Durum***\n",isim," : ",ad_glp," Bilgisayar : ",pc_glp)    
if ad_glp>pc_glp:
    print(isim," Kazandın tebrikler...:)")
elif pc_glp>ad_glp:
    print("Bilgisayar kazandi...")    
else:
    print("Oyun berabere...")
    