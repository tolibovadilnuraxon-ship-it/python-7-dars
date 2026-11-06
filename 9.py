count = 0
yigindi = 0

with open("baholar.txt", "r") as f:
    data = f.readlines()
    
max_ball = 0
min_ball = 99999  

for ball in data:
    ball = int(ball) 
    count += 1
    yigindi += ball
    
    if max_ball < ball:
        max_ball = ball
    if min_ball > ball:
        min_ball = ball
    
print("Eng katta ball: ", max_ball)    
print("Eng kichik ball: ", min_ball)
print("O'rtacha ball: ", yigindi / count)
