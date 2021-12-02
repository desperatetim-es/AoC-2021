with open('02/assets/input.txt', 'r') as f:
    travel = f.readlines()

y = 0
z = 0
aim = 0

for step in travel:
    dir = step.split()[0]
    dist = step.split()[1]
    if dir == 'forward':
        y = y+int(dist)
        z = z-(aim*int(dist))
    if dir == 'down':
        aim = aim+int(dist)
    if dir == 'up':
        aim = aim-int(dist)

solution = y*-z
print(solution)