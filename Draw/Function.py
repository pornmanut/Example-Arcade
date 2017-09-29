import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_background():
    arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT/2,0,arcade.color.FOREST_GREEN)
    arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_HEIGHT/2,arcade.color.SKY_BLUE)

def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,'Function')
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    draw_background()


    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
