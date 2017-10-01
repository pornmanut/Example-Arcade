import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Window(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height,title='Test-Window')
        #setblackground-color
        arcade.set_background_color(arcade.color.BLUE_BELL)
        self.text_angle = 0
        self.time_elapsed = 0

        self.t1 = arcade.create_text("Hello1",arcade.color.BLACK,12)
        self.t2 = arcade.create_text("Hello2",arcade.color.BLACK,12,anchor_x="left",anchor_y="top")
        self.t3 = arcade.create_text("Hello3\nThis\nNumber\nis\n3",arcade.color.BLACK,12,anchor_y="top")
        self.t4 = arcade.create_text("Hello4\nHello44\nHello444",arcade.color.BLACK,12,width=200,align="center",anchor_y="top")
        self.t5 = arcade.create_text("Hello5\nI-Like\n-Center",arcade.color.BLACK,12,width=200,align="center",anchor_x="center",anchor_y="center")
    def update(self,delta_time):
        self.text_angle += 1
        self.time_elapsed += delta_time
    def on_draw(self):
        arcade.start_render()
        start_x = 50
        start_y = 550
        arcade.draw_point(start_x,start_y,arcade.color.RED,5)
        arcade.render_text(self.t1,start_x,start_y)

        start_x = 150
        start_y = 550
        arcade.draw_point(start_x,start_y,arcade.color.RED,5)
        arcade.render_text(self.t2,start_x,start_y)

        start_x = 250
        start_y = 550
        arcade.draw_point(start_x,start_y,arcade.color.RED,5)
        arcade.render_text(self.t3,start_x,start_y)

        start_x = 350
        start_y = 550
        arcade.draw_point(start_x,start_y,arcade.color.RED,5)
        arcade.render_text(self.t4,start_x,start_y)

        start_x = 50
        start_y = 400
        arcade.draw_point(start_x,start_y,arcade.color.RED,5)
        arcade.render_text(self.t5,start_x,start_y)


window = Window(SCREEN_WIDTH,SCREEN_HEIGHT)
arcade.run()
