        # bb = bitboard
        # for i in range(1, self.z):
        #     bb &= (bitboard >> i*(self.x - 1))
        # if bb != 0 : return True

        # bb = bitboard
        # for i in range(1, self.z):
        #     bb &= bitboard & (bitboard >> i*(self.x + 1))
        # if bb != 0 : return True

        # bb = bitboard
        # for i in range(1, self.z):
        #     bb &= (bitboard >> i*(self.x))
        # if bb != 0 : return True

        # if (bitboard & (bitboard >> (self.x - 1)) & (bitboard >> 2*(self.x - 1)) & (bitboard >> 3*(self.x - 1)) != 0): return True # diagonal \
        # if (bitboard & (bitboard >> (self.x + 1)) & (bitboard >> 2*(self.x + 1)) & (bitboard >> 3*(self.x + 1)) != 0): return True # diagonal /
        # if (bitboard & (bitboard >> self.x) & (bitboard >> 2*self.x) & (bitboard >> 3*self.x) != 0): return True # horizontal
        # if (bitboard & (bitboard >> 1) & (bitboard >>  2) & (bitboard >>  3) != 0): return True # vertical
        # directions = {1, self.x, self.x - 1, self.x + 1}
        # for direction in directions:
        #     bb = bitboard & (bitboard >> direction)
        #     if ((bb & (bb >> (2 * direction))) != 0): return True
        # return False