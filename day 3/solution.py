inputs = []

# Check ascii table for chosen values
def getValue(character):
    if character.isupper():
        return 27 + ord(character) - 65
    return ord(character) - 96


with open("input.txt", "r") as file:
    reader = file.readlines()
    for line in reader:
        inputs.append(line.strip())


def Part1(inputs):
    sum = 0 
    for line in inputs:
        length = len(line) // 2
        # Returns a list of characters from a string 
        firstHalf = [*line[0:length]]
        secondHalf = [*line[length:]]
        # Finds the common character in both lists 
        sameItem = set(firstHalf) & set(secondHalf)
        # Reason for iterating: Even tho its only one item in the set I dont know how to access that ONE item! 
        for item in sameItem:
            sum += getValue(item)
    return sum


def Part2(inputs):
    sum = 0
    for group in range(0, len(inputs), 3):
        elf1 = inputs[group]
        elf2 = inputs[group + 1]
        elf3 = inputs[group + 2]
        badges = set(elf1) & set(elf2) & set(elf3)
        # Same reason for iterating over the set.
        for badge in badges:
            sum += getValue(badge)
    return sum


print("Sum of the priorities of those item types?", Part1(inputs))
print("The sum of the priorities of those item types:", Part2(inputs))


    


