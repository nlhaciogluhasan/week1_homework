print("***Beden Kitle İndeksi Hesaplama Programina Hosgeldiniz***")
kilo=float(input("Kilonuzu Giriniz : "))
boy=float(input("Boyunuzu Metre Cinsinden Giriniz : "))
bki=kilo/(boy*boy)
if bki<25:
    print("NORMAL")
elif 25<=bki<30:
    print("FAZLA KİLOLU")
elif 30<=bki<40:
    print("OBEZ")
elif bki>=40:
    print("AŞIRI ŞİŞMAN") 