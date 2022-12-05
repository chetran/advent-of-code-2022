import re

unorg_stack = []
moves = []

with open("input.txt", "r") as file:
    reader = file.readlines()
    for line in reader:
        if line[1].isdigit():
            break
        unorg_stack.append(line)
    # Honestly should do this in the loop above
    read = False
    for line in reader:
        if not line.strip():
            read = True
        if read:
            # Each move will be a list of 3 integers, first one for "amount of boxes", second one "from where" and thrid "to where?"
            moves.append(re.findall(r"\d+", line))
        

class stackers:
    def __init__(self, stacks) -> None:
        # Should find a way to not hard code all the list 
        self.stack = [[], [], [], [], [], [], [], [], [],]
        self.makeEachStack()

    def makeEachStack(self):
        for row in range(len(unorg_stack)):
            i = 0 
            for col in range(1 , len(unorg_stack[row]), 4):
                # Reason for this if case instead of 'if != "" ' is because for some reason it didn't work, when it really should be the same thing 
                if ord(unorg_stack[row][col]) != 32:
                    self.stack[i].append(unorg_stack[row][col])
                i += 1
    
    def move(self, instruc, model="CM9001"):
        # Our stacks are 0 indexed thats why we need to do intruc[x] - 1 when accessing our stack.
        move = []
        new_stack = []
        # Amount of boxes
        for box in range(instruc[0]):
            # Move from 
            move.append(self.stack[instruc[1] - 1][box])
        
        # Reason for reversing is that we want the box at the bottom of the stack we're moving from to be at the top when we're done
        if model == "CM9000":
            move.reverse()

        # The start of the list is the top of the stack so when we append later it will be at the botton
        for box in move:
            new_stack.append(box)
            # Need to remove from original stack 
            self.stack[instruc[1] - 1].remove(box)
        # Adding the botton of the stack
        for box in self.stack[instruc[2] - 1]:
            new_stack.append(box)
        # Lastly this new stack we made should be how the stack should look like when we're done 
        self.stack[instruc[2] - 1] = new_stack
        

def Part1():
    stack = stackers(unorg_stack)
    for move in moves:
        if len(move) != 0:
            # Turns the list of strings into ints 
            stack.move([eval(i) for i in move], "CM9000")
    print("After the rearrangement: ", end="")
    for i in stack.stack:
        print(i[0], end="")
    print()


def Part2():
    stack = stackers(unorg_stack)
    for move in moves:
        if len(move) != 0:
            # Turns the list of strings into ints 
            stack.move([eval(i) for i in move],)
    print("After the rearrangement: ", end="")
    for i in stack.stack:
        print(i[0], end="")
    print()

    
Part1()
Part2()