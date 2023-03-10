import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

#ventana
SCREEN_WIDTH = 400
SCREEN_HEIGTH = 600
SIDE_MARGIN = 200

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGTH))
pygame.display.set_caption('Level editor')


#variables
COLS = 16
MAX_ROWS = 150
TILE_SIZE = SCREEN_WIDTH // COLS

scroll_up = False
scroll_down = False
scroll = 0
scroll_speed = 1

#colores
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)

#cargar imagenes
background = pygame.image.load('img/background/bg.png').convert_alpha()
particles = pygame.image.load('img/background/bg1.png').convert_alpha()

#dibujar background
def draw_bg():
    screen.fill(GREEN)
    heigth = background.get_height()
    for x in range(10):
        screen.blit(background, (0, -(x * heigth) - scroll * 0.5))
        screen.blit(particles, (0, -(x * heigth) - scroll * 0.5))

#dibujar cuadricula
def draw_grid():
    heigth = background.get_height()
    width = background.get_width()
    #lineas verticales
    for c in range(COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGTH))
    
    #lineas horizontales
    for c in range(MAX_ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE + scroll), (SCREEN_WIDTH, c * TILE_SIZE + scroll))

run = True

while run:

    clock.tick(FPS)

    draw_bg()
    draw_grid()

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