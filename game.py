import os

GRID_SIZE = 5

player_x = 0
player_y = 0

def draw_grid():
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            if x == player_x and y == player_y:
                row += "P "
            else:
                row += ". "
        print(row)

def move(dx, dy):
    global player_x, player_y
    nx = player_x + dx
    ny = player_y + dy
    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
        player_x = nx
        player_y = ny

def main_loop():
    print("Welcome to the Grid Game!")
    print("WASD to move, quit to exit\n")

    while True:
        os.system("clear" if os.name == "posix" else "cls")
        draw_grid()
        cmd = input("\n> ").strip().lower()

        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "w":
            move(0, -1)
        elif cmd == "s":
            move(0, 1)
        elif cmd == "a":
            move(-1, 0)
        elif cmd == "d":
            move(1, 0)
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main_loop()
