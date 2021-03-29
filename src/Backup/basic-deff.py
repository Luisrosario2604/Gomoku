#!/usr/bin/env python3.7
import random


def checkVertical(x, y, board, simbol, rangeMax):
    size = 0
    for i in range(1, rangeMax):
        if y + i > 19:
            break
        elif board[y + i][x] == simbol:
            size += 1
        else:
            break
    for i in range(1, rangeMax):
        if y - 1 < 0:
            break
        elif board[y - i][x] == simbol:
            size += 1
        else:
            break
    return size


def checkHorizontal(x, y, board, simbol, rangeMax):
    size = 0
    for i in range(1, rangeMax):
        if x + i > 19:
            break
        elif board[y][x + i] == simbol:
            size += 1
        else:
            break
    for i in range(1, rangeMax):
        if x - i < 0:
            break
        elif board[y][x - i] == simbol:
            size += 1
        else:
            break
    return size


def checkSlash(x, y, board, simbol, rangeMax):
    size = 0
    for i in range(1, rangeMax):
        if x + i > 19 or y - i < 0:
            break
        elif board[y - i][x + i] == simbol:
            size += 1
        else:
            break
    for i in range(1, rangeMax):
        if x - i < 0 or y + i > 19:
            break
        elif board[y + i][x - i] == simbol:
            size += 1
        else:
            break
    return size


def checkBackSlash(x, y, board, simbol, rangeMax):
    size = 0
    for i in range(1, rangeMax):
        if x + i > 19 or y + i > 19:
            break
        elif board[y + i][x + i] == simbol:
            size += 1
        else:
            break
    for i in range(1, rangeMax):
        if x - i < 0 or y - i < 0:
            break
        elif board[y - i][x - i] == simbol:
            size += 1
        else:
            break
    return size


def checkIfIsRange(board, simbol, rangeMax):
    for x in range(20):
        for y in range(20):
            if board[y][x] == '-':
                if checkHorizontal(x, y, board, simbol, rangeMax) >= rangeMax - 1:
                    return x, y, True
                if checkVertical(x, y, board, simbol, rangeMax) >= rangeMax - 1:
                    return x, y, True
                if checkSlash(x, y, board, simbol, rangeMax) >= rangeMax - 1:
                    return x, y, True
                if checkBackSlash(x, y, board, simbol, rangeMax) >= rangeMax - 1:
                    return x, y, True
    return 0, 0, False


def randomPick(board):
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    while board[y][x] != '-':
        x = random.randint(0, 19)
        y = random.randint(0, 19)
    return x, y


def play():
    board = [
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    ]
    active = 'X'
    passive = 'O'
    while 1:
        line = input().split(' ')
        if line[0] == 'BEGIN':
            active = 'O'
            passive = 'X'
            board[19][18] = 'O'
            print("%d,%d" % (18, 19))
        elif line[0] == 'TURN':
            line = line[1].split(',')
            board[int(line[1])][int(line[0])] = 'X'

            x, y , isWin = checkIfIsRange(board, 'O', 5)
            if not isWin:
                x, y, isLost = checkIfIsRange(board, active, 4)
                if not isLost:
                    x, y, isWin = checkIfIsRange(board, passive, 4)
                    if not isWin:
                        x, y, isLost = checkIfIsRange(board, active, 3)
                        if not isLost:
                            x, y, isWin = checkIfIsRange(board, passive, 3)
                            if not isWin:
                                x, y, isLost = checkIfIsRange(board, active, 2)
                                if not isLost:
                                    x, y, isWin = checkIfIsRange(board, passive, 2)
                                    if not isWin:
                                        x, y = randomPick(board)
            board[y][x] = 'O'
            print("%d,%d" % (x, y))
        if line[0] == 'RESTART':
            break
    return

def start():
    if input() == 'START 20':
        print("OK")
        return 1
    else:
        print("KO Error - Bad size")
    return 0


def main():
    if start() == 1:
        while 1:
            play()
    return



if __name__ == "__main__":
    main()
