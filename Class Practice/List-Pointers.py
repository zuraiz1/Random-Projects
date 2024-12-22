from os import system
from time import sleep

# Making the List itself

class Node():
    def __init__(self):
        self.data = ""
        self.next = None

L_list = [Node() for _ in range(6)]

for i in range(5):
    L_list[i].next = i+1

L_list[len(L_list)-1].next = -1

Start, Free = -1 , 0

# Making functions for the list

def add(val : str):
    global L_list, Start, Free

    if Start == -1:
        Start = Free
        L_list[Free].data = val
        Free = L_list[Free].next

    else:
        old  = 0
        current = Start
        while L_list[current].next != Free or L_list[current].data < val:
            old = current
            current = L_list[current].next
        
        if current == Start:
            L_list[Free].data = val
            Free = L_list[current].next
            
def add(val: str):
    global L_list, Start, Free

    if Start == -1:  # List is empty
        Start = Free
        L_list[Free].data = val
        Free = L_list[Free].next
    else:
        old = -1
        current = Start

        while current != -1 and L_list[current].data < val:
            old = current
            current = L_list[current].next

        # Insert the new node
        if old == -1:  # Insert at the beginning
            L_list[Free].data = val
            L_list[Free].next = Start
            Start = Free
        else:  # Insert in the middle or end
            L_list[Free].data = val
            L_list[Free].next = current
            L_list[old].next = Free

    # Update Free pointer
    Free = L_list[Free].next  # Update Free to the next available node


# Display
def display():
    global L_list, Start, Free
    system("cls")
    if Start == -1:
        print("List is empty")
    else:
        for i in range(len(L_list)):
            print('[ ', i ,' ] ',' | ', L_list[i].data, ' | ' , L_list[i].next)
    
    sleep(0.5)


# MAIN PROGRAM #

while True:
    display()

    add(input("Enter a Alphabet to add : "))

    
    