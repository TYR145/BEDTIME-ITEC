def page1():
    print("\n--- PAGE 1 ---")
    print("You wake up in a dark room.")
    print("[W] Go forward")
    print("[A] Go left")
    print("[D] Go right")
    print("[M] Play Maze mini-game")
    print("[Q] Quit")

    choice = input("Choose: ").lower()

    if choice == "w":
        return "page2"
    elif choice == "a":
        return "page3"
    elif choice == "d":
        return "page4"
    elif choice == "m":
        return "maze"
    elif choice == "q":
        return "quit"
    else:
        print("Invalid choice.")
        return "page1"
