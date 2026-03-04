def page3():
    print("\n--- PAGE 3 ---")
    print("You enter a small library filled with dusty books.")
    print("[L] Look around")
    print("[B] Go back to Page 2")
    print("[Q] Quit")

    choice = input("Choose: ").lower()

    if choice == "l":
        return "page4"
    elif choice == "b":
        return "page2"
    elif choice == "q":
        return "quit"
    else:
        print("Invalid choice.")
        return "page3"
