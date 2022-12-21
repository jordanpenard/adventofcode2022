

f = open("input_day01.txt", "r")
string_per_elf = f.read().split("\n\n")
list_per_elf = [i.split("\n") for i in string_per_elf]
list_of_int = [[int(i) for i in j if i] for j in list_per_elf]
cal_per_elf = list(map(sum, list_of_int))

print(sorted(cal_per_elf, reverse=True)[0])
