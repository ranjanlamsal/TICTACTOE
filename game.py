
game_board = { '1': '   ', '2': '   ', '3': '   ',
               '4': '   ', '5': '   ', '6': '   ',
               '7': '   ', '8': '   ', '9': '   '}

board_space = []
for key in game_board:
    board_space.append(key)


def printBoard(board):
    print('\t'+ board['7'] + '|' + board['8'] + '|' + board['9'])
    print('\t'+ '---+---+---')
    print('\t'+ board['4'] + '|' + board['5'] + '|' + board['6'])
    print('\t'+ '---+---+---')
    print('\t'+ board['1'] + '|' + board['2'] + '|' + board['3'])


def main_game():
    turn = ''
    while True:
        # try:
        choice = input("Player one select your choice (O/X)?")
        if choice.capitalize() == 'X':
            turn = 'X'
            break
        elif choice.capitalize() == 'O':
            turn = 'O'
            break
        else:
            print("Invalid input")
            continue
        # except:
        #     print("Invalid input!!!!!!!!!")
        #     continue
    count = 0

    for i in range(10):
        # global turn
        printBoard(game_board)
        print("It's your turn, Player( " + turn + "). Move to which place?")

        move = input()
        try:
            if game_board[move] == '   ':
                game_board[move] = f" {turn} "
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue
        except:
            print("Invalid input!!!!")
            continue

        if count >= 5:
            if game_board['7'] == game_board['8'] == game_board['9'] != '   ':  # across the top
                printBoard(game_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif game_board['4'] == game_board['5'] == game_board['6'] != '   ':  # across the middle
                printBoard(game_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif game_board['1'] == game_board['2'] == game_board['3'] != '   ':  # across the bottom
                printBoard(game_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif game_board['1'] == game_board['4'] == game_board['7'] != '   ':  # down the left side
                printBoard(game_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif game_board['2'] == game_board['5'] == game_board['8'] != '   ':  # down the middle
                printBoard(game_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif game_board['3'] == game_board['6'] == game_board['9'] != '   ':  # down the right side
                printBoard(game_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif game_board['7'] == game_board['5'] == game_board['3'] != '   ':  # diagonal
                printBoard(game_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif game_board['1'] == game_board['5'] == game_board['9'] != '   ':  # diagonal
                printBoard(game_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("Tie!!!!")
            break

            #changing player after every move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    play_again = input("Do want to play Again?(y/n)")
    if play_again.capitalize() == "Y":
        for key in board_space:
            game_board[key] = "   "

        main_game()


if __name__ == "__main__":
    main_game()