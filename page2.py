def page2():
    print("\n--- PAGE 2 ---")
    print("You walk forward and find a hallway.")
    print("[W] Continue forward")
    print("[B] Go back to Page 1")
    print("[R] Play Race mini-game")
    print("[Q] Quit")

    choice = input("Choose: ").lower()

    if choice == "w":
        return "page3"
    elif choice == "b":
        return "page1"
    elif choice == "r":
        return "race"
    elif choice == "q":
        return "quit"
    else:
        print("Invalid choice.")
        return "page2"
