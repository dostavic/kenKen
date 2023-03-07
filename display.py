import pygame
from numpy.core.defchararray import isnumeric
import Kenken

class Display:

    def __init__(self, game: Kenken):
        self.game = game
        pygame.font.init()

        pygame.display.set_caption("KenKen")
        self.screen = pygame.display.set_mode((500, 500))
        self.size = game.size
        self.dif = 500 / self.size
        self.val = 0
        self.font1 = pygame.font.SysFont("comicsans", 40)
        self.font2 = pygame.font.SysFont("comicsans", 20)
        self.font3 = pygame.font.SysFont("comicsans", 30)

        self.run = True
        self.screen.fill((255, 255, 255))

        text1 = self.font3.render("Press corresponding button on the keyboard", True, (0, 0, 0))
        self.screen.blit(text1, (30, 50))

        text1 = self.font1.render("1  -  DFS", True, (0, 0, 0))
        self.screen.blit(text1, (100, 180))

        text1 = self.font1.render("2  -  Backtracking", True, (0, 0, 0))
        self.screen.blit(text1, (100, 230))

        text1 = self.font1.render("3  -  Forward-check", True, (0, 0, 0))
        self.screen.blit(text1, (100, 280))

        text1 = self.font1.render("4  -  Maps (default: 3x3)", True, (0, 0, 0))
        self.screen.blit(text1, (100, 330))

        text1 = self.font2.render("Created by: Dmytro Havrysh", True, (0, 0, 0))
        self.screen.blit(text1, (300, 450))

        text1 = self.font2.render("Yurii Levchenko", True, (0, 0, 0))
        self.screen.blit(text1, (375, 470))



    def draw_maps_select(self):
        self.screen.fill((255, 255, 255))

        text1 = self.font1.render("1  -  3x3", True, (0, 0, 0))
        self.screen.blit(text1, (200, 130))

        text1 = self.font1.render("2  -  4x4", True, (0, 0, 0))
        self.screen.blit(text1, (200, 180))

        text1 = self.font1.render("3  -  5x5", True, (0, 0, 0))
        self.screen.blit(text1, (200, 230))

        text1 = self.font1.render("4  -  8x8", True, (0, 0, 0))
        self.screen.blit(text1, (200, 280))

        text1 = self.font1.render("5  -  9x9", True, (0, 0, 0))
        self.screen.blit(text1, (200, 330))


    def draw_game(self):
        while self.run:
            self.screen.fill((255, 255, 255))
            self.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
        pygame.quit()

    def draw(self):
        self.screen.fill((255, 255, 255))

        for i in range(self.size):
            for j in range(self.size):
                # if self.game.field[j][i] != 0:
                pygame.draw.rect(self.screen, (255, 255, 255),
                                     (i * self.dif, j * self.dif, self.dif + 1, self.dif + 1))
                text1 = self.font1.render(str(self.game.field[j][i]), 1, (0, 0, 0))
                if self.size != 8 and self.size != 9:
                    self.screen.blit(text1, (i * self.dif + 55, j * self.dif + 55))
                else:
                    self.screen.blit(text1, (i * self.dif + 30, j * self.dif + 30))
        for blocks in self.game.blocks:
            if ~isnumeric(blocks[-2]):
                text2 = self.text_to(blocks)
                self.screen.blit(text2, (blocks[0][0] * self.dif + 15, blocks[0][1] * self.dif + 15))

        if self.game.size == 3:
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif), (500, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif * 2), (self.dif * 2, self.dif * 2), 7)

            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, 0), (self.dif, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif), (self.dif * 2, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif * 2), (self.dif, self.dif * 3), 7)
        elif self.size == 4:
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif), (self.dif * 3, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 2), (self.dif * 2, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif * 2), (self.dif * 4, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 3), (self.dif * 4, self.dif * 3), 7)

            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, 0), (self.dif, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, 0), (self.dif * 3, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif), (self.dif * 3, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif), (self.dif * 2, self.dif * 4), 7)
        elif self.size == 5:
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif), (self.dif * 2, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif), (self.dif * 5, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif * 2), (self.dif * 3, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 3), (self.dif * 5, self.dif * 3), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 4), (self.dif * 4, self.dif * 4), 7)

            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, 0), (self.dif * 2, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif), (self.dif, self.dif * 3), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, 0), ( self.dif * 3, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, self.dif), (self.dif * 4, self.dif * 5), 7)
        elif self.size == 8:
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif), (self.dif, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif), (self.dif * 4, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 5, self.dif), (self.dif * 7, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif * 2), (self.dif * 5, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0,self.dif * 3), (self.dif * 8, self.dif * 3), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif * 4), (self.dif * 7, self.dif * 4), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 5), (self.dif * 8, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 6), (self.dif * 8, self.dif * 6), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif * 7), (self.dif * 7, self.dif * 7), 7)

            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif), (self.dif, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif * 6), (self.dif, self.dif * 7), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, 0), (self.dif * 2, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif * 3), (self.dif * 2, self.dif * 4), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif * 5), (self.dif * 2, self.dif * 6), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif * 7), (self.dif * 2, self.dif * 8), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif * 2), (self.dif * 3, self.dif * 3), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif * 4), (self.dif * 3, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif * 6), (self.dif * 3, self.dif * 7), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, 0), (self.dif * 4, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, self.dif * 3), (self.dif * 4, self.dif * 4), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, self.dif * 5), (self.dif * 4, self.dif * 6), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, self.dif * 7), (self.dif * 4, self.dif * 8), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 5, 0), (self.dif * 5, self.dif * 3), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 5, self.dif * 4), (self.dif * 5, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 5, self.dif * 6), (self.dif * 5, self.dif * 7), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 6, self.dif), (self.dif * 6, self.dif * 4), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 6, self.dif * 5), (self.dif * 6, self.dif * 6), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 6, self.dif * 7), (self.dif * 6, self.dif * 8), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 7, 0), (self.dif * 7, self.dif * 3), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 7, self.dif * 4), (self.dif * 7, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 7, self.dif * 6), (self.dif * 7, self.dif * 7), 7)

        elif self.size == 9:
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif), (self.dif * 9, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 2), (self.dif * 7, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif * 3), (self.dif * 2, self.dif * 3), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif * 3), (self.dif * 9, self.dif * 3), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif * 4), (self.dif * 7, self.dif * 4), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 8, self.dif * 4), (self.dif * 9, self.dif * 4), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 5), (self.dif * 2, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif * 5), (self.dif * 4, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 7, self.dif * 5), (self.dif * 9, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 6), (self.dif * 3, self.dif * 6), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, self.dif * 6), (self.dif * 8, self.dif * 6), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 7), (self.dif * 2, self.dif * 7), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif * 7), (self.dif * 5, self.dif * 7), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 7, self.dif * 7), (self.dif * 9, self.dif * 7), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.dif * 8), (self.dif * 3, self.dif * 8), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 5, self.dif * 8), (self.dif * 7, self.dif * 8), 7)

            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif), (self.dif, self.dif * 5), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, 0), (self.dif * 2, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 2, self.dif * 3), (self.dif * 2, self.dif * 8), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif), (self.dif * 3, self.dif * 4), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 3, self.dif * 5), (self.dif * 3, self.dif * 9), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, 0), (self.dif * 4, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, self.dif * 3), (self.dif * 4, self.dif * 6), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 4, self.dif * 7), (self.dif * 4, self.dif * 9), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 5, self.dif), (self.dif * 5, self.dif * 2), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 5, self.dif * 4), (self.dif * 5, self.dif * 9), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 6, 0), (self.dif * 6, self.dif), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 6, self.dif * 4), (self.dif * 6, self.dif * 8), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 7, 0), (self.dif * 7, self.dif * 9), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 8, self.dif * 4), (self.dif * 8, self.dif * 6), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 8, self.dif * 7), (self.dif * 8, self.dif * 9), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif, self.dif * 8), (self.dif, self.dif * 9), 7)
            pygame.draw.line(self.screen, (0, 0, 0), (self.dif * 5, self.dif), (self.dif * 5, self.dif * 3), 7)

        for i in range(self.size):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.dif), (500, i * self.dif), 1)
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.dif, 0), (i * self.dif, 500), 1)

    def text_to(self, blocks):
        if blocks[-2] == "add":
            return self.font2.render(str('+' + str(blocks[-1])), 1, (0, 0, 0))
        elif blocks[-2] == "div":
            return self.font2.render(str('/' + str(blocks[-1])), 1, (0, 0, 0))
        elif blocks[-2] == "sub":
            return self.font2.render(str('-' + str(blocks[-1])), 1, (0, 0, 0))
        elif blocks[-2] == "mult":
            return self.font2.render(str('*' + str(blocks[-1])), 1, (0, 0, 0))