gameField = {x: "_" for x in range(1, 10)}


def draw_field():
    print("□ --- --- □")
    print(f"|  {gameField[1]} {gameField[2]} {gameField[3]}  |")
    print(f"|  {gameField[4]} {gameField[5]} {gameField[6]}  |")
    print(f"|  {gameField[7]} {gameField[8]} {gameField[9]}  |")
    print("□ --- --- □")


def is_player_won(pl_char: str) -> bool:
    for a in range(0, 3):
        if (pl_char == gameField[a*3+1]) and (pl_char == gameField[a*3+2]) and (pl_char == gameField[a*3+3]):
            return True
        if (pl_char == gameField[(1+a)]) and (pl_char == gameField[(1+a)+3]) and (pl_char == gameField[(1+a)+6]):
            return True
    if (pl_char == gameField[1]) and (pl_char == gameField[5]) and (pl_char == gameField[9]):
        return True
    if (pl_char == gameField[3]) and (pl_char == gameField[5]) and (pl_char == gameField[7]):
        return True
    return False


def get_game_state() -> str:
    if is_player_won("X") and is_player_won("O"):
        return "Impossible"
    playerxcount = 0
    playernullcount = 0
    for a in gameField:
        if a == "X":
            playerxcount += 1
        if a == "O":
            playernullcount += 1
    if playerxcount - playernullcount > 1 or playernullcount - playerxcount > 1:
        return "Impossible"

    if is_player_won("X"):
        return "X wins!"
    if is_player_won("O"):
        return "O wins!"

    if "_" in gameField.values():
        return "Game not finished"
    else:
        return "Draw"


def do_rest()-> bool:
    print()
    print("...Restart? (Yes/...)")
    if str(input(">")) != "Yes":
      return True
    global gameField
    gameField = {x: "_" for x in range(1, 10)}
    return False


# Game cycle
playersymb  = "X"
while True:
    draw_field()
    gameState = get_game_state()
    print(gameState)
    if gameState != "Game not finished":
        if do_rest():
            break
        else:
            continue

    while True:
        command = input(">").split()
        cont = False
        for a in command:
            if not a.isnumeric():
                print("You should enter numbers!")
                cont = True
                break
        if cont:
            continue
        command[0] = int(command[0])
        command[1] = int(command[1])

        if len(command) < 2:
            print("Two numbers. Two. Row and column. Потому что мне лень это прописывать, и в тз вообще нет такого")
            continue

        if command[0] > 3 or command[0] < 1:
            print("Coordinates should be from 1 to 3!")
            continue
        if command[1] > 3 or command[1] < 1:
            print("Coordinates should be from 1 to 3!")
            continue

        if gameField[((command[0]-1) * 3) + command[1]] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        gameField[((command[0] - 1) * 3) + command[1]] = playersymb
        if playersymb == "X":
            playersymb = "O"
        else:
            playersymb = "X"
        break


