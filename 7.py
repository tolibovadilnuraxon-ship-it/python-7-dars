with open("matn.txt", "r") as f:
    sozlar = f.read().split()

eng_uzun = ""

for soz in sozlar:
    if len(soz) > len(eng_uzun):
        eng_uzun = soz

print("Eng uzun so'z:", eng_uzun)
