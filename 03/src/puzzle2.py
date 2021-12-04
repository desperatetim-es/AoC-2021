with open('03/assets/input.txt', 'r') as f:
    report = f.readlines()

length = int(len(report[0])) - 2
oxygen_l = list(report)
co2_l = list(report)

while len(oxygen_l) > 1:
    for pos in range(0, length+1):
        c = int(0)
        for reading in oxygen_l:
            if reading[pos] == '1':
                c=c+1
        if c >= len(oxygen_l)/2:
            b = 1
        else:
            b = 0
        l = list(oxygen_l)
        for i in l:
            if int(i[pos]) != b:
                if len(oxygen_l) > 1:
                    oxygen_l.remove(i)
o2rating = str(oxygen_l[0])

for pos in range(0, length+1):
    c = int(0)
    for reading in co2_l:
        if reading[pos] == '1':
            c=c+1
    if c >= len(co2_l)/2:
        b = 0
    else:
        b = 1
    l = list(co2_l)
    for i in l:
        if int(i[pos]) != b:
            if len(co2_l) > 1:
                co2_l.remove(i)
co2rating = str(co2_l[0])

print('   O2 Rating:', int(o2rating,2))
print('  CO2 Rating:', int(co2rating,2))

print('Life Support:', int(o2rating, 2)*int(co2rating, 2))
exit()