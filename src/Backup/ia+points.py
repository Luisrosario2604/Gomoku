#!/usr/bin/env python3.7
import random

sizeGame = 18

def checkVertical(x, y, board, simbol, rangeMax, isPoint):
    size = 0
    blocked = 0
    white = 0
    white1 = 0
    white2 = 0
    for i in range(1, 6):
        if y + i > sizeGame:
            break
        elif board[y + i][x] == simbol and blocked == 0 and i <= rangeMax:
            size += 1
        elif board[y + i][x] == '-' or board[y + i][x] == simbol:
            white += 1
            blocked = 1
            white1 = 1
        else:
            break
    blocked = 0
    for i in range(1, 6):
        if y - 1 < 0:
            break
        elif board[y - i][x] == simbol and blocked == 0 and i <= rangeMax:
            size += 1
        elif board[y - i][x] == '-' or board[y - i][x] == simbol:
            white += 1
            blocked = 1
            white2 = 1
        else:
            break
    if size + white < 5 :
        return 0
    if isPoint == 0:
        return size
    elif white1 == 1 and white2 == 1:
        return size * 10 + white + 10
    else:
        return size * 10 + white


def checkHorizontal(x, y, board, simbol, rangeMax, isPoint):
    size = 0
    white = 0
    blocked = 0
    white1 = 0
    white2 = 0
    for i in range(1, 6):
        if x + i > sizeGame:
            break
        elif board[y][x + i] == simbol and blocked == 0 and i <= rangeMax:
            size += 1
        elif board[y][x + i] == '-' or board[y][x + i] == simbol:
            white += 1
            blocked = 1
            white1 = 1
        else:
            break
    blocked = 0
    for i in range(1, 6):
        if x - i < 0:
            break
        elif board[y][x - i] == simbol and blocked == 0 and i <= rangeMax:
            size += 1
        elif board[y][x - i] == '-' or board[y][x - i] == simbol:
            white += 1
            blocked = 1
            white2 = 1
        else:
            break
    if size + white < 5:
        return 0
    if isPoint == 0:
        return size
    elif white1 == 1 and white2 == 1:
        return size * 10 + white + 10
    else:
        return size * 10 + white


def checkSlash(x, y, board, simbol, rangeMax, isPoint):
    size = 0
    white = 0
    blocked = 0
    white1 = 0
    white2 = 0
    for i in range(1, 6):
        if x + i > sizeGame or y - i < 0:
            break
        elif board[y - i][x + i] == simbol and blocked == 0 and i <= rangeMax:
            size += 1
        elif board[y - i][x + i] == '-' or board[y - i][x + i] == simbol:
            white += 1
            blocked = 1
            white1 = 1
        else:
            break
    blocked = 0
    for i in range(1, 6):
        if x - i < 0 or y + i > sizeGame:
            break
        elif board[y + i][x - i] == simbol and blocked == 0 and i <= rangeMax:
            size += 1
        elif board[y + i][x - i] == '-' or board[y + i][x - i] == simbol:
            white += 1
            blocked = 1
            white2 = 1
        else:
            break
    if size + white < 5:
        return 0
    if isPoint == 0:
        return size
    elif white1 == 1 and white2 == 1:
        return size * 10 + white + 10
    else:
        return size * 10 + white


def checkBackSlash(x, y, board, simbol, rangeMax, isPoint):
    size = 0
    white = 0
    blocked = 0
    white1 = 0
    white2 = 0
    for i in range(1, 6):
        if x + i > sizeGame or y + i > sizeGame:
            break
        elif board[y + i][x + i] == simbol and blocked == 0 and i <= rangeMax:
            size += 1
        elif board[y + i][x + i] == '-' or board[y + i][x + i] == simbol:
            white += 1
            blocked = 1
            white1 = 1
        else:
            break
    blocked = 0
    for i in range(1, 6):
        if x - i < 0 or y - i < 0:
            break
        elif board[y - i][x - i] == simbol and blocked == 0 and i <= rangeMax:
            size += 1
        elif board[y - i][x - i] == '-' or board[y - i][x - i] == simbol:
            white += 1
            blocked = 1
            white2 = 1
        else:
            break
    if size + white < 5:
        return 0
    if isPoint == 0:
        return size
    elif white1 == 1 and white2 == 1:
        return size * 10 + white + 10
    else:
        return size * 10 + white

def getPoints(x, y, board, simbol):
    points = 0

    if simbol == 'O':
        antiSimbol = 'X'
    else:
        antiSimbol = 'O'

    points += checkHorizontal(x, y, board, simbol, 5, 1)
    points += checkVertical(x, y, board, simbol, 5, 1)
    points += checkSlash(x, y, board, simbol, 5, 1)
    points += checkBackSlash(x, y, board, simbol, 5, 1)
    points += checkHorizontal(x, y, board, antiSimbol, 5, 1)
    points += checkVertical(x, y, board, antiSimbol, 5, 1)
    points += checkSlash(x, y, board, antiSimbol, 5, 1)
    points += checkBackSlash(x, y, board, antiSimbol, 5, 1)

    #print ('Points : %d - X : %d - Y : %d' % (points, x, y))
    return points


def checkIfIsRange(board, simbol, rangeMax):
    xTmp = 0
    yTmp = 0
    points = 0
    isStop = False
    for x in range(sizeGame):
        for y in range(sizeGame):
            if board[y][x] == '-':
                if checkHorizontal(x, y, board, simbol, rangeMax, 0) >= rangeMax - 1:
                    tmpPoints = getPoints(x, y, board, simbol)
                    if tmpPoints >= points :
                        points = tmpPoints
                        xTmp, yTmp, isStop = x, y, True
                if checkVertical(x, y, board, simbol, rangeMax, 0) >= rangeMax - 1:
                    tmpPoints = getPoints(x, y, board, simbol)
                    if tmpPoints >= points :
                        points = tmpPoints
                        xTmp, yTmp, isStop = x, y, True
                if checkSlash(x, y, board, simbol, rangeMax, 0) >= rangeMax - 1:
                    tmpPoints = getPoints(x, y, board, simbol)
                    if tmpPoints >= points:
                        points = tmpPoints
                        xTmp, yTmp, isStop = x, y, True
                if checkBackSlash(x, y, board, simbol, rangeMax, 0) >= rangeMax - 1:
                    tmpPoints = getPoints(x, y, board, simbol)
                    if tmpPoints >= points:
                        points = tmpPoints
                        xTmp, yTmp, isStop = x, y, True
    return xTmp, yTmp, isStop


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

            x, y , isWin = checkIfIsRange(board, 'O', 5)
            if not isWin:
                x, y, isLost = checkIfIsRange(board, 'X', 5)
                if not isLost:
                    x, y, isLost = checkIfIsRange(board, 'O', 4)
                    if not isLost:
                        x, y, isWin = checkIfIsRange(board, 'X', 4)
                        if not isWin:
                            x, y, isLost = checkIfIsRange(board, 'O', 3)
                            if not isLost:
                                x, y, isWin = checkIfIsRange(board, 'X', 3)
                                if not isWin:
                                    x, y, isLost = checkIfIsRange(board, 'O', 2)
                                    if not isLost:
                                        x, y, isWin = checkIfIsRange(board, 'X', 2)
                                        if not isWin:
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
