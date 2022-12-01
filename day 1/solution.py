elfs_cal = []
sum = 0

# Part 1
with open("input.txt", "r") as file:
    reader = file.readlines()
    last = reader[-1]
    for line in reader:
        line = line.strip()
        if not line or line == last: # If its an empty string or its the last element 
            elfs_cal.append(sum)
            sum = 0
        else:
            sum += int(line)


print("The elf carrying the most calories has:",max(elfs_cal), "cal")

# Part 2, we can reuse sum, since sum will be 0 after the last elf.
for i in range(3):
    current_top = max(elfs_cal)
    sum += current_top
    elfs_cal.remove(current_top)

print("The calorie total of top 3 are:", sum, "cal")
