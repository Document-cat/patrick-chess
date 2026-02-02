import numpy as np
import textwrap

#----Start of Bit Boards----
class bitBoard:     
    wP = np.uint64(0x00FF000000000000)
    wR = np.uint64(0x8100000000000000)
    wN = np.uint64(0x4200000000000000)
    wB = np.uint64(0x2400000000000000)
    wQ = np.uint64(0x1000000000000000)
    wK = np.uint64(0x8000000000000000)

    bP = np.uint64(0x000000000000FF00)
    bR = np.uint64(0x0000000000000081)
    bN = np.uint64(0x0000000000000042)
    bB = np.uint64(0x0000000000000024)
    bQ = np.uint64(0x0000000000000001)
    bK = np.uint64(0x8000000000000000)


def printBitBoard(bitBoard):
    bstring = (bin(bitBoard)[2:].zfill(64))
    bstring = bstring.replace("0",".")
    print(bstring)
    
    
    
printBitBoard(bitBoard.wP)
