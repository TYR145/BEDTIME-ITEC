# MAIN PAGE -- "Scroll" through pages here w/ mini games (Available only in pages 2 & 3)

from Pages import page1
from Pages import page2
from Pages import page3
from Pages import page4
from Pages import page5
from Pages import page6

def main():
    current_page = "page1"

    while current_page != "quit":
        if current_page == "page1":
            current_page = page1.page1()
        elif current_page == "page2":
            current_page = page2.page2()
        elif current_page == "page3":
            current_page = page3.page3()
        elif current_page == "page4":
            current_page = page4.page4()
        elif current_page == "page5":
            current_page = page5.page5()
        elif current_page == "page6":
            current_page = page6.page6()
        else:
            print("Exiting page.")
            current_page = "quit"

    print("That's all for now!")
main()
