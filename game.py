import os
import random

GRID_SIZE = 5

player_x = 0
player_y = 0
score = 0
collectible_x = 0
collectible_y = 0

def spawn_collectible():
    global collectible_x, collectible_y
    while True:
        x = random.randrange(GRID_SIZE)
        y = random.randrange(GRID_SIZE)
        if x != player_x or y != player_y:
            collectible_x = x
            collectible_y = y
            break

def draw_grid():
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            if x == player_x and y == player_y:
                row += "P "
            elif x == collectible_x and y == collectible_y:
                row += "C "
            else:
                row += ". "
        print(row)

def move(dx, dy):
    global player_x, player_y, score
    nx = player_x + dx
    ny = player_y + dy
    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
        player_x = nx
        player_y = ny
        if player_x == collectible_x and player_y == collectible_y:
            score += 1
            spawn_collectible()

def main_loop():
    global score
    print("Welcome to the Grid Game!")
    print("WASD to move, quit to exit\n")

    spawn_collectible()

    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"Score: {score}")
        draw_grid()

        if score >= 10:
            print("\nVictory! You reached 10 points!")
            break

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
