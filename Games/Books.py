from tkinter import font

import pygame
import os
import random


#---------------------
# Book Objects
#---------------------
class BookObjects:
    
    class Book: # defining books properties
        def __init__(self, book_ans, book_cover):
            # defining & loading image (x,y) dimensions
            self.image = pygame.image.load(os.path.join("ProjectImages", "BooksImages", book_cover)).convert_alpha() #--> .convert_alpha for a transparent PNG (yes)
            self.image = pygame.transform.smoothscale(self.image, (180,250)) #--> helps with image clarity

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
    
        # dEFINE Background image (x,y) Dimensions
        self.background = pygame.image.load(os.path.join("ProjectImages", "kidTOYS_img.jpeg"))
        self.background = pygame.transform.smoothscale(self.background, (WIDTH, HEIGHT))

        # making text visible
        self.message = "" #--> makes anything attached to self.message a string
        self.font = pygame.font.SysFont(None, 50) #--> font sizing
    
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

        # making message's appear
        self.message = "Click to find which book the kid wants!"

        # Clue responses --> {} is a dictionary, applying a key-value pair (key = Book#, value = Clue)
        self.clues = {
            "Book1": "Clue: test#1",
            "Book2": "Clue: test #2",
            "Book3": "Clue: test#3",
            "Book4": "Clue: test#4",
            "Book5": "Clue: test#5",
        }

        def get_clue(self, wrong_book):
            if self.correct_answer == "Book1":
                return "The kid wants a book with a red cover."
            elif self.correct_answer == "Book2":
                return "The kid wants a book with animals."
            elif self.correct_answer == "Book3":
                return "The kid wants a book with a spaceship."
            elif self.correct_answer == "Book4":
                return "The kid wants a book with a princess."
            elif self.correct_answer == "Book5":
                return "The kid wants a book with a dragon."


    # Ending screen:
    def show_message(self, text_string, duration=2000):
        font = pygame.font.SysFont('Arial', 80)
        # Render the text
        text_surface = font.render(text_string, True, (255, 255, 255))

        # Center the text on the screen
        text_rect = text_surface.get_rect(center=(1000 // 2, 680 // 2))

        # Draw the final frame (background + books)
        self.screen.blit(self.background, (0, 0))
        for book in self.books:
            self.screen.blit(book.image, book.rect)

        # Draw the message centered
        self.screen.blit(text_surface, text_rect)

        pygame.display.update()
        pygame.time.delay(duration)


    # positioning the books PLACEMENT MANUALLY
    def book_positions(self):
        #--> targets the specific book by index & places it (x,y)
        self.books[0].rect.topleft = (150, 110)
        self.books[1].rect.topleft = (400, 110)
        self.books[2].rect.topleft = (650, 110)

        # Bottom row (shifted inward to fill the gaps)
        self.books[3].rect.topleft = (275, 410)
        self.books[4].rect.topleft = (525, 410)

#>>--------UPDATE (N/A: No game movement)-----------

#---------------------------------
#  MAIN GAME LOOP
#---------------------------------
game = BookGame()

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for book in game.books:
                if book.rect.collidepoint(mouse_pos):
                    if book.answer == game.correct_answer:
                        if game.guesses_left == 3:
<<<<<<< HEAD
                            game.message = f"WOW! {game.correct_answer} was correct!"
                        else:
                            game.message = f"{game.correct_answer} is the right book!"
                        game_over = True
                    else:
                        game.guesses_left -= 1
                        game.message = game.clues.get(book.answer, "No clue available.")
                        if game.guesses_left > 0:
                            game.message += f" {game.guesses_left} guesses left."
=======
                            game.message = f"It's like you read his mind! {game.correct_answer} was correct!"
                       
                        # Guessing correctly after using a guess
                        else:
                           game.message = f"You found it! The right book was {game.correct_answer}!"
                        running = False   # <-- MUST be here, outside the inner if/else


                    # Wrong book clicked --> clues used
                    else:
                        game.guesses_left -= 1
                        game.message = game.clues.get(book.answer, "No clue available.")
                        
                        # More than 0 guesses --> tells you have many guesses left
                        if game.guesses_left > 0:
                            game.message += f" Try again! {game.guesses_left} guesses left." 
                            #--> += adds "Try again!" to clues
                        
                        # Running out of guesses
>>>>>>> 509de5169f145e89adf2e77f4c814231e5514c19
                        else:
                            game.message = "No tries left. The kid is disappointed."
                            game_over = True

    # DRAW
    game.screen.blit(game.background, (0, 0))
    for book in game.books:
        game.screen.blit(book.image, book.rect)

<<<<<<< HEAD
    # Draw message during gameplay
    font = pygame.font.SysFont("Arial", 30)
    text_surface = font.render(game.message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(500, 40))
    game.screen.blit(text_surface, text_rect)

    # Final message
    if game_over:
        game.show_message(game.message)

    pygame.display.update()  
    game.clock.tick(game.FPS)
=======
   # drawing out the message (anything w/ game.mesge & colours it)
    text_surface = game.font.render(game.message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(1000 // 2, 55)) #--> text_surface creates image of text
                                                              #--> creates a rect of text we can move & center
    game.screen.blit(text_surface, text_rect) #--> draws the image & centers it
    pygame.display.update()

game.clock.tick(game.FPS)
>>>>>>> 509de5169f145e89adf2e77f4c814231e5514c19

pygame.quit()             
