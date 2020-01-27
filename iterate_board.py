import numpy as np
# board = np.array([[6, 13, 20, 27, 34, 41, 48],
#          [5, 12, 19, 26, 33, 40, 47],
#          [4, 11, 18, 25, 32, 39, 46],
#          [3, 10, 17, 24, 31, 38, 45],
#          [2,  9, 16, 23, 30, 37, 44],
#          [1,  8, 15, 22, 29, 36, 43],
#          [0,  7, 14, 21, 28, 35, 42]])


# _board = [[6, 13, 20, 27, 34, 41, 48],
#          [5, 12, 19, 26, 33, 40, 47],
#          [4, 11, 18, 25, 32, 39, 46],
#          [3, 10, 17, 24, 31, 38, 45],
#          [2,  9, 16, 23, 30, 37, 44],
#          [1,  8, 15, 22, 29, 36, 43],
#          [0,  7, 14, 21, 28, 35, 42]]


#correct format of position
board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 0, 2, 1, 0, 0, 0],
         [0, 0, 2, 2, 1, 0, 0],
         [0, 0, 2, 1, 1, 2, 0]]



x = 7
y = 6
player = 1
position, mask = '', ''
# Start with right-most column
for j in range(6, -1, -1): #7 - 1
    # Add 0-bits to sentinel 
    mask += '0'
    position += '0'
    # Start with bottom row
    for i in range(0, 6): # 7 = 6 + 1
        mask += ['0', '1'][board[i][j] != 0] # j = x, y = i
        position += ['0', '1'][board[i][j] == player]

print(int(mask, 2))
print(int(position, 2))
import pdb; pdb.set_trace()

self.check(player, column, self.counter) #

def check(self, player, column, counter):
    print("Player", player, "Column", column, "Play", counter + 1)
    import pprint as pp
    pp.pprint(self.matrix)
