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
        self.x = x #width of the board
        self.y = y #height of the board
        self.z = z #no. of tokens to connect
        self.matrix = [[0 for w in range(x)] for h in range(y + 1)] #init. matrix of zeros
        self.col = [0] * self.x #init. the row counter for each column
        self.counter = 0 #init. player turn to move
    def insert(self, column): #
        index = column -1 #pyhton array is zero based
        self.col[index] += 1 #keep track of the height of the column
        if self.col[index] > self.y: #height is not allowed
            return 5
        player =  1 if self.counter % 2 == 0 else 2
        self.matrix[self.y + 1 - self.col[index]][column - 1] = player
        self.check(player, column, self.counter) #
        position, mask = self.get_position_mask_bitmap(player)
        print(position, mask)
        #import pdb; pdb.set_trace()
        win = self.connected_four(position)
        if win:
            return player
        self.counter += 1

    def check(self, player, column, counter):
        print("Player", player, "Column", column, "Play", counter)
        import pprint as pp
        pp.pprint(self.matrix)

    def get_position_mask_bitmap(self, player):
        position, mask = '', ''
        # Start with right-most column
        for j in range(self.x - 1, -1, -1):
            # Add 0-bits to sentinel 
            mask += '0'
            position += '0'
            # Start with bottom row
            for i in range(0, self.y):
                mask += ['0', '1'][self.matrix[j][i] != 0]
                position += ['0', '1'][self.matrix[j][i] == player]
        print(position, mask)
        return int(position, 2), int(mask, 2)

    def connected_four(self, position):
        # Horizontal check
        m = position & (position >> (self.x))
        if m & (m >> (2 * self.x)):
            return True
        # Diagonal \
        m = position & (position >> (self.x - 1))
        if m & (m >> (2 * (self.x - 1))):
            return True
        # Diagonal /
        m = position & (position >> (self.x + 1))
        if m & (m >> (2 * (self.x + 1))):
            return True
        # Vertical
        m = position & (position >> 1)
        if m & (m >> 2):
            return True
        # Nothing found
        return False
        
def read_file_content(f):
    headerLine = f.readline()
    header = headerLine.rstrip()
    regExp = '^\d{1,3}\ \d{1,3}\ \d{1,3}$' #3 digits sep. by space
    p = re.compile(regExp)
    if not p.match(header):
        print("Error code 8: Invalid file")
        return

    x = int(headerLine.rstrip().split(" ")[0])
    y = int(headerLine.rstrip().split(" ")[1])
    z = int(headerLine.rstrip().split(" ")[2])
    if (x < z) and (y < z):
        print("Error code 7: Illegal game")
        return
    
    moves = f.read().splitlines()
    if len(moves) > x * y:
        print("Error code 5: Illegal row") #if the no. of moves is bigger than total no. of cells it's not worth prusue further
        return
    insertOK = -1
    p = play(x, y, z)
    for move in moves:
        if (insertOK == 1) or (insertOK == 2): #of the player won but the are still moves
            if move != None:
                print("Error code 4: Illegal continue") #the grame has already been won
                return
        if not move.isdigit():
            print("Error code 8: Invalid file") #the move is not valid digit
            return
        if int(move) > x:
            print("Error code 6: Illegal column") #the column is not in the allowed interval
            return
        insertOK = p.insert(int(move))
        if insertOK == 5:
            print("Error code 5: Illegal row") #the column is full
            return

    if (insertOK == 1) or (insertOK == 2): #one of the players won
        print("Win for player", insertOK)
        return

    if insertOK == -1:
        if len(moves) == x * y:
            print("Draw") # Code 0
            return

    print("Error code 3: Incomplete")
    return

if __name__ == "__main__":
    f = None
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        f = read_file(fileName)
    while f == None:
        fileName = input("connectz.py: Provide one input file ")
        f = read_file(fileName)
    
    read_file_content(f)

    
        
    
