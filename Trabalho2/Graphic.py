
import Tkinter as tk
import Loader
import Maze
import Player

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.root = tk.tk()

        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 20
        self.columns = 20
        self.tiles = {}
        self.canvas.bind("<Configure>", self.redraw)
        self.status = tk.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")

    def play(self):

    	self.maze = Loader.load_game()
    	self.player = Player.Player([1,1])

    	self.root.bind('K-Up', self.move('U'))
    	self.root.bind('K-Right', self.move('R'))



    def redraw(self, event=None):
        self.canvas.delete("rect")
        cellwidth = int(self.canvas.winfo_width()/self.columns)
        cellheight = int(self.canvas.winfo_height()/self.columns)
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column*cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                tile = self.canvas.create_rectangle(x1,y1,x2,y2, fill="blue", tags="rect")
                self.tiles[row,column] = tile
                self.canvas.tag_bind(tile, "<1>", lambda event, row=self.player.pos[0], column=self.player.pos[1])


    def move(self, direction):

    	self.player.move(direction)
    	tile = self.tiles[self.player.pos[0],self.player.pos[1]]
        tile_color = self.canvas.itemcget(tile, "fill")
        new_color = "blue" if  tile_color == "red" else "red"
        self.canvas.itemconfigure(tile, fill=new_color)
        self.status.configure(text="you are on %s/%s" % (self.player.pos[0],self.player.pos[1]))

if __name__ == "__main__":
    app = App()
    app.mainloop()