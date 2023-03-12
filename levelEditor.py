import pygame
import button

pygame.init()


clock = pygame.time.Clock()
FPS = 60

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

#crear una lista de tiles
world_data = []
for col in range(MAX_ROWS):
    c = [-1] * COLS
    world_data.append(c)

#cargar imagenes
background = pygame.image.load('img/background/bg.png').convert_alpha()
particles = pygame.image.load('img/background/bg1.png').convert_alpha()

#almacenar tiles en una lista
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/tile/{x}.png')
    img =  pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)


#dibujar background
def draw_bg():
    screen.fill(GREEN)
    heigth = background.get_height()
    for x in range(10):
        screen.blit(background, (0, (-(x * heigth)) + scroll))
        screen.blit(particles, (0, (-(x * heigth)) + scroll))

#dibujar los tiles
def draw_world():
    for y, col in enumerate(world_data):
        for x, tile in enumerate(col):
            if tile >= 0:
                screen.blit(img_list[tile],(x * TILE_SIZE, y * TILE_SIZE - scroll))

#dibujar cuadricula
def draw_grid():
    heigth = background.get_height()
    width = background.get_width()
    #lineas verticales
    for c in range(COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGTH))
    
    #lineas horizontales
    for c in range(MAX_ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE - scroll), (SCREEN_WIDTH, c * TILE_SIZE - scroll))

#crear botones
button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
    tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
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
    draw_world()
    
    #escoger un tile
    button_count = 0
    for button_count, i in enumerate(button_list):
        if i.draw(screen):
            current_tile = button_count
    
    #destacar el tile seleccionado
    pygame.draw.rect(screen, RED, button_list[current_tile].rect, 2)

    #scroll
    if scroll_up == True:
        scroll += 3 * scroll_speed
    if scroll_down == True and scroll > 0:
        scroll -= 3 * scroll_speed

    pos = pygame.mouse.get_pos()
    x = pos[0] // TILE_SIZE
    y = (pos[1] + scroll) // TILE_SIZE

    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGTH:
		#update tile value
        if pygame.mouse.get_pressed()[0] == 1:
                    if world_data[y][x] != current_tile:
                        world_data[y][x] = current_tile         
        if pygame.mouse.get_pressed()[2] == 1:
            world_data[y][x] = -1

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