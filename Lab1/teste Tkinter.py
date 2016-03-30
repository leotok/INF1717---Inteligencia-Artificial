import Tkinter as tk
#
# board = [ [None]*10 for _ in range(10) ]
#
# counter = 0
#
# root = tk.Tk()

# def on_click(i,j,event):
#     global counter
#     color = "red" if counter%2 else "black"
#     event.widget.config(bg=color)
#     board[i][j] = color
#     counter += 1


# for i,row in enumerate(board):
#     for j,column in enumerate(row):
#
#
#         # L = tk.Label(root,text='    ',bg='grey')
        # L.grid(row=i,column=j)
        # L.bind('<Button-1>',lambda e,i=i,j=j: on_click(i,j,e))


import Tkinter

screen = Tkinter.Tk()
screen.title("My First Game")

#Create a board
board = Tkinter.Canvas(screen,width=(50*10)+2,height=(50*10)+2)

width = 50
height = 50
margin = 2

for i in range(10):
    for j in range(10):
        (x, y) = (i*width + margin, j*height + margin)
        (x_lim, y_lim) = ((i+1)*width + margin, (j+1)*height + margin)
        board.create_rectangle(x, y, x_lim, y_lim)


board.pack()

screen.mainloop()





# import pygame
# import time
# from pygame.locals import *
# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
# # This sets the WIDTH and HEIGHT of each grid location
# WIDTH = 20
# HEIGHT = 20
#
# # This sets the margin between each cell
# MARGIN = 5
#
# # Create a 2 dimensional array. A two dimensional
# # array is simply a list of lists.
# grid = []
# for row in range(10):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(10):
#         grid[row].append(0)  # Append a cell
#
#
#
# # Initialize pygame
# pygame.init()
#
# WINDOW_SIZE = [500, 500]
# screen = pygame.display.set_mode(WINDOW_SIZE)
#
# done = False
#
# while not done:
#     time.sleep(3)
#     for row in range(10):
#             for column in range(10):
#                 color = WHITE
#                 if grid[row][column] == 1:
#                     color = GREEN
#                 pygame.draw.rect(screen,
#                                  color,
#                                  [(MARGIN + WIDTH) * column + MARGIN,
#                                   (MARGIN + HEIGHT) * row + MARGIN,
#                                   WIDTH,
#                                   HEIGHT])
