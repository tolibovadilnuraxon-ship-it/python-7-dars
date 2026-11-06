with open("sonlar.txt", "r") as f:
    qatorlar = f.readlines()


with open("juft_sonlar.txt", "w") as f:
    for qator in qatorlar:
        son = int(qator)
        if son % 2 == 0:
            f.write(f"{son} \n")
