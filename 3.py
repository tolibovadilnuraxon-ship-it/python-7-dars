with open("ismlar.txt", "r") as fayl:
    matn = fayl.read()
    print(f"Fayldagi ismlar: {matn}")


yangi_ism = input("Yangi ism: ")


with open("ismlar.txt", "a") as fayl:
    fayl.write(f"{yangi_ism}")

print("Yangi ism muvaffaqiyatli qo'shildi!")
