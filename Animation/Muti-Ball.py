import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Ball():
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.size = size
        self.color = color

    @staticmethod
    def create_ball():
        size = random.randrange(10,30)
        x = random.randrange(size,SCREEN_WIDTH-size)
        y = random.randrange(size,SCREEN_HEIGHT-size)
        change_x = random.randrange(-2,3)
        change_y = random.randrange(-2,3)
        color = (random.randrange(256),random.randrange(256),random.randrange(256))
        ball = Ball(x,y,size,color)
        ball.change_x = change_x
        ball.change_y = change_y
        return ball

class Windows(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height,"Muti-Ball")
        arcade.set_background_color(arcade.color.VANILLA)
        self.ball_list = []
        self.ball_list.append(Ball.create_ball())


    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x,ball.y,ball.size,ball.color)

    def update(self,delta):
        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y
            if (ball.x < ball.size or ball.x > SCREEN_WIDTH - ball.size):
                ball.change_x *= -1
            if (ball.y < ball.size or ball.y > SCREEN_WIDTH - ball.size):
                ball.change_y *= -1

def main():
    Windows(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()


if __name__ == '__main__':
    main()
