# 2023-08-09 밤에 만들기 시작했다.
# 만드는데 약 1시간 30분 정도 걸렸다. 

import pygame
import numpy as np
import random

# Info of the map
SCREEN_SIZE = [600, 600]
ARRAY_SIZE = [200, 200]
NUM_ISLAND = 23
MIN_ISLAND_SIZE = 6000
MAX_ISLAND_SIZE = 6500

CELL_WIDTH = SCREEN_SIZE[0] // ARRAY_SIZE[0]
CELL_HEIGHT = SCREEN_SIZE[1] // ARRAY_SIZE[1]

# Colours of elements
TERRITORY_COLOR = (143, 133, 123)
WATER_COLOR = (55, 55, 119)

def create_map(width, height, num_islands, min_island_size, max_island_size):
    maps = []

    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(0)  # 초기값으로 모두 물로 채움
        maps.append(row)

    # 땅 덩어리 생성
    for _ in range(num_islands):
        island_size = random.randint(min_island_size, max_island_size)
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for _ in range(island_size):
            if 0 <= y < height and 0 <= x < width:
                maps[y][x] = 1
                direction = random.choice(directions)
                y += direction[1]
                x += direction[0]

    return maps

def update_screen(array):
    screen.fill((0, 0, 0))

    for y in range(ARRAY_SIZE[1]):
        for x in range(ARRAY_SIZE[0]):
            cell_value = array[y][x]
            cell_color = TERRITORY_COLOR if cell_value == 1 else WATER_COLOR

            pygame.draw.rect(screen, cell_color, (x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

    pygame.display.flip()

def take_input():
    global SCREEN_SIZE, ARRAY_SIZE, NUM_ISLAND, MIN_ISLAND_SIZE, MAX_ISLAND_SIZE

    SCREEN_SIZE[0] = int(input("(Vertical) WINDOWS_SCREEN_SIZE: "))
    SCREEN_SIZE[1] = int(input("(Horizontal) WINDOWS_SCREEN_SIZE: "))
    ARRAY_SIZE[0] = int(input("(Vertical) MAP_SIZE: "))
    ARRAY_SIZE[1] = int(input("(Horizontal) MAP_SIZE: "))
    NUM_ISLAND = int(input("NUM_ISLAND: "))
    MIN_ISLAND_SIZE = int(input("MIN_ISLAND_SIZE: "))
    MAX_ISLAND_SIZE = int(input("MAX_ISLAND_SIZE: "))

if __name__ == "__main__":
    take_input()

    array = create_map(ARRAY_SIZE[0], ARRAY_SIZE[1], 5, MIN_ISLAND_SIZE, MAX_ISLAND_SIZE)

    # Set Pygame
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Map Generator")

    update_screen(array)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
