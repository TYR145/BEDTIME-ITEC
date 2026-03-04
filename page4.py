import Maze

def page4():
    print("\n=== PAGE 4 ===")
    print("FOURTH PAGE.")
    print("Press A to go back to Page 3.")
    print("Press D to got to Page 5.")
    print("Press P to play [Maze] game")


    choice = input("Choose: ").lower()

    if choice == "a":
        return "page4"
    elif choice == "d":
        return "page3"
    elif choice == "p":
        Maze.run()
        return "page4"
    else:
        print("Invalid choice.")
        return "page4"
