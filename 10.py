yigindi = 0

with open("xarajatlar.txt", "r") as f:
    data = f.readlines()
    
for qator in data:
    nom, narx = qator.split() 
    yigindi += int(narx)       
    
print(yigindi)
