#!/usr/bin/env python3.7
import random

sizeGame = 18

def checkVertical(x, y, board, simbol, rangeMax):
    size = 0
    white = 0
    for i in range(1, 6):
        if y + i > sizeGame:
            break
        elif board[y + i][x] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y + i][x] == '-':
                white += 1
            break
    for i in range(1, 6):
        if y - i < 0:
            break
        elif board[y - i][x] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y - i][x] == '-':
                white += 1
            break
    return size, white


def checkHorizontal(x, y, board, simbol, rangeMax):
    size = 0
    white = 0
    for i in range(1, 6):
        if x + i > sizeGame:
            break
        elif board[y][x + i] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y][x + i] == '-':
                white += 1
            break
    for i in range(1, 6):
        if x - i < 0:
            break
        elif board[y][x - i] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y][x - i] == "-":
                white += 1
            break
    return size, white


def checkSlash(x, y, board, simbol, rangeMax):
    size = 0
    white = 0
    for i in range(1, 6):
        if x + i > sizeGame or y - i < 0:
            break
        elif board[y - i][x + i] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y - i][x + i] == '-':
                white += 1
            break
    for i in range(1, 6):
        if x - i < 0 or y + i > sizeGame:
            break
        elif board[y + i][x - i] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y + i][x - i] == '-':
                white += 1
            break
    return size, white


def checkBackSlash(x, y, board, simbol, rangeMax):
    size = 0
    white = 0
    for i in range(1, 6):
        if x + i > sizeGame or y + i > sizeGame:
            break
        elif board[y + i][x + i] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y + i][x + i] == '-':
                white += 1
            break
    for i in range(1, 6):
        if x - i < 0 or y - i < 0:
            break
        elif board[y - i][x - i] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y - i][x - i] == '-':
                white += 1
            break
    return size, white

# def getPoints(x, y, board, simbol):
#     points = 0
#
#     if simbol == 'O':
#         antiSimbol = 'X'
#     else:
#         antiSimbol = 'O'
#
#     points += checkHorizontal(x, y, board, simbol, 5, 1)
#     points += checkVertical(x, y, board, simbol, 5, 1)
#     points += checkSlash(x, y, board, simbol, 5, 1)
#     points += checkBackSlash(x, y, board, simbol, 5, 1)
#     points += checkHorizontal(x, y, board, antiSimbol, 5, 1)
#     points += checkVertical(x, y, board, antiSimbol, 5, 1)
#     points += checkSlash(x, y, board, antiSimbol, 5, 1)
#     points += checkBackSlash(x, y, board, antiSimbol, 5, 1)
#
#     #print ('Points : %d - X : %d - Y : %d' % (points, x, y))
#     return points


def checkIfIsRange(board, simbol, rangeMax, free2sides):
    xTmp = 0
    yTmp = 0
    ifReturn = 0
    xFinal = 0
    yFinal = 0
    possibilityFinal = 0
    isReturnFinal = False
    for x in range(sizeGame + 1):
        for y in range(sizeGame + 1):
            if board[y][x] == '-':
                possibility = 0
                size, white = checkHorizontal(x, y, board, simbol, rangeMax)
                if size >= rangeMax - 1:
                    if (free2sides == 1 and white == 2) or free2sides == 0:
                        xTmp, yTmp, isReturn =  x, y, True
                        possibility += 1
                size, white = checkVertical(x, y, board, simbol, rangeMax)
                if size >= rangeMax - 1:
                    if (free2sides == 1 and white == 2) or free2sides == 0:
                        xTmp, yTmp, isReturn = x, y, True
                        possibility += 1
                size, white = checkSlash(x, y, board, simbol, rangeMax)
                if size >= rangeMax - 1:
                    if (free2sides == 1 and white == 2) or free2sides == 0:
                        xTmp, yTmp, isReturn = x, y, True
                        possibility += 1
                size, white = checkBackSlash(x, y, board, simbol, rangeMax)
                if size >= rangeMax - 1:
                    if (free2sides == 1 and white == 2) or free2sides == 0:
                        xTmp, yTmp, isReturn = x, y, True
                        possibility += 1
                if possibility > possibilityFinal:
                    xFinal, yFinal = xTmp, yTmp
                    possibilityFinal = possibility
                    isReturnFinal = True
    return xFinal, yFinal, isReturnFinal


def randomPick(board):
    x = random.randint(0, sizeGame)
    y = random.randint(0, sizeGame)
    while board[y][x] != '-':
        x = random.randint(0, sizeGame)
        y = random.randint(0, sizeGame)
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
    while 1:
        line = input().split(' ')
        if line[0] == 'BEGIN':
            board[10][10] = 'O'
            print("%d,%d" % (10, 10))
        elif line[0] == 'TURN':
            line = line[1].split(',')
            board[int(line[1])][int(line[0])] = 'X'

            x, y , isWin = checkIfIsRange(board, 'O', 5, 0)
            if not isWin:
                x, y, isLost = checkIfIsRange(board, 'X', 5, 0)
                if not isLost:
                    x, y, isWin = checkIfIsRange(board, 'O', 4, 1)
                    if not isWin:
                        x, y, isLost = checkIfIsRange(board, 'X', 4, 1)
                        if not isLost:
                            x, y = randomPick(board)
            board[y][x] = 'O'
            print("%d,%d" % (x, y))
        if line[0] == 'RESTART':
            break
    return

def start():
    if input() == 'START 19':
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