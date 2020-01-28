
Checking game wins or valid moves can take a sizable computation time. Bitboards offer a unique solution to those game checks. Bitboards are a data structure to represent the game’s state. The idea is to store the game’s state in an array of bits. Once in that form, it is possible to perform operations such as adjacency and intersections.

For the purpose of demonstration, the board as seven bits tall and seven bits wide as shown below.

6 13 20 27 34 41 48
5 12 19 26 33 40 47
4 11 18 25 32 39 46
3 10 17 24 31 38 45
2  9 16 23 30 37 44
1  8 15 22 29 36 43
0  7 14 21 28 35 42 

The height is important for two reasons. The first is that it guides the “constant” that we use to bitshift. Second, we include a buffer of one space on the top of the board to prevent the false positives from the board wrapping around 
