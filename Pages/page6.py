# import BOOKSEARCH

def page6():
    print("=== PAGE 6 ===")
    print("Press A to go back to Page 5.")
    print("Press R to restart at page 1")
    #print("Press P to play [BOOKSEARCH - N/A])

    choice = input("Choose: ").lower()

    if choice == "a":
        return "page5"
    elif choice == "r": # Changed from "d" to "r" to keep "a" for going back to prvious page
        return "page1"
    #elif choice == "p":
        #BOOKSEARCH.run()
        #return "page6"
    else:
        print("Invalid choice.")
        return "page6"
