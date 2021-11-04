"""
Name: Joanna Godawa
lab10.py
"""


def build_board():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]


def display_board(board):
    fill = ""
    print(" __________________________")
    for i in range(len(board)):
        fill = get_fill(board[i])
        print(" | ", end="")
        print("[" + str(i + 1) + "]", fill, end="")
        if (i + 1) % 3 == 0:
            print(" |")
    print(" __________________________")


def get_fill(num):
    if num == 0:
        return " "
    if num == 1:
        return "X"
    if num == 2:
        return "O"


def fill_spot(board, pos, char):
    pos -= 1
    if can_fill(board, pos):
        board[pos] = char


def can_fill(board, pos):
    if board[pos] == 0:
        return True
    else:
        return False


def game_over(board):
    if (board[0] == board[1] == board[2]) and (board[0] != 0):
        return 1
    elif (board[3] == board[4] == board[5]) and (board[3] != 0):
        return 1
    elif (board[6] == board[7] == board[8]) and (board[6] != 0):
        return 1
    elif (board[0] == board[4] == board[8]) and (board[0] != 0):
        return 1
    elif (board[2] == board[4] == board[6]) and (board[2] != 0):
        return 1
    elif (board[0] == board[3] == board[6]) and (board[0] != 0):
        return 1
    elif (board[1] == board[4] == board[7]) and (board[1] != 0):
        return 1
    elif (board[2] == board[5] == board[8]) and (board[2] != 0):
        return 1

    for i in board:
        if i == 0:
            return 0
    return 2


def main():
    board = build_board()
    display_board(board)
    turns = 1
    is_running = 0
    while is_running != 1 and is_running != 2:
        player = (turns % 2)
        if player == 0:
            player = 2
        prompt = "Player " + str(player) + ", enter a position (1 - 9) to fill: "
        spot_to_fill = eval(input(prompt))
        fill_spot(board, spot_to_fill, player)
        display_board(board)
        turns += 1
        is_running = game_over(board)
        if is_running == 1:
            print("Player", player, "wins!")
            break
        if is_running == 2:
            print("Stalemate: no more moves!")

    pass


main()
