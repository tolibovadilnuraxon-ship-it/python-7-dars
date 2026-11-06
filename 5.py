count = 0
with open("matn.txt", "r") as fayl:
    for qatorlar in fayl:
       count+=1

print("Qatorlar soni:",count)
