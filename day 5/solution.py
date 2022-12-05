import re

unorg_stack = []
moves = []
stacks_count = 0


with open("input.txt", "r") as file:
    reader = file.readlines()
    done_with_stacks = False
    for line in reader:
        if not line.strip():
            done_with_stacks = True
        if not done_with_stacks:
            unorg_stack.append(line)
            # Divide by 4 because each stack are 4 characters apart
            stacks_count = len(line) // 4 
        elif done_with_stacks:
            moves.append(re.findall(r"\d+", line))
        
class stackers:
    def __init__(self, stacks) -> None:
        self.stack = []
        self.makeStacks()
        self.makeEachStack()


    def makeEachStack(self):
        for row in range(len(unorg_stack)):
            stack = 0 
            for col in range(1 , len(unorg_stack[row]), 4):
                # Reason for this if case instead of 'if != "" ' is because for some reason it didn't work, when it really should be the same thing 
                if ord(unorg_stack[row][col]) != 32 and not unorg_stack[row][col].isdigit():
                    self.stack[stack].append(unorg_stack[row][col])
                stack += 1


    def move(self, instruc, model="CM9001"):
        # Our stacks are 0 indexed thats why we need to do intruc[x] - 1 when accessing our stack.
        move = []
        new_stack = []
        for box in range(instruc[0]):
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
        
    def makeStacks(self):
        for stack in range(stacks_count):
            self.stack.append([])


def printAnswer(stack):
    print("After the rearrangement: ", end="")
    for i in stack.stack:
        print(i[0], end="")
    print()


def Solution():
    CM9000 = stackers(unorg_stack)
    CM9001 = stackers(unorg_stack)
    for move in moves:
        if len(move) != 0:
            # Turns the list of strings into ints 
            CM9000.move([eval(i) for i in move], "CM9000")
            CM9001.move([eval(i) for i in move])
    printAnswer(CM9000)
    printAnswer(CM9001)


Solution()
