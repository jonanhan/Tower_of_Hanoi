#! /usr/bin/python

# TOWER OF HANOI GAME

# =====================================================================================================================


header = "\n* The Towers of Hanoi Game! *\n\n" \
         "The rules are simple:\n" \
         "   Smaller discs can go on top of larger discs,\n" \
         "   but NOT visa versa.\n" \
         "   Move all the discs from A to C, in as few moves as possible.\n\n" \
         "This is your starting position, good luck!\n\n"

abc = [[" ", "          A          ", "          B          ", "          C          \n"]]
d = " "
t = " "
d0 = "         | |         "
d1 = "       (=|1|=)       "
d2 = "     (===|2|===)     "
d3 = "   (=====|3|=====)   "
d4 = " (=======|4|=======) "
win = 0
mov = 0

mat = [[1, d1, d0, d0],
       [2, d2, d0, d0],
       [3, d3, d0, d0],
       [4, d4, d0, d0]]

mat2 = [[1, 1000, 10, 20],
        [2, 20000, 30, 40],
        [3, 300000, 50, 60],
        [4, 4000000, 70, 80]]


# =====================================================================================================================


def index_2d(my_list, v):
    for n, x in enumerate(my_list):
        if v in x:
            return n, x.index(v)


def small():
    print("\nYou cannot move disc " + d + " to a smaller disc in tower " + t.upper() + ".\n\nTry again...\n\n")


def stuck():
    print("\nYou cannot move disc " + d + "!\n\nTry again...\n\n")


def in_tow():
    print("Disc " + d + " is already in tower " + t.upper() + ".\n\nPlease try again...\n")


def moved():
    print("You moved disc " + d + " to tower " + t.upper() + ".\nMoves: " + str(mov) + "\n\n")


def error():
    print("\n* Error...Error...Error...Error...Error *\n\n")


def in_val():
    print("\nInvalid input, use:\ndisc = 1, 2, 3 or 4\ntower = A/a, B/b, or C/c\n\nPlease try again...\n\n")


# =====================================================================================================================


for row in mat2:
    r = mat2.index(row)
    for col in row:
        ci = index_2d(mat2, col)
        c = ci[1]
        if c > 0:
            if mat2[r][c] == 1000:
                mat[r][c] = d1
            elif mat2[r][c] == 20000:
                mat[r][c] = d2
            elif mat2[r][c] == 300000:
                mat[r][c] = d3
            elif mat2[r][c] == 4000000:
                mat[r][c] = d4
            else:
                mat[r][c] = d0

print(header)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in abc]))
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mat]))

# =====================================================================================================================


while win != 1:
    print(" \n ")
    d = input("Move disc: ")
    t = input("To tower: ")

    # =================================================================================================================

    if d == "1" and t.upper() == "A":
        i = 1000
        j = 1
        ind = index_2d(mat2, i)
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 1000
            mov += 1
            moved()

        elif 20000 < sum2 < 20500 or \
                300000 < sum2 < 300500 or \
                4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 1000
            mov += 1
            moved()

        elif 320000 < sum2 < 320500 or \
                4300000 < sum2 < 4300500 or \
                4020000 < sum2 < 4020500:
            mat2[ind[0]][ind[1]] = mat2[1][j]
            mat2[1][j] = 1000
            mov += 1
            moved()

        elif 4320000 < sum2 < 4320500:
            mat2[ind[0]][ind[1]] = mat2[0][j]
            mat2[0][j] = 1000
            mov += 1
            moved()

        else:
            error()

    # -----------------------------------------------------------------------------------------------------------------

    elif d == "1" and t.upper() == "B":
        i = 1000
        j = 2
        ind = index_2d(mat2, i)
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 1000
            mov += 1
            moved()

        elif 20000 < sum2 < 20500 or \
                300000 < sum2 < 300500 or \
                4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 1000
            mov += 1
            moved()

        elif 320000 < sum2 < 320500 or \
                4300000 < sum2 < 4300500 or \
                4020000 < sum2 < 4020500:
            mat2[ind[0]][ind[1]] = mat2[1][j]
            mat2[1][j] = 1000
            mov += 1
            moved()

        elif 4320000 < sum2 < 4320500:
            mat2[ind[0]][ind[1]] = mat2[0][j]
            mat2[0][j] = 1000
            mov += 1
            moved()

        else:
            error()

    # -----------------------------------------------------------------------------------------------------------------

    elif d == "1" and t.upper() == "C":
        i = 1000
        j = 3
        ind = index_2d(mat2, i)
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 1000
            mov += 1
            moved()

        elif 20000 < sum2 < 20500 or \
                300000 < sum2 < 300500 or \
                4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 1000
            mov += 1
            moved()

        elif 320000 < sum2 < 320500 or \
                4300000 < sum2 < 4300500 or \
                4020000 < sum2 < 4020500:
            mat2[ind[0]][ind[1]] = mat2[1][j]
            mat2[1][j] = 1000
            mov += 1
            moved()

        elif 4320000 < sum2 < 4320500:
            mat2[ind[0]][ind[1]] = mat2[0][j]
            mat2[0][j] = 1000
            mov += 1
            moved()

        else:
            error()

    # =================================================================================================================

    elif d == "2" and t.upper() == "A":
        i = 20000
        j = 1
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 21000 < sum1 < 21500 or \
                321000 < sum1 < 321500 or \
                4021000 < sum1 < 4021500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                301000 < sum2 < 301500 or \
                4001000 < sum2 < 4001500 or \
                4301000 < sum2 < 4301500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 20000
            mov += 1
            moved()

        elif 300000 < sum2 < 300500 or \
                4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 20000
            mov += 1
            moved()

        elif 4300000 < sum2 < 4300500:
            mat2[ind[0]][ind[1]] = mat2[1][j]
            mat2[1][j] = 20000
            mov += 1
            moved()

        else:
            error()

    # -----------------------------------------------------------------------------------------------------------------

    elif d == "2" and t.upper() == "B":
        i = 20000
        j = 2
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 21000 < sum1 < 21500 or \
                321000 < sum1 < 321500 or \
                4021000 < sum1 < 4021500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                301000 < sum2 < 301500 or \
                4001000 < sum2 < 4001500 or \
                4301000 < sum2 < 4301500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 20000
            mov += 1
            moved()

        elif 300000 < sum2 < 300500 or \
                4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 20000
            mov += 1
            moved()

        elif 4300000 < sum2 < 4300500:
            mat2[ind[0]][ind[1]] = mat2[1][j]
            mat2[1][j] = 20000
            mov += 1
            moved()

        else:
            error()

    # -----------------------------------------------------------------------------------------------------------------

    elif d == "2" and t.upper() == "C":
        i = 20000
        j = 3
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 21000 < sum1 < 21500 or \
                321000 < sum1 < 321500 or \
                4021000 < sum1 < 4021500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                301000 < sum2 < 301500 or \
                4001000 < sum2 < 4001500 or \
                4301000 < sum2 < 4301500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 20000
            mov += 1
            moved()

        elif 300000 < sum2 < 300500 or \
                4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 20000
            mov += 1
            moved()

        elif 4300000 < sum2 < 4300500:
            mat2[ind[0]][ind[1]] = mat2[1][j]
            mat2[1][j] = 20000
            mov += 1
            moved()

        else:
            error()

    # =================================================================================================================

    elif d == "3" and t.upper() == "A":
        i = 300000
        j = 1
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 301000 < sum1 < 301500 or \
                320000 < sum1 < 320500 or \
                321000 < sum1 < 321500 or \
                4301000 < sum1 < 4301500 or \
                4320000 < sum1 < 4320500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                20000 < sum2 < 20500 or \
                21000 < sum2 < 21500 or \
                4020000 < sum2 < 4020500 or \
                4021000 < sum2 < 4021500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 300000
            mov += 1
            moved()

        elif 4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 300000
            mov += 1
            moved()

        else:
            error()

    # -----------------------------------------------------------------------------------------------------------------

    elif d == "3" and t.upper() == "B":
        i = 300000
        j = 2
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 301000 < sum1 < 301500 or \
                320000 < sum1 < 320500 or \
                321000 < sum1 < 321500 or \
                4301000 < sum1 < 4301500 or \
                4320000 < sum1 < 4320500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                20000 < sum2 < 20500 or \
                21000 < sum2 < 21500 or \
                4020000 < sum2 < 4020500 or \
                4021000 < sum2 < 4021500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 300000
            mov += 1
            moved()

        elif 4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 300000
            mov += 1
            moved()

        else:
            error()

    # -----------------------------------------------------------------------------------------------------------------

    elif d == "3" and t.upper() == "C":
        i = 300000
        j = 3
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 301000 < sum1 < 301500 or \
                320000 < sum1 < 320500 or \
                321000 < sum1 < 321500 or \
                4301000 < sum1 < 4301500 or \
                4320000 < sum1 < 4320500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                20000 < sum2 < 20500 or \
                21000 < sum2 < 21500 or \
                4020000 < sum2 < 4020500 or \
                4021000 < sum2 < 4021500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 300000
            mov += 1
            moved()

        elif 4000000 < sum2 < 4000500:
            mat2[ind[0]][ind[1]] = mat2[2][j]
            mat2[2][j] = 300000
            mov += 1
            moved()

        else:
            error()

    # =================================================================================================================

    elif d == "4" and t.upper() == "A":
        i = 4000000
        j = 1
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 4001000 < sum1 < 4001500 or \
                4020000 < sum1 < 4020500 or \
                4021000 < sum1 < 4021500 or \
                4300000 < sum1 < 4300500 or \
                4301000 < sum1 < 4301500 or \
                4320000 < sum1 < 4320500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                20000 < sum2 < 20500 or \
                21000 < sum2 < 21500 or \
                300000 < sum2 < 300500 or \
                301000 < sum2 < 301500 or \
                320000 < sum2 < 320500 or \
                321000 < sum2 < 321500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 4000000
            mov += 1
            moved()

        else:
            error()

    # -----------------------------------------------------------------------------------------------------------------

    elif d == "4" and t.upper() == "B":
        i = 4000000
        j = 2
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 4001000 < sum1 < 4001500 or \
                4020000 < sum1 < 4020500 or \
                4021000 < sum1 < 4021500 or \
                4300000 < sum1 < 4300500 or \
                4301000 < sum1 < 4301500 or \
                4320000 < sum1 < 4320500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                20000 < sum2 < 20500 or \
                21000 < sum2 < 21500 or \
                300000 < sum2 < 300500 or \
                301000 < sum2 < 301500 or \
                320000 < sum2 < 320500 or \
                321000 < sum2 < 321500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 4000000
            mov += 1
            moved()

        else:
            error()

    # -----------------------------------------------------------------------------------------------------------------

    elif d == "4" and t.upper() == "C":
        i = 4000000
        j = 3
        ind = index_2d(mat2, i)
        sum1 = mat2[0][ind[1]] + mat2[1][ind[1]] + mat2[2][ind[1]] + mat2[3][ind[1]]
        sum2 = mat2[0][j] + mat2[1][j] + mat2[2][j] + mat2[3][j]

        if 4001000 < sum1 < 4001500 or \
                4020000 < sum1 < 4020500 or \
                4021000 < sum1 < 4021500 or \
                4300000 < sum1 < 4300500 or \
                4301000 < sum1 < 4301500 or \
                4320000 < sum1 < 4320500 or \
                4321000 == sum1:
            stuck()

        elif 1000 < sum2 < 1500 or \
                20000 < sum2 < 20500 or \
                21000 < sum2 < 21500 or \
                300000 < sum2 < 300500 or \
                301000 < sum2 < 301500 or \
                320000 < sum2 < 320500 or \
                321000 < sum2 < 321500:
            small()

        elif ind[1] == j:
            in_tow()

        elif sum2 < 500:
            mat2[ind[0]][ind[1]] = mat2[3][j]
            mat2[3][j] = 4000000
            mov += 1
            moved()

        else:
            error()

    elif d == "all" and t.upper() == "C":
        print("\n\nYou CHEATED, but if no one saw you do it you still win:\n\n")

        mat = [[1, d0, d0, d1],
               [2, d0, d0, d2],
               [3, d0, d0, d3],
               [4, d0, d0, d4]]

        mat2 = [[1, 10, 20, 1000],
                [2, 30, 40, 20000],
                [3, 50, 60, 300000],
                [4, 70, 80, 4000000]]
    else:
        in_val()

    # =================================================================================================================

    for row in mat2:
        r = mat2.index(row)
        for col in row:
            ci = index_2d(mat2, col)
            c = ci[1]
            if c > 0:
                if mat2[r][c] == 1000:
                    mat[r][c] = d1
                elif mat2[r][c] == 20000:
                    mat[r][c] = d2
                elif mat2[r][c] == 300000:
                    mat[r][c] = d3
                elif mat2[r][c] == 4000000:
                    mat[r][c] = d4
                else:
                    mat[r][c] = d0

    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in abc]))
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mat]))

    # =================================================================================================================

    if mat2[0][3] + mat2[1][3] + mat2[2][3] + mat2[3][3] == 4321000:
        print("\n\nCongratulations, you WIN!!!\n\nYou finished in " + str(mov) + " moves.\n")
        print("Minimum number of moves possible for 4 discs is 15.\n"
              "You used " + str(mov - 15) + " move(s) more.\nTry again if you want to improve you're game.\n")
        win = 1
