import random

red_box = 20
blue_box = 20
green_box = 20

f = open("simulation.csv", "w")
f.write("Time,Red,Blue,Green\n")

i = 0
t = 1
# Set the end condition for the while loop
while i < 100:
  # Generate a new random number for each box
  blue_r = random.random()
  green_r = random.random()
  red_r = random.random()

  if (green_r > 0.4 and green_box<=0 ) or (red_box<=0 and red_r > 0.4 ):
    pass
  # This little if block keeps total number of balls at 60

  else:
    # assume that the ball is in BLUE box
    if 0.0 <= blue_r <= 0.2:
      print("Stay at the same box: BLUE")
    elif 0.2 < blue_r <= 0.6:
      print("move to the box: RED")
      red_box += 1
      blue_box -= 1
    elif 0.6 < blue_r < 1.0:
      print("move to the box: GREEN")
      green_box += 1
      blue_box -= 1

    # assume that the ball is in GREEN box
    if 0.0 <= green_r <= 0.4:
      print("Stay at the same box: GREEN")
    elif 0.4 < green_r <= 1:
      print("move to the box: BLUE")
      blue_box += 1
      green_box -= 1

    # assume that the ball is in RED box
    if 0.0 <= red_r <= 0.4:
      print("Stay at the same box: RED")
    elif 0.4 < red_r <= 1:
      print("move to the box: BLUE")
      blue_box += 1
      red_box -= 1

    # Write the current time and ball count to the file
    # Write the current time and ball count to the file
    f.write("{:<5}{:<5}{:<5}{:<5}\n".format(t, red_box, blue_box, green_box))

    t += 1
    i += 1
