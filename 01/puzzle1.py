#Try re-writing with 'with'
readings_file = open('01/inputs/sonar.txt', 'r')
readings_content = readings_file.read()
readings_list = readings_content.split()
readings_list = list(map(int, readings_list))

calc_last = readings_list[0]
increase_count = 0

for calc_current in readings_list:
    if calc_current > calc_last:
        increase_count = increase_count+1
    calc_last = calc_current

print(increase_count)