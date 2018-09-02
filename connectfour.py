import random
def p(array):
    string = ""
    for row in array:
        for column in row:
            string += str(column)
        string += "\n"
    string += "1,2,3,4,5,6,7"
    print(string)
def isFilled(array):
    b = True
    for row in array:
        for column in row:
            if str(column) == "_.":
                b = False
    return b
def vertical(array):
    for col in range(0, 6):
        for row in range(0, 3):
            if (array[row][col] == array[row + 1][col] == array[row + 2][col] == array[row + 3][col]) and (array[row][col] != "_."):
                return array[row][col]
    return "_."
def horizontal(array):
    for row in range(0, 6):
        for col in range(0, 4):
            if (array[row][col] == array[row][col + 1] == array[row][col + 2] == array[row][col + 3]) and (array[row][col] != "_."):
                return array[row][col]
    return "_."
def downRight(array):
    for row in range(0, 3):
        for col in range(0, 4):
            if (array[row][col] == array[row + 1][col + 1] == array[row + 2][col + 2] == array[row + 3][col + 3]) and (array[row][col] != "_."):
                return array[row][col]
    return "_."
def upRight(array):
    for row in range(5, 2, -1):
        for col in range(0, 4):
            if (array[row][col] == array[row - 1][col + 1] == array[row - 2][col + 2] == array[row - 3][col + 3]) and (array[row][col] != "_."):
                return array[row][col]
    return "_."
def hasWon(array):
    if horizontal(array) != "_.":
        return horizontal(array)
    else:
        if vertical(array) != "_.":
            return vertical(array)
        else:
            if downRight(array) != "_.":
                return downRight(array)
            else:
                return upRight(array)
def canDrop(array, column):
    return column >= 0 and column < 7 and array[0][column] == "_."
def drop(array, column, color):
    index = 5
    while(index >= 0):
        if array[index][column] == "_.":
            array[index][column] = str(color) + "."
            break
        else:
            index -= 1
def computerTurn(array, color):
    hasDropped = False
    r = -1
    c = -1
    otherR = -1
    otherC = -1
    t = False
    for row in range(0, 6):
        for col in range(0, 5):
            if (array[row][col] == array[row][col + 1] == array[row][col + 2]) and (array[row][col] != "_."):
                if row < 5:
                    if t is False and col < 4 and array[row][col + 3] == "_." and array[row + 1][col + 3] != "_.":
                        r = row
                        c = col
                        t = True
                    else:
                        if t is False and col > 0 and array[row][col - 1] == "_." and array[row + 1][col - 1] != "_.":
                            r = row
                            c = col
                            t = True
                else:
                    if t is False and col < 4 and array[row][col + 3] == "_.":
                        r = row
                        c = col
                        t = True
                    else:
                        if t is False and col > 0 and array[row][col - 1] == "_.":
                            r = row
                            c = col
                            t = True
            else:
                if col != 4:
                    if (array[row][col] == array[row][col + 2] == array[row][col + 3]) and array[row][col + 1] == "_." and array[row][col] != "_.":
                        otherR = row
                        otherC = col + 1
                    else:
                        if (array[row][col] == array[row][col + 1] == array[row][col + 3]) and array[row][col + 2] == "_." and array[row][col] != "_.":
                            otherR = row
                            otherC = col + 2
    if r >= 0:
        print("HI")
        if c != 0 and canDrop(array, c - 1) is True and array[r][c - 1] == "_.":
            if r < 5:
                print("YES")
                if array[r + 1][c - 1] != "_.":
                    drop(array, c - 1, "Y")
                    hasDropped = True
            else:
                drop(array, c - 1, "Y")
                hasDropped = True
        else:
            if c != 4 and canDrop(array, c + 3) is True and array[r][c + 3] == "_.":
                if r < 5:
                    if array[r + 1][c + 3] != "_.":
                        drop(array, c + 3, "Y")
                        hasDropped = True
                else:
                    drop(array, c + 3, "Y")
                    hasDropped = True
    if otherR >= 0 and hasDropped is False:
        if canDrop(array, otherC) is True and array[otherR][otherC] == "_.":
            if otherR < 5:
                if array[otherR + 1][otherC] != "_.":
                    drop(array, otherC, "Y")
                    hasDropped = True
            else:
                drop(array, otherC, "Y")
                hasDropped = True
    r = -1
    c = -1
    if hasDropped is False:
        for col in range(0, 6):
            for row in range(0, 4):
                if (array[row][col] == array[row + 1][col] == array[row + 2][col]) and (array[row][col] != "_."):
                    r = row
                    c = col
        if r >= 0:
            if canDrop(array, c) is True and array[r - 1][c] == "_.":
                drop(array, c, "Y")
                hasDropped = True
    r = -1
    c = -1
    otherR = -1
    otherC = -1
    t = False

    if hasDropped is False:
        for row in range(0, 4):
            for col in range(0, 5):
                if (array[row][col] == array[row + 1][col + 1] == array[row + 2][col + 2]) and (array[row][col] != "_."):
                    #add redundancy
                    r = row
                    c = col
                else:
                    if row != 3 and col != 4:
                        if (array[row][col] == array[row + 1][col + 1] == array[row + 3][col + 3]) and array[row + 2][col + 2] == "_." and array[row][col] != "_.":
                            otherR = row + 2
                            otherC = col + 2
                        else:
                            if (array[row][col] == array[row + 2][col + 2] == array[row + 3][col + 3]) and array[row + 1][col + 1] == "_." and array[row][col] != "_.":
                                otherR = row + 1
                                otherC = col + 1
        if r >= 0:
            if c != 0 and r != 0 and canDrop(array, c - 1) is True and array[r - 1][c - 1] == "_.":
                if array[r][c - 1] != "_.":
                    drop(array, c - 1, "Y")
                    hasDropped = True
            else:
                if c != 4 and r < 3 and canDrop(array, c + 3) is True and array[r + 3][c + 3] == "_.":
                    if r < 2 and array[r + 4][c + 3] != "_.":
                        drop(array, c + 3, "Y")
                        hasDropped = True
                    else:
                        drop(array, c + 3, "Y")
                        hasDropped = True
        if otherR >= 0 and hasDropped is False:
            if canDrop(array, otherC) is True and array[otherR][otherC] == "_.":
                if array[otherR + 1][otherC] != "_.":
                    drop(array, otherC, "Y")
                    hasDropped = True
    r = -1
    c = -1
    otherR = -1
    otherC = -1
    if hasDropped is False:
        for row in range(5, 1, -1):
            for col in range(0, 5):
                if (array[row][col] == array[row - 1][col + 1] == array[row - 2][col + 2]) and (array[row][col] != "_."):
                    r = row
                    c = col
                else:
                    if row != 2 and col != 4:
                        if (array[row][col] == array[row - 1][col + 1] == array[row - 3][col + 3]) and array[row - 2][col + 2] == "_." and array[row][col] != "_.":
                            otherR = row - 2
                            otherC = col + 2
                        else:
                            if (array[row][col] == array[row - 2][col + 2] == array[row - 3][col + 3]) and array[row - 1][col + 1] == "_." and array[row][col] != "_.":
                                otherR = row - 1
                                otherC = col + 1
        if r >= 0:
            if c != 0 and r < 5 and canDrop(array, c - 1) is True and array[r + 1][c - 1] == "_.":
                if r < 4 and array[r + 2][c - 1] != "_.":
                    drop(array, c - 1, "Y")
                    hasDropped = True
                else:
                    drop(array, c - 1, "Y")
                    hasDropped = True
            else:
                if r > 2 and c != 4 and canDrop(array, c + 3) is True and array[r - 3][c + 3] == "_.":
                    if array[r - 2][c + 3]:
                        drop(array, c + 3, "Y")
                        hasDropped = True
        if otherR >= 0 and hasDropped is False:
            if canDrop(array, otherC) is True and array[otherR, otherC] == "_.":
                if array[otherR + 1][otherC] != "_.":
                    drop(array, otherC, "Y")
                    hasDropped = True
    over = 20
    if hasDropped is False:
        index = random.randint(0, 6)
        while hasDropped is False and over > 0:
            if canDrop(array, index) is True:
                a = []
                for i in range(0, len(array)):
                    a.append(array[i][:])
                drop(a, index, "Y")
                drop(a, index, "R")
                if hasWon(a) != "R.":
                    drop(array, index, "Y")
                    hasDropped = True
            else:
                index = random.randint(0, 6)
            over -= 1
        if hasDropped is False:
            while hasDropped is False:
                if canDrop(array, index) is True:
                    drop(array, index, "Y")
                    hasDropped = True
print("Let's play Connect Four!")
array = []
for x in range(0, 6):
    array.append(["_."] * 7)
p(array)
while isFilled(array) is False and hasWon(array) == "_.":
    print("Enter a number to drop the red piece.")
    number = int(input())
    if canDrop(array, number - 1) is False:
        while canDrop(array, number - 1) is False:
            print("Enter another legal position.\nSorry, the previous position was full.")
            number = int(input())
    drop(array, number - 1, "R")
    p(array)
    if hasWon(array) == "_.":
        print("My turn now...")
        computerTurn(array, "Y")
        p(array)
if hasWon(array) == "Y.":
    print("Sorry. I won. Too bad...")
if hasWon(array) == "R.":
    print("Wow, I underestimated you! GG")
if isFilled(array) is True:
    print("Oops, no more space. Oh well. It's a tie!")
