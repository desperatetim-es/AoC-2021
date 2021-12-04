with open('03/assets/input.txt', 'r') as f:
    report = f.readlines()

length = int(len(report[0])) - 2
gamma = {}
epsilon = {}

for pos in range(0, length+1):
    l = list()
    for reading in report:
        l.append(reading[pos])
    c = int(0)
    for i in l:
        if int(i) == 1:
            c = c+1
        if int(i) == 0:
            c = c-1
    if  c < 0:
        gamma[pos] = 0
        epsilon[pos] = 1
    elif c > 0:
        gamma[pos] = 1
        epsilon[pos] = 0
    else:
        print("There is an equal nubmber of 1s and zeros in position", pos, ".  What do?")

#Remove all but numbers from the values output of the dictionary
gamma = str(''.join(filter(str.isdigit, str(gamma.values()))))
epsilon = str(''.join(filter(str.isdigit, str(epsilon.values()))))

print('            Gamma:', int(gamma,2))
print('          Epsilon:', int(epsilon,2))

print('Power Consumption:', int(gamma, 2)*int(epsilon, 2))

exit()
    
    




