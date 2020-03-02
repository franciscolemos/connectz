#connectz

connectz.py script was built and tested in Windows 10 running Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)]
Checking game wins or valid moves can take a sizable computation time. Bitboards offer a unique solution to those game checks. Bitboards are a data structure to represent the game's state. The idea is to store the game's state in an array of bits. Once in that form, it is possible to perform operations such as adjacency and intersections.

For the purpose of demonstration game is width of 7 and a height of 6; however the board as seven bits tall to prevent the false positives from the board wrapping around: 

  6 13 20 27 34 41 48   Additional row
+---------------------+ 
| 5 12 19 26 33 40 47 | Top row
| 4 11 18 25 32 39 46 | 
| 3 10 17 24 31 38 45 | 
| 2  9 16 23 30 37 44 | 
| 1  8 15 22 29 36 43 | 
| 0  7 14 21 28 35 42 | Bottom row
+---------------------+

We encode the position separately for each player. One bitboard encodes the position with tokens 1 only, the other bitboard the position with tokens 2 only.

               0 0 0 0 0 0 0  0 0 0 0 0 0 0   6 13 20 27 34 41 48
. . . . . . .  0 0 0 0 0 0 0  0 0 0 0 0 0 0   5 12 19 26 33 40 47
. . . . . . .  0 0 0 0 0 0 0  0 0 0 0 0 0 0   4 11 18 25 32 39 46
. . . . . . .  0 0 0 0 0 0 0  0 0 0 0 0 0 0   3 10 17 24 31 38 45
. . . 2 . . .  0 0 0 0 0 0 0  0 0 0 1 0 0 0   2  9 16 23 30 37 44
. . . 1 1 . .  0 0 0 1 1 0 0  0 0 0 0 0 0 0   1  8 15 22 29 36 43
. . 2 1 2 . .  0 0 0 1 0 0 0  0 0 1 0 1 0 0   0  7 14 21 28 35 42
-------------
0 1 2 3 4 5 6  

Shown as a flat series of ones and zeros the two bitboards look like this. Leading zeros, i.e. the bits beyond position 48, are cut off.

0000000 0000000 0000010 0000011 0000000 0000000 0000000 // encoding 1s
0000000 0000000 0000001 0000100 0000001 0000000 0000000 // encoding 2s
 col 6   col 5   col 4   col 3   col 2   col 1   col 0

By shifting our resulting bitstring 14 positions to the right, we are checking if we can match two horizontally consecutive tokens with two other horizontally consecutive tokens 2 positions left to it on the board. These steps combined are equivalent to checking whether four tokens are connected horizontally. The operations for the other directions (diagonally and vertically) are the same, we just shift our bitmap for more or less positions (1 for vertical, 8 for diagonal to the south-west (/) and 6 for diagonal to the south-east (\)). The code this approach to any valid size of consecutive tokens.
 
Another piece of information we track is the number of moves done, a counter. Each time we make a move we increment the counter. We proceed in this way to validate illegal rows. The remaining validations are set to check, the problem statement.

We designed the script to solve boards 999 x 999 x 999.

Test files are supplied for the following situations:
data.dat Win for player 1
data20x20z7.dat Win for player 2
data100x100z4.dat Win for player 1
dataIllegalColumn.dat Illegal column
dataIllegalContinue.dat Illegal continue
dataIllegalGame.dat Illegal game
dataIllegalRow1.dat Illegal row. The script detects if the row is not a digit.
dataIllegalRow2.dat Illegal row. The script detects if the row is outside the board.

Finally the script will loop until the user types a valid file name.


### Installing

git clone https://github.com/franciscolemos/connectz.git

### Run

python main.py







