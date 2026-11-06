with open("ismlar.txt", "w") as f:
    soni = int(input("Nechta ism kiritmoqchisiz? "))
    
    for i in range(soni):
        ism = input(f"{i+1}-ismni kiriting: ")
        f.write(f"{ism} \n")
