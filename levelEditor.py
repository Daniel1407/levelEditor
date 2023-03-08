import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

#ventana
SCREEN_WIDTH = 540
SCREEN_HEIGTH = 400
LOWER_MARGIN = 200
SIDE_MARGIN = 100

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGTH + LOWER_MARGIN))
pygame.display.set_caption('Level editor')


#variables
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGTH // ROWS

scroll_up = False
scroll_down = False
scroll = 0
scroll_speed = 1

#colores
GREEN = (144, 201, 120)
RED = (255, 255, 255)
WHITE = (200, 25, 25)

#cargar imagenes
background = pygame.image.load('img\\background\\bg.png').convert_alpha()
particles = pygame.image.load('img\\background\\bg1.png').convert_alpha()

#dibujar background
def draw_bg():
    screen.fill(GREEN)
    heigth = background.get_height()
    for x in range(10):
        screen.blit(background, (0, -(x * heigth) - scroll * 0.5))
        screen.blit(particles, (0, -(x * heigth) - scroll * 0.5))

#dibujar cuadricula
def draw_grid():
    #lineas verticales
    for c in range(MAX_COLS+1):
        pygame.draw.line(screen, WHITE, ())

run = True

while run:

    clock.tick(FPS)

    draw_bg()

    #scroll
    if scroll_up == True:
        scroll -= 5 * scroll_speed
    if scroll_down == True and scroll < 0:
        scroll += 5 * scroll_speed


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #teclas pulsadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                scroll_up = True
            if event.key == pygame.K_DOWN:
                scroll_down = True
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                scroll_up = False
            if event.key == pygame.K_DOWN:
                scroll_down = False
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 1

            

    pygame.display.update()

pygame.quit()