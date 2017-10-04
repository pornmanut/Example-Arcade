import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

RECT_WIDTH = 50
RECT_HEIGHT = 50

class Windows:

    center_x = 100
    center_y = 50
    delta_x = 115
    delta_y = 130
    def on_draw(delta_time):
        arcade.start_render()
        arcade.draw_rectangle_filled(Windows.center_x,Windows.center_y,RECT_WIDTH,RECT_HEIGHT,arcade.color.RED_DEVIL)
        Windows.center_x += Windows.delta_x*delta_time
        Windows.center_y += Windows.delta_y*delta_time

        if (Windows.center_x < RECT_WIDTH//2 or Windows.center_x > SCREEN_WIDTH- RECT_WIDTH //2):
            Windows.delta_x *= -1
        if (Windows.center_y < RECT_HEIGHT//2 or Windows.center_y > SCREEN_HEIGHT-RECT_HEIGHT//2):
            Windows.delta_y *= -1

    def main():
        arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,"Bouncing")
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        arcade.schedule(Windows.on_draw,1/80)
        arcade.run()



if( __name__ == "__main__"):
    Windows.main()
