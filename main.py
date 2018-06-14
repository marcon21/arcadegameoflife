import arcade
from random import randint as ri
import numpy as np

WIDHT, HEIGHT = 800, 800
num_cell = 60
dim_cell = WIDHT // num_cell
FPS = 60
interval = 1 / FPS

matrix = None

def create_matrix():
    global matrix
    matrix = np.random.randint(2, size=(num_cell, num_cell))

def parse_matrix():
    copied_matrix = np.copy(matrix)

    for x in range(num_cell):
        for y in range(num_cell):
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

    for x in range(num_cell):
        for y in range(num_cell):
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
    arcade.open_window(WIDHT, HEIGHT, "GAME OF LIFE")

    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, interval)


    arcade.run()


if __name__ == "__main__":
    main()
