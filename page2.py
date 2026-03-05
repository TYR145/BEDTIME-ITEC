import Race

def page2():
    print("=== PAGE 2 ===")
    print("SECOND PAGE.")
    print("Press D to go to the next page.")
    print("Press A to go back to Page 1.")
    print("Press P to play the [Racing] Game")

    choice = input("Choose: ").lower()

    if choice == "d":
        return "page3"
    elif choice == "p":
        Race.run()
        return "page2"
    elif choice == "a":
        return "page1"
    else:
        print("Invalid choice.")
        return "page2"
