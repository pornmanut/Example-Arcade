import arcade

ROW_COUNT = 20
COLUM_COUNT = 20

WIDTH = 30
HEIGHT = 30

MARGIN = 5

SCREEN_WIDTH = (WIDTH+MARGIN)*COLUM_COUNT+MARGIN
SCREEN_HEIGHT = (HEIGHT+MARGIN)*ROW_COUNT+MARGIN

class Window(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for colum in range(COLUM_COUNT):
                self.grid[row].append(0)
            print(self.grid[row])
        arcade.set_background_color(arcade.color.AERO_BLUE)

    def on_draw(self):
        arcade.start_render()
        for row in range(ROW_COUNT):
            for coloum in range(COLUM_COUNT):
                if self.grid[row][coloum] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                x = (MARGIN+WIDTH)*coloum+MARGIN+WIDTH//2
                y = (MARGIN+HEIGHT)*row+MARGIN+HEIGHT//2

                arcade.draw_rectangle_filled(x,y,WIDTH,HEIGHT,color)

    def on_mouse_press(self,x,y,button,modifiers):
        colum =x // (WIDTH+MARGIN)
        row = y // (HEIGHT+MARGIN)

        if row < ROW_COUNT and colum < COLUM_COUNT:
            if(self.grid[row][colum] == 0):
                self.grid[row][colum] = 1
            else:
                self.grid[row][colum] = 0

Window = Window(SCREEN_WIDTH,SCREEN_HEIGHT)

arcade.run()
