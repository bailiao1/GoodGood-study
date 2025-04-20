import random


def chu(qi):
    for i in range(len(qi)):
        for j in range(len(qi[0])):
            print(f" {qi[i][j]} ", end='')
            if j < len(qi[0]) - 1:
                print("|", end='')
        print()
        if i < len(qi) - 1:
            print("---|---|---")


def pla(qi):
    while True:
        x, y = map(int, input("请落子（格式：1,3）：").split(","))
        if 1 <= x <= 3 and 1 <= y <= 3:
            if qi[x - 1][y - 1] == " ":
                qi[x - 1][y - 1] = "O"
                break
            else:
                print("位置已被占用")
        else:
            print("坐标越界")


def renji(qi):
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if qi[x][y] == " ":
            qi[x][y] = "X"
            break


def cheak(qi):
    # 判断斜线
    if (qi[0][0] == qi[1][1] == qi[2][2]) and qi[0][0] != " ":
        return qi[0][0]
    if (qi[0][2] == qi[1][1] == qi[2][0]) and qi[0][2] != " ":
        return qi[0][2]

    # 判断横竖
    for i in range(3):
        if qi[i][0] == qi[i][1] == qi[i][2] and qi[i][0] != " ":
            return qi[i][0]
        if qi[0][i] == qi[1][i] == qi[2][i] and qi[0][i] != " ":
            return qi[0][i]

    # 判断平局（是否还有空格）
    for row in qi:
        if " " in row:
            return "C"

    return "Pin"


def game():
    q = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        chu(q)
        pla(q)
        p = cheak(q)
        if p == "O":
            chu(q)
            print("玩家胜")
            break
        elif p == "Pin":
            chu(q)
            print("平局")
            break

        renji(q)
        p = cheak(q)
        if p == "X":
            chu(q)
            print("电脑胜")
            break
        elif p == "Pin":
            chu(q)
            print("平局")
            break


while True:
    game()
    a = input("再来一局？输入1继续，其他键退出：")
    if a != "1":
        break
