import pygame
import button

pygame.init()

FPS = 60
clock = pygame.time.Clock()

#ventana
SCREEN_WIDTH = 400
SCREEN_HEIGTH = 600
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGTH))
pygame.display.set_caption('Level editor')


#variables
COLS = 16
MAX_ROWS = 150
TILE_SIZE = SCREEN_WIDTH // COLS
TILE_TYPES = 16
current_tile = 0
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

#almacenar tiles en una lista
tile_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/tile/{x}.png')
    img =  pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    tile_list.append(img)


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

#crear botones
button_list = []
button_col = 0
button_row = 0
for i in range(len(tile_list)):
    tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, tile_list[i], 1)
    button_list.append(tile_button)
    button_col += 1
    if button_col == 3:
        button_row +=1
        button_col = 0

run = True

while run:

    clock.tick(FPS)

    draw_bg()
    draw_grid()
    
    #escoger un tile
    button_count = 0
    for button_count, i in enumerate(button_list):
        if i.draw(screen):
            current_tile = button_count
    
    #destacar el tile seleccionado
    pygame.draw.rect(screen, RED, button_list[current_tile].rect, 2)

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