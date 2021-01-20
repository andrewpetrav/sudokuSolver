r''' regions
      |       |  
  0   |   1   |   2
      |       |  
- - - - - - - - - - -
      |       |  
  3   |   4   |   5  
      |       |  
- - - - - - - - - - -
      |       |  
  6   |   7   |   8 
      |       | 
'''

r'''
board=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]
'''
permutations=0

board=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

def enter():
    for i in range(9):
        s=['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
        print("Enter the",s[i], "row (put spaces in between each number): ")
        row_entry=input()
        entry=row_entry.split(' ')
        for j in range(len(entry)):
            entry[j]=int(entry[j])
        while len(entry)<9:
            entry.append(0)
        board[i]=entry

    draw(board)
    r'''
    hange=input("Are there any rows that you'd like to change. Type 'Yes' if there are any rows that you'd like to edit. If not, press enter now.")
    while change=="Yes":
        change_row=input("Enter the number(s) of the row(s) that you'd like to change. Include a space in between each row.")
     '''   
        
        
def draw(b):
    for row in range(len(b)):
        for col in range(len(b[0])):
            print(b[row][col], end=' ')
            if col==2 or col==5:
                print('|', end=' ')
        print()
        if row==2 or row==5:
            print('- - - - - - - - - - -')

def find_empty(b):
    for x in range(0,9):
        for y in range(0,9):
            if b[x][y]==0:
                return (x,y)
    return (-1,-1) #indicates no more empty cells

def check_validity(b,r,c,num):
    region=[0,0] #top left
    for ver in range(0,9): #check vertical
        if b[ver][c]==num:
            return False
    for hor in b[r]: #check horizontal
        if hor==num:
            return False
    #find square
    if r<=2:
        if c<=2:
            region=[0,0]
        elif c<=5:
            region=[0,3]
        else:
            region=[0,6]
    elif r<=5:
        if c<=2:
            region=[3,0]
        elif c<=5:
            region=[3,3]
        else:
            region=[3,6]
    else:
        if c<=2:
            region=[6,0]
        elif c<=5:
            region=[6,3]
        else:
            region=[6,6]
    for i in range(region[0], region[0]+3):
        for j in range(region[1], region[1]+3):
            if b[i][j]==num:
                return False
    #valid number
    return True

def solve(b,row=0,col=0):
    global permutations
    permutations+=1
    row,col=find_empty(b)
    if col==-1:
        board=b
        return True #solved
    for n in range(1,10):
        if check_validity(b,row,col,n):
            b[row][col]=n
            if solve(b, row, col):
                return True
        #backctrack
        b[row][col] = 0
    return False
print("Welcome to SudokuSolver! Want to impress your friends and family by being a master at sudoku, but don't want to have to actually use your brain? Then you've come to the right place!")
print("Simply enter the values of the puzzle row by row. Enter blank values as a '0'. Don't worry about the lines or anything like that.")
print("After you enter each row, press enter to enter the next row")
print("After you enter all rows, you can go back and edit one if you have made a mistake.")
enter()
solve(board)
print()
print('SOLUTION')
draw(board)
print(permutations)
                     

    
    
   
