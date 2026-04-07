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


    # Create book LIST to initalize & store book objects
    all_books = [
        BookObjects.Book("Book1", "book1.png"),
        Book("Book2", "book2.png"),
        Book("Book3", "book3.png"),
        Book("Book4", "book4.png"),
        Book("Book5", "book5.png"),
    ]

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
        pygame.display.set_caption("Page 4: Guessing story Books")
        self.clock = pygame.time.Clock()
       
        # Background image
        self.background = pygame.image.load(os.path.join("ProjectImages", "kidTOYS_img.jpg"))
        self.background = pygame.transform.smoothscale(self.background, (WIDTH, HEIGHT)) #--> Image dimensions (x,y)

        # Loading Books images!!
        self.books = BookObjects.all_books #--> accessing images LIST "Books"
        
        # calling book positions functions
        self.book_positions() #--> call the positioning function

    # positioning the books PLACEMENT
    def book_positions(self):
        x = 80 
        y = 400

        # targetting book in list, 
        for book in self.books:
            book.rect.topleft = (x, y)

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
        # Make books clickable
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() #--> tracks the mouse's position

            for book in game.books: # targetting game var, which is assigned to BookGame() function
                if book.rect.collidepoint(mouse_pos):
                    print("You clicked:", book.answer) #--> collidepoint (checks if MOUSE CLICK is inside a rect) vs. colliderect (checks if rects are inside rects)

 #>>---------------------------------
# DRAW - background & books
#>>---------------------------------
# Draw background
game.screen.blit(game.background, (0, 0))

# Draw books
for book in game.books:
    game.screen.blit(book.image, book.rect)

pygame.display.update()
game.clock.tick(game.FPS)

pygame.quit()
