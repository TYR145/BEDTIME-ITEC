from Games import Maze

def page3():
    print("=== PAGE 3 ===")
    print("Press D to go to Page 4.")
    print("Press A to go back to Page 2.")
    print("Press P to play [Maze] game --> check hotbar for Python window")

    choice = input("Choose: ").lower()

    if choice == "d":
        return "page4"
    elif choice == "a":
        return "page2"
    elif choice == "p":
        Maze.run()
        return "page3"
    else:
        print("Invalid choice.")
        return "page3"
