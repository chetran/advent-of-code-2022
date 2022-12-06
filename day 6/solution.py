import re 

First_markerer_packet = int() 
First_markerer_message = int() 
with open("input.txt", "r") as file:
    for seq in file:
        for index in range(13,len(seq)):
            Start_of_packet = set(re.findall(r"\w",seq[index - 13: index - 9]))
            Start_of_message = set(re.findall(r"\w",seq[index - 13: index + 1]))
            if len(Start_of_packet) == 4 and First_markerer_packet == 0:
                First_markerer_packet = index + 1
            if len(Start_of_message) == 14:
                First_markerer_message = index + 1
                break
            

print("Characters needed to be processed before the first start-of-packet marker is detected:", First_markerer_packet)
print("Characters needed to be processed before the first start-of-message marker is detected:", First_markerer_message)
