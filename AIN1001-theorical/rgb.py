import random

red_box = 20
blue_box = 20
green_box = 20

f = open("simulation.csv", "w")
f.write("Time,Red,Blue,Green\n")

for t in range(100):
    
    # assume that the ball is in BLUE box
    r = random.random()
    if 0.0 <= r <= 0.2:
        print("Stay at the same box: BLUE")
    elif 0.2 < r <= 0.6:
        print("move to the box: RED")
        red_box += 1
        blue_box -= 1
    elif 0.6 < r < 1.0:
        print("move to the box: GREEN")
        green_box += 1
        blue_box -= 1

    # assume that the ball is in GREEN box
    #r = random.random()
    if 0.0 <= r <= 0.4:
        print("Stay at the same box: GREEN")
        
    elif 0.4 < r <= 1:
        print("move to the box: BLUE")
        blue_box += 1
        green_box -= 1

    # assume that the ball is in RED box
    #r = random.random()
    if 0.0 <= r <= 0.4:
        print("Stay at the same box: RED")
        
    elif 0.4 < r <= 1:
        print("move to the box: BLUE")
        blue_box += 1
        red_box -= 1

    # Write the current time and ball count to the file
    f.write(str(t) + "," + str(red_box) + "," + str(blue_box) + "," + str(green_box) + "\n")

