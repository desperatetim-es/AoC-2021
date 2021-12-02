readings_file = open('01/inputs/sonar.txt', 'r')
readings_content = readings_file.read()
readings_list = readings_content.split()
readings_windows = []

#copypasta... what is this doing, is ther a more efficient way?
def window(fseq, window_size=5):
    for i in range(len(fseq) - window_size + 1):
        yield fseq[i:i+window_size]


for seq in window(readings_list, 3):
    readings_windows.append(seq)
#/copypasta

readings_first = readings_windows[0]
calc_last = int(readings_first[0])+int(readings_first[1])+int(readings_first[2])
increase_count = 0

for readings_window in readings_windows:
    calc_current = int(readings_window[0])+int(readings_window[1])+int(readings_window[2])
    if calc_current > calc_last:
        increase_count = increase_count+1
    calc_last = calc_current

print(increase_count)