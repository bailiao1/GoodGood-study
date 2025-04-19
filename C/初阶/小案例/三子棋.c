#define ROW 3
#define COL 3
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void initb(char b[ROW][COL])
{
    for (int i = 0; i < ROW; i++)
    {
        for (int j = 0; j < COL; j++)
        {
            b[i][j] = ' ';
        }
    }
}

void dpb(char b[ROW][COL])
{
    for (int i = 0; i < ROW; i++)
    {
        for (int j = 0; j < COL; j++)
        {
           printf(" %c ",b[i][j]);
           if (j < COL-1)
           printf("|");
        }
        printf("\n");
        if (i < ROW-1)
        printf("---|---|---\n");
    }
}

void player(char b[ROW][COL])
{   
    int x = 0;
    int y = 0;
    printf("请落子(x,y):\n");
    while(1)
    {
        if (scanf(" %d, %d",&x,&y) != 2) 
        {   
            printf("请遵守格式，使用(3,3)\n");
            while (getchar() != '\n')
            continue;
        }
        else if (x <= ROW && x > 0 && y <= COL && y > 0) 
        {   
            if (b[x-1][y-1] == ' ')
                {
                    b[x-1][y-1] = 'X';
                    break;
                }
            else {printf("坐标已被占用，重新输入\n");}
        }
        else {printf("坐标越界，请输入 1~%d 范围：\n", ROW);}
    }   
}

void ComputerMove(char board[ROW][COL])
{
    printf("电脑正在落子...\n");
    while (1)
    {
        int x = rand() % 3;
        int y = rand() % 3;
        if (board[x][y] == ' ')
        {
            board[x][y] = 'O';
            break;
        }
    }
}

char CheckWin(char board[ROW][COL])
{
    // 行
    for (int i = 0; i < ROW; i++)
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ')
            return board[i][0];

    // 列
    for (int j = 0; j < COL; j++)
        if (board[0][j] == board[1][j] && board[1][j] == board[2][j] && board[0][j] != ' ')
            return board[0][j];

    // 对角线
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ')
        return board[0][0];
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ')
        return board[0][2];

    // 是否平局（是否还有空格）
    for (int i = 0; i < ROW; i++)
        for (int j = 0; j < COL; j++)
            if (board[i][j] == ' ')
                return 'C'; // 继续

    return 'Q'; // 平局
}

void Game()
{
    char board[ROW][COL];
    char result = 0;

    initb(board);

    while (1)
    {
        dpb(board);
        player(board);
        result = CheckWin(board);
        if (result != 'C') break;

        ComputerMove(board);
        result = CheckWin(board);
        if (result != 'C') break;
    }

    dpb(board);
    if (result == 'X')
        printf("恭喜你赢了！\n");
    else if (result == 'O')
        printf("你输了，电脑赢了！\n");
    else
        printf("平局！\n");
}

void Menu()
{
    printf("*********************\n");
    printf("**** 1. play ********\n");
    printf("**** 0. exit ********\n");
    printf("*********************\n");
}

int main()
{
    srand((unsigned int)time(NULL));
    int input = 0;
    do
    {
        Menu();
        printf("请选择：");
        scanf("%d", &input);
        if (input == 1)
            Game();
        else if (input == 0)
            printf("退出游戏，再见！\n");
        else
            printf("选择无效，请重选！\n");
    } while (input);
    return 0;
}
