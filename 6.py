qidirilayotgan_ism = input("Ismni kiriting:")
with open("ismlar.txt", "r") as fayl:
    matn = fayl.read()
    
if qidirilayotgan_ism  in matn:
    print("Ism topildi!")
else:
    print("Ism topilmadi! ")
    
