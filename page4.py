def page4():
    print("\n--- PAGE 4 ---")
    print("You find a locked door with strange symbols.")
    print("[T] Try to open it")
    print("[B] Go back to Page 3")
    print("[Q] Quit")

    choice = input("Choose: ").lower()

    if choice == "t":
        print("The door won't budge.")
        return "page4"
    elif choice == "b":
        return "page3"
    elif choice == "q":
        return "quit"
    else:
        print("Invalid choice.")
        return "page4"
