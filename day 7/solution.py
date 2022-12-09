Part1Sum = 0
all_files = {}
Part2Sum = 70000000 # Just max storage

def addFile(all_files: dict, paths: list, add: dict):
    # Just so we dont change the original list
    paths_copy = paths.copy()

    # If the path is 1 then we want to add it here, whatever that is 
    if len(paths) == 1 and paths[0] in all_files:
        return all_files[paths[0]].update(add)

    # Else we're gonna look through the dict if there is a key that has the same name as the first path in paths.
    # It's also important, that the key is a dict.
    for dir, inside in all_files.items():
        if dir == paths[0] and isinstance(inside, dict):
            # If there is we want to remove that path from our list so in some sense "we're inside of it".
            paths_copy.remove(paths_copy[0])
            # Recurse but sending the new dict until we're in the right position
            return addFile(inside, paths_copy, add)
    # If all those fails that means all_files is empty
    all_files[paths[0]] = {}
    # If the path happend to be longer that ["/"........] then we want to keep going 
    paths_copy.remove(paths_copy[0])
    if len(paths) == 1:
        return all_files[paths[0]].update(add)
    return addFile(all_files[paths[0]], paths_copy, add)


def Solution(inputs):
    # Honestly, should probably think of a way of not using global variable
    global Part1Sum
    global Part2Sum
    # The idea is that the roots of the dict will start with 0 and the rest of the dicts is gonna build upon that 
    # It will always return sum so thats why it made it hard to seperate what values we want and dont want.
    sum = 0
    for k, v in inputs.items():
        if isinstance(v, dict):
            sum += Solution(v)
        elif isinstance(v, str):
            sum += int(v)
    # Part 1
    if sum < 100000:
        Part1Sum += sum
    # Part 2 
    if sum >= 2143088 and sum < Part2Sum:
        Part2Sum = sum
    return sum


with open("input.txt", "r") as file:
    reader = file.readlines()
    # Where we are currently
    pwd = []
    for line in reader:
        line = line.strip().split(" ")
        # Commandlines
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    pwd.pop()
                else:
                    pwd.append(line[2])
            # So if its not cd then its ls we kinda dont want to do anything but to skip.
            else:
                continue
        # None of the above means its a file or a dir.
        else:
            item = {f"{line[1]}": f"{line[0]}"}
            if line[0] == "dir":
                item = {f'{line[1]}': {}}
            addFile(all_files, pwd, item)


Solution(all_files)
print("Total sizes of those directories:",Part1Sum)
print("Size of that directory:",Part2Sum)


