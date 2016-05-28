
import Tkinter as tk
from Tkinter import Tk, Canvas, Frame, BOTH
import Loader
import Maze
import Player
import pygame
from pygame import display,movie
from pygame.locals import *
import sys



class Wumpus(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent)
        self.parent = parent
        self.maze = Loader.load_game()
        self.player = Player.Player(self.maze, [1,1])


    def draw_maze(self):
        self.parent.title("Wumpus")
        self.pack(fill = BOTH, expand = 1)
        self.canvas = canvas = Canvas(self)
        self.pieces_of_maze = []
        row = 0
        col = 0
        width = 501/24.

        for i in range(self.maze.dims[0]):
         for j in range(self.maze.dims[1]):

          if self.maze.maze[i][j] == 'P':
            print "P"
            self.canvas.create_rectangle(i*width, j*width, (i+1)*width, (j+1)*width, outline="#000000", fill="#000000")

          else:
            self.canvas.create_rectangle(i*width, j*width, (i+1)*width, (j+1)*width, outline="#000000", fill="#ffffff")
            player_rect = self.canvas.create_rectangle((self.player.pos[0]-1)*width, (self.player.pos[1]-1)*width, (self.player.pos[0])*width, (self.player.pos[0])*width, 
            outline="#000000", fill="#ff0000")

        canvas.pack(fill = BOTH, expand = 1)







parent = Tk()
Game = Wumpus(parent)
Game.draw_maze()
parent.geometry("500x500")
parent.mainloop()