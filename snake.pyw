from random import randint
from time import sleep
import pygame

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

class Food:
    def __init__(self):
        self.pos = [0, 0]
        self.color = (255, 0, 0)

    def pick_pos(self, width, height):
        self.pos[0] = round(randint(0, width))
        self.pos[1] = round(randint(0, height))

        while self.pos[0] % 10 != 0: self.pos[0] -= 1
        while self.pos[1] % 10 != 0: self.pos[1] -= 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], 10, 10))

class Snake:
    def __init__(self):
        self.pos = [0, 0]
        self.color = (0, 255, 0)
        self.dir = [10, 0]
        self.length = 5
        self.prev_pos = []

    def move(self):
        self.prev_pos.insert(0, self.pos[:])

        if (len(self.prev_pos) > self.length):
            del(self.prev_pos[len(self.prev_pos) - 1])

        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]

    def user_input(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] and self.dir != [0, 10]):
            self.dir = [0, -10]

        if (keys[pygame.K_DOWN] and self.dir != [0, -10]):
            self.dir = [0, 10]

        if (keys[pygame.K_RIGHT] and self.dir != [-10, 0]):
            self.dir = [10, 0]

        if (keys[pygame.K_LEFT] and self.dir != [10, 0]):
            self.dir = [-10, 0]

    def die(self, width, height):
        font = pygame.font.SysFont("Fixedsys", 30)
        surface = font.render("GAME OVER, YOUR SCORE WAS {}".format(self.length), True, (0, 255, 0))
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        sleep(0.5)
        pygame.quit()
        exit()

    def check(self, screen, food, width, height):
        if (self.pos == food.pos):
            self.length += 1
            food.pick_pos(width, height)

        if (self.pos[0] > width or self.pos[0] < 0 or self.pos[1] > height or self.pos[1] < 0):
            self.die(width, height)

        for pos in self.prev_pos:
            if (pos == self.pos):
                self.die(width, height)

    def draw(self, screen):
        for pos in self.prev_pos:
            pygame.draw.rect(screen, self.color, (pos[0], pos[1], 10, 10))

        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], 10, 10))  

food = Food()
food.pick_pos(width, height)
snake = Snake()

while True:
    sleep(0.05)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    snake.move()
    snake.check(screen, food, width, height)
    snake.user_input()

    food.draw(screen)
    snake.draw(screen)

    pygame.display.flip()
