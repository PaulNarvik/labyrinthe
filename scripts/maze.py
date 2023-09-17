import pygame

from settings import *

class Maze:
    def __init__(self,  game, size) -> None:
        self.game = game
        self.size = size

        self.offset = [0, 0]
        self.maze = self.new_maze(self.size)
        

    def new_maze(self, size):
        maze = []

        # Valeurs choisis arbitrairement
        wall = -1
        empty = 0

        for i in range(size[1]):
            # Alternance lignes complètes, creuses
            if i % 2 == 0:
                line = [wall for i in range(size[0])]
            else:
                line = [wall if i % 2 == 0 else empty for i in range(size[0])]

            # Cas où la ligne finit par 0
            if size[0] % 2 == 0:
                line.pop(-1)
                self.offset[0] = CELL_SIZE // 2

            maze.append(line)

        # Si la dernière ligne n'est pas complète
        if size[1] % 2 == 0:
            # Selon si la dimension x est paire ou impaire la ligne ne doit pas faire la même longueur
            maze.pop(-1)
            self.offset[1] = CELL_SIZE // 2

        return maze
    
    def draw(self):
        wall = -1
        for y, line in enumerate(self.maze):
            for x, cell in enumerate(line):
                if cell == wall:
                    pygame.draw.rect(self.game.screen, (255, 255, 255), (x * CELL_SIZE + self.offset[0], y * CELL_SIZE + self.offset[1], CELL_SIZE, CELL_SIZE))