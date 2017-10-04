import arcade


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

CIRCLE_RADIUS = 20
GRAVITY = 0.3
BOUNCINESS = 0.9

class Window:
    x = CIRCLE_RADIUS
    y = SCREEN_HEIGHT- CIRCLE_RADIUS

    delta_x = 2
    delta_y = 0

    @classmethod
    def on_draw(cls,delta):
        #start_render
        arcade.start_render()
        arcade.draw_circle_filled(cls.x,cls.y,CIRCLE_RADIUS,arcade.color.ALABAMA_CRIMSON)

        cls.x += cls.delta_x
        cls.y += cls.delta_y

        cls.delta_y -= GRAVITY

        if((cls.x < CIRCLE_RADIUS and cls.delta_x < 0)or(cls.x > SCREEN_WIDTH- CIRCLE_RADIUS and cls.delta_x > 0)):
            cls.delta_x *= -BOUNCINESS

        if(cls.y < CIRCLE_RADIUS and cls.delta_y < 0):
            if(cls.delta_y *-1 > GRAVITY * 15):
                cls.delta_y *= -BOUNCINESS
            else:
                cls.delta_y *= -BOUNCINESS//2


    @classmethod
    def main(cls):
        arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,"Bouning Ball")
        arcade.set_background_color(arcade.color.WHEAT)
        arcade.schedule(cls.on_draw,1/80)
        arcade.run()


if __name__ == '__main__':
    Window.main()
