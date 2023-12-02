import math

import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {
            1: pygame.image.load('img/Wall.webp').convert(),
            2: pygame.image.load('img/Wall2.webp').convert(),
            'D': pygame.image.load('img/door.webp').convert(),
            'S': pygame.image.load('img/sky.png').convert()
        }

    def background(self, angle):
        pygame.draw.rect(self.sc, WHITE, (0, 0, WIDTH, HALF_HEIGHT))
        # sky_offset = -5 * math.degrees(angle) % WIDTH
        # self.sc.blit(self.textures['S'], (sky_offset, 0))
        # self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        # self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        fps = int(clock.get_fps())
        if fps >= 58:
            col = GREEN
        elif fps >= 20:
            col = YELLOW
        else:
            col = RED
        display_fps = str(fps)
        render = self.font.render(display_fps, 0, col)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                               map_y + 12 * math.sin(player.angle)))
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, SANDY, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)
