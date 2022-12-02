# Helper function. We're comparing ascii values, no specific reason why i didnt choose 64 as standard. 
# However we need to alternate the base variable depending on who's choice we're looking at.
# These two values comes from characters behind A and X, so for A that would be "@" (64) and for X that would be "W" (87)
def getValueForPick(pick, base=87):
    return ord(pick) - base

# Part 1 
sum = 0
with open("input.txt", "r") as file:
    reader = file.readlines()
    for row in reader:
        opponentChoice = getValueForPick(row[0], 64)
        myChoice = getValueForPick(row[2]) 
        sum += myChoice # The points for the pick 
        result = opponentChoice - myChoice
        # When its draw
        if result == 0:
            sum += 3
        # When its a loss
        # -2 is for when opponent picks rock and i pick scissor => 1-3= -2 
        elif result == 1 or result == -2:
            pass
        # Otherwise I would win
        else:
            sum += 6    


print("My total score would be:",sum, "pts")

# Part 2 
sum1 = 0
with open("input.txt", "r") as file:
    reader = file.readlines()
    for row in reader:
        opponentChoice = getValueForPick(row[0], 64)
        whatImGonnaDo = getValueForPick(row[2]) 
        # I need to lose
        if whatImGonnaDo == 1:
            # So inorder to lose i almost always pick the something "1 less" than opponentChoice. 
            # Except when he picks rock which is equivalent to 1, I need to pick scissors which is equivalent to 3 
            if opponentChoice == 1:
                sum1 += 3
            else:
                sum1 += opponentChoice - 1
        # I need to draw
        elif whatImGonnaDo == 2:
            sum1 += 3 + opponentChoice
        # I need to win
        else:
            # Same logic when it comes to winning, I should almost always pick something "1 greater" than opponentChoice
            # Except when he picks scissors (3), I want to pick rock (1)
            if opponentChoice == 3:
                sum1 += 6 + 1
            else:
                sum1 += 6 + opponentChoice + 1

print("My points if i followed his strat:", sum1, "pts")
