# bounce.py
#
# Exercise 1.5

height = 100  # initial height in meters
bounce_factor = 0.6  # bounce factor (fraction of height after bounce)

for i in range(1, 11): 
    height *= bounce_factor  # calculate new height after bounce
    print(i, height)