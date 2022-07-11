import pygame

#### CLASSES ####

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.health = 100
        self.x = x
        self.y = y

#### MAIN CODE ####

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

player1 = Player("Angel", 0, SCREEN_HEIGHT/2)
player2 = Player("Damien", 950, SCREEN_HEIGHT/2)


# MAIN LOOP
run = True
while run:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Red Boi")
    screen.fill(BLACK)

    # CREATE PLAYERS
    player1.character = pygame.draw.rect(screen, RED, (player1.x, player1.y, 50, 50))
    player2.character = pygame.draw.rect(screen, BLUE, (player2.x, player2.y, 50, 50))

    pygame.display.update()
    
    # CHECK IF SHOULD CLOSE SCREEN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
            elif event.key == pygame.K_w:
                if player1.y > 0:
                    player1.y -= 50
            elif event.key == pygame.K_s:
                if player1.y < SCREEN_HEIGHT-50:
                    player1.y += 50
            elif event.key == pygame.K_UP:
                if player2.y > 0:
                    player2.y -= 50
            elif event.key == pygame.K_DOWN:
                if player2.y < SCREEN_HEIGHT-50:
                    player2.y += 50
