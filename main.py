import arcade
from random import randint as ri
import numpy as np

WIDTH, HEIGHT = 1920, 1080
num_cell_row = 192 // 2
num_cell_col = 108 // 2
dim_cell = WIDTH // num_cell_row
FPS = 23.98
interval = 1 / FPS

matrix = None

def create_matrix():
    global matrix
    matrix = np.random.randint(2, size=(num_cell_row, num_cell_col))

def parse_matrix():
    copied_matrix = np.copy(matrix)

    for x in range(num_cell_row):
        for y in range(num_cell_col):
            num_of_near_cells = 0

            try:
                num_of_near_cells += copied_matrix[x-1][y-1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x][y-1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x+1][y-1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x-1][y]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x+1][y]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x-1][y+1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x][y+1]
            except: pass

            try:
                num_of_near_cells += copied_matrix[x+1][y+1]
            except: pass

            if num_of_near_cells < 2 or num_of_near_cells > 3:
                matrix[x][y] = 0
            elif num_of_near_cells == 3 and copied_matrix[x][y] == 0:
                matrix[x][y] = 1



def on_draw(delta_time):
    parse_matrix()
    arcade.start_render()

    for x in range(num_cell_row):
        for y in range(num_cell_col):
            if matrix[x][y] == 1:
                arcade.draw_rectangle_filled(
                    x * dim_cell + dim_cell // 2,
                    y * dim_cell + dim_cell // 2,
                    dim_cell, dim_cell,
                    arcade.color.GREEN
                )

    arcade.finish_render()


def main():
    create_matrix()
    window = arcade.Window(WIDTH, HEIGHT, "GAME OF PYFE", True)
    arcade.set_background_color(arcade.color.BLACK)
    window.set_update_rate(interval)
    arcade.schedule(on_draw, interval)

    arcade.run()

if __name__ == "__main__":
    main()
