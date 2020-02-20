import pygame
from network import Network
from battleship import game


def redrawWindow(screen, player1, player2):
    player1.refresh_screen(screen, player2)
    pygame.display.update()

def main():
    running = True
    n = Network()
    p1 = n.connection
    pygame.display.set_caption('Battleship')
    pygame.display.set_icon(pygame.image.load('images/battleshipicon.jpg'))
    screen_height = 500
    screen_width = 860
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    while running:
        clock.tick(10)
        p2 = n.send(p1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        p1.check_turn(p2)
        p1.get_hits(p2)
        p1.check_game_over(p2)
        if p1.player_ready == False and p2.gameover == True:
            pass
        else:
            p1.key_press(screen, p2)
        redrawWindow(screen, p1, p2)
main()
