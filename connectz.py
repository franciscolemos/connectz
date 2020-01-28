import sys
import re

def read_file(fileName):
    try:
        f = open(fileName)
        return f
    except OSError:
        fileName = input("connectz.py: Provide one input file ")
        return None

class play:
    def __init__(self, x, y, z):
        self.x = x # Width of the board
        self.y = y # Height of the board
        self.z = z # No. of tokens to connect
        self.matrix = [[0 for w in range(x)] for h in range(y)] #init. matrix of zeros
        self.col = [0] * self.x # init. the row counter for each column
        self.counter = 0 # init. player turn to move

    def insert(self, column): #
        index = column -1 # Because pyhton array is zero based
        self.col[index] += 1 # To keep track of the height of the column
        if self.col[index] > self.y: # Height is not allowed
            return 5
        player =  1 if self.counter % 2 == 0 else 2 # To decide who plays 0: player 1, 1: player 2
        self.matrix[self.y - self.col[index]][column - 1] = player # To record all plays
        position, mask = self.get_position_mask_bitmap(player) # To retrive the board and the play encoded to integer
        win = self.is_win(position) # Check if there is a win
        if win:
             return player
        self.counter += 1

    def get_position_mask_bitmap(self, player):
        position, mask = '', ''
        for j in range(self.x - 1, -1, -1):# Start with right-most column
            # Add 0-bits to sentinel 
            mask += '0'
            position += '0'
            # Start with bottom row
            for i in range(0, self.y):
                mask += ['0', '1'][self.matrix[i][j] != 0]
                position += ['0', '1'][self.matrix[i][j] == player]
        return int(position, 2), int(mask, 2) # Encode binary strings to integer

    def is_win(self, bitboard):
        if (bitboard & (bitboard >> (self.x - 1)) & (bitboard >> 2*(self.x - 1)) & (bitboard >> 3*(self.x - 1)) != 0): return True # diagonal \
        if (bitboard & (bitboard >> (self.x + 1)) & (bitboard >> 2*(self.x + 1)) & (bitboard >> 3*(self.x + 1)) != 0): return True # diagonal /
        if (bitboard & (bitboard >> self.x) & (bitboard >> 2*self.x) & (bitboard >> 3*self.x) != 0): return True # horizontal
        if (bitboard & (bitboard >> 1) & (bitboard >>  2) & (bitboard >>  3) != 0): return True # vertical
        # directions = {1, self.x, self.x - 1, self.x + 1}
        # for direction in directions:
        #     bb = bitboard & (bitboard >> direction)
        #     if ((bb & (bb >> (2 * direction))) != 0): return True
        # return False

def read_file_content(f):
    headerLine = f.readline()
    header = headerLine.rstrip()
    regExp = '^\d{1,3}\ \d{1,3}\ \d{1,3}$' # Reg. exp. 3 digits sep. by space
    p = re.compile(regExp)
    if not p.match(header): # Check if the header matches the reg. exp. 
        print("Error code 8: Invalid file")
        return
    headerArr = headerLine.rstrip().split(" ")
    x = int(headerArr[0])
    y = int(headerArr[1])
    z = int(headerArr[2])
    # Find ASAP if the game is valid
    if (x < z) and (y < z):
        print("Error code 7: Illegal game")
        return

    moves = f.read().splitlines() # Read all the lines of the files after the header
    # If the no. of moves is bigger than total no. of cells it's not worth prusue further
    if len(moves) > x * y:
        print("Error code 5: Illegal row") 
        return
    insertOK = -1
    p = play(x, y, z)
    for move in moves:
        # One of the players won but the are still moves
        if (insertOK == 1) or (insertOK == 2): 
            if move != None:
                print("Error code 4: Illegal continue") 
                return
        # The move is not valid digit
        if not move.isdigit():
            print("Error code 8: Invalid file") 
            return
        # The column is not in the allowed interval
        if int(move) > x:
            print("Error code 6: Illegal column") 
            return
        insertOK = p.insert(int(move))
        if insertOK == 5:
            print("Error code 5: Illegal row") #the column is full
            return
    # The game has ended and one of the players won
    if (insertOK == 1) or (insertOK == 2):
        print("Win for player", insertOK)
        return
    # The game has ended and none of the players won and the board is full 
    if insertOK == -1:
        if len(moves) == x * y:
            print("Draw") # Code 0
            return
    # The game has ended and one of the players won and the board is not full 
    print("Error code 3: Incomplete")
    return

if __name__ == "__main__":
    f = None
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        f = read_file(fileName)
    # Loop until a valid file name is provided
    while f == None:
        fileName = input("connectz.py: Provide one input file ")
        f = read_file(fileName)
    
    read_file_content(f)

    
        
    
