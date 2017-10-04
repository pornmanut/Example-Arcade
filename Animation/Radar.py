import arcade
import math
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

CENTER_X = SCREEN_WIDTH//2
CENTER_Y = SCREEN_HEIGHT//2

RADIANS_PER_FRAME = 0.02
SWEEP_LENGTH = 250

class Windows(arcade.Window):

    angle = 0
    def __init__(self,width,height):
        super().__init__(width,height,"Radar")
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)

    def on_draw(self):
        Windows.angle += RADIANS_PER_FRAME
        x = SWEEP_LENGTH*math.sin(Windows.angle)+CENTER_X
        y = SWEEP_LENGTH*math.cos(Windows.angle)+CENTER_Y
        arcade.start_render()
        arcade.draw_line(CENTER_X,CENTER_Y,x,y,arcade.color.OLIVE,4)
        arcade.draw_circle_outline(CENTER_X,CENTER_Y,SWEEP_LENGTH,arcade.color.DARK_GREEN,10)

def main():
    Windows(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()
