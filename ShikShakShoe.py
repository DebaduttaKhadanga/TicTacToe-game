def isOdd(n: int): # Function to check odd numbers to make life easier
    if n%2!=0:
        return True

def showMat(l: list): # Prints the list in a readable matrix form. Also a function to make life easier
    for i in l:
        print(i)

def wCond(l: list): # Function that lists all the winning conditions. If any of the conditions are true, then the function returns True
    lst = [
        l[0][0]==l[1][0]==l[2][0] and l[0][0]==l[1][0]==l[2][0]!=0,
        l[0][1]==l[1][1]==l[2][1] and l[0][1]==l[1][1]==l[2][1]!=0,
        l[0][2]==l[1][2]==l[2][2] and l[0][2]==l[1][2]==l[2][2]!=0,
        l[0][0]==l[1][1]==l[2][2] and l[0][0]==l[1][1]==l[2][2]!=0,
        l[2][0]==l[1][1]==l[0][2] and l[2][0]==l[1][1]==l[0][2]!=0,
        l[0][0]==l[0][1]==l[0][2] and l[0][0]==l[0][1]==l[0][2]!=0,
        l[1][0]==l[1][1]==l[1][2] and l[1][0]==l[1][1]==l[1][2]!=0,
        l[2][0]==l[2][1]==l[2][2] and l[2][0]==l[2][1]==l[2][2]!=0,
        ]
    for a in lst: # This loop checks all the different win conditions
        if(a):
            return True
    
def drawCond(l: list, iteration: int): # After all 9 iterations of the main loop, if the game still doesn't end in a win for either party, then it's a draw
    if(iteration==9 and wCond!=True):
        return True

initial_list = [[0,0,0], [0,0,0], [0,0,0]]
showMat(initial_list)

iteration = 0
while True:
    rc_choice = input("Enter your row and column choice in the order [r,c]: ") # Uses a coordinate geometry system to determine what position the user wants their mark to be at. Splits the user's input at the comma.
    r = int(rc_choice.split(",")[0])-1
    c = int(rc_choice.split(",")[1])-1    
    if(initial_list[r][c]==0):
        if(isOdd(iteration)): # An odd iteration means the second player's turn as the iterations start at zero. An even iteration would mean player one's turn.
            initial_list[r][c] = 2
        else:
            initial_list[r][c] = 1
        showMat(initial_list)
    else:
        print("That position is already taken.") # Returns an error if a position is already taken
        continue
    iteration+=1
    flag = wCond(initial_list)
    if(flag): # If the returned value of wCond() is True, then it displays who won the match, or else the drawCond() function is called which ends the game in a draw.
        print("Player 1 Wins!" if isOdd(iteration) else "Player 2 Wins!")
        break
    elif(drawCond(initial_list, iteration)):
        print("The game is a draw!")
        break
