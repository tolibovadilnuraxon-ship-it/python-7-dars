with open("mahsulotlar.txt", "w") as fayl:
    print(" 5 ta mahsulot nomini kiriting:")
    
    for i in range(5):
        mahsulot = input(f"{i+1}-mahsulot: ")
        fayl.write(f"{mahsulot} \n")

print("\n--- Mahsulotlar muvaffaqiyatli saqlandi! ---\n")

with open("mahsulotlar.txt", "r") as fayl:
    matn = fayl.read()
    print("Fayldagi mahsulotlar ro'yxati:")
    print(matn)
