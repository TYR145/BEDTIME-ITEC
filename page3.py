def page3():
    print("\n=== PAGE 3 ===")
    print("THIRD PAGE.")
    print("Press A to go back to Page 2.")
    print("Press D to go to Page 4.")

    choice = input("Choose: ").lower()

    if choice == "a":
        return "page3"
    elif choice == "d":
        return "page1"
    else:
        print("Invalid choice.")
        return "page4"
