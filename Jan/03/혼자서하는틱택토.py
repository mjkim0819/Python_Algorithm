bingo = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8],
        [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]

def solution(board):
    posO = set()
    posX = set()
    
    for i, b in enumerate(board):
        for j in range(3):
            if b[j] == 'O': posO.add(i*3 + j+1)
            elif b[j] == 'X': posX.add(i*3 + j+1)
    
    o, x = isBingo(posO), isBingo(posX)
    
    if o+x == 0 and len(posO) - len(posX) in [0, 1]: return 1
    else:
        if o >= 1 and x == 0 and len(posO) == len(posX)+1: return 1
        if x >= 1 and o == 0 and len(posO) == len(posX): return 1

    return 0

def isBingo(pos):
    global bingo
    cnt = 0

    for b in bingo:
        if b[0] in pos and b[1] in pos and b[2] in pos: cnt += 1

    return cnt