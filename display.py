import pygame
from numpy.core.defchararray import isnumeric

import main

pygame.font.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("KenKen")

# x = 0
# y = 0
dif = 500 / 5
val = 0

game = main.KenKen(5)
game.fill_array(5)
grid = game.field

font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
# font3 = pygame.font.SysFont("comicsans", 10)

# def get_cor(pos):
#     global x
#     x = pos[0]//dif
#     global y
#     y = pos[1]//dif

def draw():
    for i in range(5):
        for j in range(5):
            if(grid[i][j] != 0):
                pygame.draw.rect(screen, (255, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 55, j * dif + 55))
    for blocks in game.blocks:
        if ~isnumeric(blocks[-2]):
            text2 = font2.render(str(blocks[-2] + str(blocks[-1])), 1, (0, 0, 0))
            screen.blit(text2, (blocks[0][0] * dif + 15, blocks[0][1] * dif + 15))


        for i in range(0, len(blocks[0]), 2):
            # print(i)
            # print(blocks[0])
            # print(len(blocks[0]))
            # if (i+2 < len(blocks[0]) and blocks[0][i] + 1 != blocks[0][i+2]) or i+2 > len(blocks[0]):

            if len(blocks[0]) == 4:
                if i+3 < len(blocks[0]) and blocks[0][i] < blocks[0][i+2] and blocks[0][i+1] == blocks[0][i+3]:
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i+1] * dif), (blocks[0][i] * dif + dif, blocks[0][i+1] * dif), 7)
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i+1] * dif), (blocks[0][i] * dif, blocks[0][i+1] * dif + dif), 7)
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i+1] * dif + dif), (blocks[0][i] * dif + dif, blocks[0][i+1] * dif + dif), 7)
                if i+3 < len(blocks[0]) and blocks[0][i] == blocks[0][i+2] and blocks[0][i+1] < blocks[0][i+3]:
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif), 7)
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif), (blocks[0][i] * dif, blocks[0][i + 1] * dif + dif), 7)
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif + dif, blocks[0][i+1] * dif + dif), (blocks[0][i] * dif + dif, blocks[0][i+1] * dif), 7)
                if i + 3 >= len(blocks[0]) and blocks[0][i] > blocks[0][i-2] and blocks[0][i+1] == blocks[0][i-1]:
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif), 7)
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif + dif), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif + dif), 7)
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif + dif), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif), 7)
                if i + 3 >= len(blocks[0]) and blocks[0][i] == blocks[0][i-2] and blocks[0][i+1] > blocks[0][i-1]:
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif), (blocks[0][i] * dif, blocks[0][i + 1] * dif + dif), 7)
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif + dif), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif + dif), 7)
                    pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif + dif), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif), 7)

        # pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif),
        #                  (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif), 7)
        # pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif),
        #                  (blocks[0][i] * dif, blocks[0][i + 1] * dif + dif), 7)
        # pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif, blocks[0][i + 1] * dif + dif),
        #                  (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif + dif), 7)
        # pygame.draw.line(screen, (0, 0, 0), (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif + dif),
        #                  (blocks[0][i] * dif + dif, blocks[0][i + 1] * dif), 7)

        # pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        # pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


    for i in range(5):
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), 1)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), 1)

run = True

def draw_game():
    global run
    while run:
        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


def display():
    pygame.font.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("KenKen")

    draw_game()
