import re
inputs = []

with open("input.txt", "r") as file:
    reader = file.readlines()
    for line in reader:
        # Returns a list only numbers. Basically a split but by multiplte characters
        inputs.append(re.findall(r"[\w']+",line.strip()))


def Part1(inputs):
    sum = 0 
    for section in inputs:
        elf1 = set(range(int(section[0]), int(section[1]) + 1))
        elf2 = set(range(int(section[2]), int(section[3]) + 1))
        # Increments sum if all items in elf1 is in elf2 and vice versa
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            sum += 1
    return sum


def Part2(inputs):
    sum = 0 
    for section in inputs:
        elf1 = set(range(int(section[0]), int(section[1]) + 1))
        elf2 = set(range(int(section[2]), int(section[3]) + 1))
        # Increments sum if the length of the returned set from intersection isn't 0
        if len(elf1.intersection(elf2)) != 0:
            sum += 1
    return sum


print("Pairs that fully contain the other:", Part1(inputs))
print("Pairs that overlap?", Part2(inputs))






