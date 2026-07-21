import os
import random

GRID_SIZE = 5


def reset_game():
    global player_x, player_y, score, collectible_x, collectible_y, hazard_x, hazard_y
    player_x = 0
    player_y = 0
    score = 0
    collectible_x = 0
    collectible_y = 0
    hazard_x = 0
    hazard_y = 0
    spawn_collectible()
    spawn_hazard()


def spawn_collectible():
    global collectible_x, collectible_y
    while True:
        x = random.randrange(GRID_SIZE)
        y = random.randrange(GRID_SIZE)
        if x != player_x or y != player_y:
            collectible_x = x
            collectible_y = y
            break


def spawn_hazard():
    global hazard_x, hazard_y
    while True:
        x = random.randrange(GRID_SIZE)
        y = random.randrange(GRID_SIZE)
        if (x != player_x or y != player_y) and (x != collectible_x or y != collectible_y):
            hazard_x = x
            hazard_y = y
            break


def draw_grid():
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            if x == player_x and y == player_y:
                row += "P "
            elif x == hazard_x and y == hazard_y:
                row += "H "
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
        if player_x == hazard_x and player_y == hazard_y:
            return "game_over"
        if player_x == collectible_x and player_y == collectible_y:
            score += 1
            spawn_collectible()
    return None


def main_loop():
    print("Welcome to the Grid Game!")
    print("WASD to move, quit to exit\n")

    reset_game()

    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"Score: {score}")
        draw_grid()

        if score >= 10:
            print("\nVictory! You reached 10 points!")
            again = input("Play again? (y/n) ").strip().lower()
            if again == "y":
                reset_game()
                continue
            else:
                break

        cmd = input("\n> ").strip().lower()

        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "w":
            result = move(0, -1)
            if result == "game_over":
                print("Game Over!")
                again = input("Play again? (y/n) ").strip().lower()
                if again == "y":
                    reset_game()
                    continue
                else:
                    break
        elif cmd == "s":
            result = move(0, 1)
            if result == "game_over":
                print("Game Over!")
                again = input("Play again? (y/n) ").strip().lower()
                if again == "y":
                    reset_game()
                    continue
                else:
                    break
        elif cmd == "a":
            result = move(-1, 0)
            if result == "game_over":
                print("Game Over!")
                again = input("Play again? (y/n) ").strip().lower()
                if again == "y":
                    reset_game()
                    continue
                else:
                    break
        elif cmd == "d":
            result = move(1, 0)
            if result == "game_over":
                print("Game Over!")
                again = input("Play again? (y/n) ").strip().lower()
                if again == "y":
                    reset_game()
                    continue
                else:
                    break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main_loop()
