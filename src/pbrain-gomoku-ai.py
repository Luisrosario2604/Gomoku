#!/usr/bin/env python3.7
import random

sizeGame = 18
start = 0

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
        else :
            if board[y][x + i] == '-':
                white += 1
            break
    for i in range(1, 6):
        if x - i < 0:
            break
        elif board[y][x - i] == simbol and i <= rangeMax:
            size += 1
        else:
            if board[y][x - i] == '-':
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


def checkVerticalPoints(x, y, board, simbol, rangeMax):
    size = 0
    white = 0
    lastX = -1
    lastY = -1
    for i in range(1, 6):
        if y + i > sizeGame:
            break
        elif board[y + i][x] == simbol and i <= rangeMax:
            size += 1
            lastX = x
            lastY = y + i
        else:
            if board[y + i][x] != '-':
                break
    if lastX != -1 and lastY != -1 and lastY + 1 <= sizeGame and board[lastY + 1][x] == '-':
        white += 1
    if lastX == -1 and lastY == -1 and y + 1 <= sizeGame and board[y + 1][x] == '-':
        white += 1
    lastX = -1
    lastY = -1
    for i in range(1, 6):
        if y - i < 0:
            break
        elif board[y - i][x] == simbol and i <= rangeMax:
            size += 1
            lastX = x
            lastY = y - i
        else:
            if board[y - i][x] != '-':
                break
    if lastX != -1 and lastY != -1 and lastY - 1 >= 0 and board[lastY - 1][lastX] == '-':
        white += 1
    if lastX == -1 and lastY == -1 and y - 1 >= 0 and board[y - 1][x] == '-':
        white += 1
    return size, white


def checkHorizontalPoints(x, y, board, simbol, rangeMax):
    size = 0
    white = 0
    lastX = -1
    lastY = -1
    for i in range(1, 6):
        if x + i > sizeGame:
            break
        elif board[y][x + i] == simbol and i <= rangeMax:
            size += 1
            lastX = x + i
            lastY = y
        else :
            if board[y][x + i] != '-':
                break
    if lastX != -1 and lastY != -1 and lastX + 1 <= sizeGame and board[lastY][lastX + 1] == '-':
        white += 1
    if lastX == -1 and lastY == -1 and x + 1 <= sizeGame and board[y][x + 1] == '-':
        white += 1
    lastX = -1
    lastY = -1
    for i in range(1, 6):
        if x - i < 0:
            break
        elif board[y][x - i] == simbol and i <= rangeMax:
            size += 1
            lastX = x - i
            lastY = y
        else:
            if board[y][x - i] != '-':
                break
    if lastX != -1 and lastY != -1 and lastX - 1 >= 0 and board[lastY][lastX - 1] == '-':
        white += 1
    if lastX == -1 and lastY == -1 and x - 1 >= 0 and board[y][x - 1] == '-':
        white += 1
    return size, white


def checkSlashPoints(x, y, board, simbol, rangeMax):
    size = 0
    white = 0
    lastX = -1
    lastY = -1
    for i in range(1, 6):
        if x + i > sizeGame or y - i < 0:
            break
        elif board[y - i][x + i] == simbol and i <= rangeMax:
            size += 1
            lastX = x + i
            lastY = y - i
        else:
            if board[y - i][x + i] != '-':
                break
    if lastX != -1 and lastY != -1 and lastX + 1 <= sizeGame and lastY - 1 >= 0 and board[lastY - 1][lastX + 1] == '-':
        white += 1
    if lastX == -1 and lastY == -1 and x + 1 <= sizeGame and y - 1 >= 0 and board[y - 1][x + 1] == '-':
        white += 1
    lastX = -1
    lastY = -1
    for i in range(1, 6):
        if x - i < 0 or y + i > sizeGame:
            break
        elif board[y + i][x - i] == simbol and i <= rangeMax:
            size += 1
            lastX = x - i
            lastY = y + i
        else:
            if board[y + i][x - i] != '-':
                break
    if lastX != -1 and lastY != -1 and lastX - 1 >= 0 and lastY + 1 <= sizeGame and board[lastY + 1][lastX - 1] == '-':
        white += 1
    if lastX == -1 and lastY == -1 and x - 1 >= 0 and y + 1 <= sizeGame and board[y + 1][x - 1] == '-':
        white += 1
    return size, white


def checkBackSlashPoints(x, y, board, simbol, rangeMax):
    size = 0
    white = 0
    lastX = -1
    lastY = -1
    for i in range(1, 6):
        if x + i > sizeGame or y + i > sizeGame:
            break
        elif board[y + i][x + i] == simbol and i <= rangeMax:
            size += 1
            lastX = x + i
            lastY = y + i
        else:
            if board[y + i][x + i] == '-':
                break
    if lastX != -1 and lastY != -1 and lastX + 1 <= sizeGame and lastY + 1 <= sizeGame and board[lastY + 1][lastX + 1] == '-':
        white += 1
    if x == -1 and y == -1 and x + 1 <= sizeGame and y + 1 <= sizeGame and board[y + 1][x + 1] == '-':
        white += 1
    lastX = -1
    lastY = -1
    for i in range(1, 6):
        if x - i < 0 or y - i < 0:
            break
        elif board[y - i][x - i] == simbol and i <= rangeMax:
            size += 1
            lastX = x - i
            lastY = y - i
        else:
            if board[y - i][x - i] == '-':
                break
    if lastX != -1 and lastY != -1 and lastX - 1 >= 0 and lastY - 1 >= 0 and board[lastY - 1][lastX - 1] == '-':
        white += 1
    if lastX == -1 and lastY == -1 and x - 1 >= 0 and y - 1 >= 0 and board[y - 1][x - 1] == '-':
        white += 1
    return size, white


def getPoints(x, y, board, symbol, length):
    points = 0
    size, white = checkHorizontalPoints(x, y, board, symbol, length)
    if size > 0 and white != 0:
        points += size * 10
        if white >= 2:
            points += 25
    size, white = checkVerticalPoints(x, y, board, symbol, length)
    if size > 0 and white != 0:
        points += size * 10
        if white >= 2:
            points += 25
    size, white = checkSlashPoints(x, y, board, symbol, length)
    if size > 0 and white != 0:
        points += size * 10
        if white >= 2:
            points += 25
    size, white = checkBackSlashPoints(x, y, board, symbol, length)
    if size > 0 and white != 0:
        points += size * 10
        if white >= 2:
            points += 25
    return points


def checkBestPoints(board):
    xArray = []
    yArray = []
    pointsFinal = 0
    for x in range(sizeGame + 1):
        for y in range(sizeGame + 1):
            if board[y][x] == '-':
                points1 = getPoints(x, y, board, 'O', 5)
                if start == 1:
                    points1 *= 2
                a = points1
                points2 = getPoints(x, y, board, 'X', 4)
                if start == 0:
                    points2 *= 2
                points = points1 + points2
                if points >= pointsFinal:
                    if points > pointsFinal:
                        xArray = []
                        yArray = []
                    b = a
                    xArray.append(x)
                    yArray.append(y)
                    pointsFinal = points
    pick = preventGoodPlay(board, xArray, yArray)
    #print ("Debug POINTS TOTAL --> %d Attack: %d, Deff: %d SIZEE: %d" % (pointsFinal, b, pointsFinal - b, len(xArray)))
    return xArray[pick], yArray[pick]


def preventGoodPlay(board, xArray, yArray):
    #for i in range(len(xArray)):
        #print ("Debug ----------------------------")
        #print ("Debug X: %d - Y: %d  Size : %d " % (xArray[i], yArray[i], len(xArray)))
    return 0


def checkIfIsRange(board, simbol, rangeMax, free2sides):
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
                        possibility += 1
                size, white = checkVertical(x, y, board, simbol, rangeMax)
                if size >= rangeMax - 1:
                    if (free2sides == 1 and white == 2) or free2sides == 0:
                        possibility += 1
                size, white = checkSlash(x, y, board, simbol, rangeMax)
                if size >= rangeMax - 1:
                    if (free2sides == 1 and white == 2) or free2sides == 0:
                        possibility += 1
                size, white = checkBackSlash(x, y, board, simbol, rangeMax)
                if size >= rangeMax - 1:
                    if (free2sides == 1 and white == 2) or free2sides == 0:
                        possibility += 1
                if possibility > possibilityFinal:
                    xFinal, yFinal = x, y
                    possibilityFinal = possibility
                    isReturnFinal = True
    return xFinal, yFinal, isReturnFinal, possibilityFinal


def randomPick(board):
    x = random.randint(0, sizeGame)
    y = random.randint(0, sizeGame)
    while board[y][x] != '-':
        x = random.randint(0, sizeGame)
        y = random.randint(0, sizeGame)
    return x, y


def fillTheBoard(board):
    line = input().split(',')
    while line[0] != 'DONE':
        if int(line[2]) == 1:
            board[int(line[1])][int(line[0])] = 'O'
        else:
            board[int(line[1])][int(line[0])] = 'X'
        line = input().split(',')
    return board


def play():
    global start
    board = [['-']*(sizeGame + 1) for i in range(sizeGame + 1)]
    while 1:
        line = input().split(' ')
        if line[0] == 'BEGIN':
            start = 1
            board[4][4] = 'O'
            print("%d,%d" % (4, 4))
        elif line[0] == 'END':
            return 84
        elif line[0] == 'TURN' or line[0] == 'BOARD':
            if line[0] == 'BOARD':
                board = fillTheBoard(board)
            else:
                line = line[1].split(',')
                board[int(line[1])][int(line[0])] = 'X'

            x, y , isWin, possibility = checkIfIsRange(board, 'O', 5, 0)
            if not isWin:
                x, y, isLost, possibility = checkIfIsRange(board, 'X', 5, 0)
                if not isLost:
                    x, y, isWin, possibility = checkIfIsRange(board, 'O', 4, 1)
                    if not isWin:
                        x, y, isLost, possibility = checkIfIsRange(board, 'X', 4, 1)
                        if not isLost:
                            x, y, isWin, possibility = checkIfIsRange(board, 'O', 3, 1)
                            if not isWin or possibility < 2:
                                x, y, isLost, possibility = checkIfIsRange(board, 'X', 3, 1)
                                if not isLost or possibility < 2:
                                    x, y = checkBestPoints(board)
                                    #x, y = randomPick(board)
            board[y][x] = 'O'
            print("%d,%d" % (x, y))
        if line[0] == 'RESTART':
            break
    return 0

def start():
    global sizeGame
    start = input().split(' ')
    if len(start) == 2 and start[0] == 'START' and 5 <= int(start[1]) <= 20:
        print("OK")
        sizeGame = int(start[1]) - 1
        return 0
    else:
        print("ERROR")
    return 0


def main():
    tmp = 0
    if start() == 0:
        while tmp == 0:
            tmp = play()
    return 0



if __name__ == "__main__":
    main()
