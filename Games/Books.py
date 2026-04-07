import pygame
import os
import random


#---------------------
# Book Objects
#---------------------
class BookObjects:
    
    class Book: # defining books properties
        def __init__(self, book_ans, book_cover):
            # 
            
            # defining & loading image
            self.image = pygame.image.load(os.path.join("ProjectImages", "BooksImages", book_cover)).convert_alpha() #--> .convert_alpha for a transparent PNG (yes)
            self.image = pygame.transform.smoothscale(self.image, (180, 180)) #--> helps with image clarity

            # Set & store the book to COMPARE to the answer later
            self.answer = book_ans

            # create a Rect for clickability
            self.rect = self.image.get_rect()


#>>---------------------------------
# INIT
#>>---------------------------------
class BookGame:
    def __init__(self):
        pygame.init()

      # Creating Game window
        WIDTH, HEIGHT = 1000, 680
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.FPS = 60
        pygame.display.set_caption("Game 4: Books Guessing")
        self.clock = pygame.time.Clock()
    
        # dEFINE Background image
        self.background = pygame.image.load(os.path.join("ProjectImages", "kidTOYS_img.jpeg"))
        self.background = pygame.transform.smoothscale(self.background, (WIDTH, HEIGHT)) #--> Image dimensions (x,y)
        
        # Create book LIST to initalize & store book objects
        all_books = [
            BookObjects.Book("Book1", "book1.png"),
            BookObjects.Book("Book2", "book2.png"),
            BookObjects.Book("Book3", "book3.png"),
            BookObjects.Book("Book4", "book4.png"),
            BookObjects.Book("Book5", "book5.png"),
        ]

        # Loading Books & Positioning them
        self.books = all_books  #--> accessing images LIST "Books" 
        self.book_positions() #--> call the positioning function

        #----------------------------------------------------------
        # Game Loic VARIABLES
        #----------------------------------------------------------
        # randomized answer
        self.correct_answer = random.choice(["Book1", "Book2", "Book3", "Book4", "Book5"])
        self.guesses_left = 3

        # Clue responses --> {} is a dictionary, applying a key-value pair (key = Book#, value = Clue)
        self.clues = {
            "Book1": "Clue: test#1",
            "Book2": "Clue: test #2",
            "Book3": "Clue: test#3",
            "Book4": "Clue: test#4",
            "Book5": "Clue: test#5",
        }



    # positioning the books PLACEMENT MANUALLY
    def book_positions(self):
        #--> targets the specific book by index & places it (x,y)

        self.books[0].rect.topleft = (150, 150)
        self.books[1].rect.topleft = (400, 150)
        self.books[2].rect.topleft = (650, 150)

        # Bottom row (shifted inward to fill the gaps)
        self.books[3].rect.topleft = (275, 400)
        self.books[4].rect.topleft = (525, 400)
#>>---------------------------------
# UPDATE - N/A (no movements)
#>>----------------------------
#---------------------------------
#  MAIN GAME LOOP
#---------------------------------
game = BookGame()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for book in game.books:
                if book.rect.collidepoint(mouse_pos):
                    if book.answer == game.correct_answer:
                        # Guess correctly FIRST TRY
                        if game.guesses_left == 3:
                            print(f"It's like you read his mind! {game.correct_answer} was correct!")
                       
                        # Guessing correctly after using a guess
                        else:
                            print(f"You found it! The right book was {game.correct_answer}!")
                        running = False   # <-- MUST be here, outside the inner if/else


                    # Wrong book clicked --> clues used
                    else:
                        game.guesses_left -= 1
                        print(game.clues.get(book.answer, "No clue available."))
                        # More than 0 guesses --> tells you have many guesses left
                        if game.guesses_left > 0:
                            print(f"Try again! {game.guesses_left} guesses left.")
                        # Running out of guesses
                        else:
                            print("No tries left. Game over.")
                            running = False   # <-- quit only when guesses hit 0

    #---------------------------------
    # DRAW - background & books
    #---------------------------------
    game.screen.blit(game.background, (0, 0))

    for book in game.books:
        game.screen.blit(book.image, book.rect)

    pygame.display.update()
    game.clock.tick(game.FPS)

pygame.quit()