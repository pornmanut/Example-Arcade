import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,'Function')
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()


    arcade.run()

if __name__ == "__main__":
    main()
