import arcade
from random import randint
from random import choice
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_background():
    arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT/2,0,arcade.color.FOREST_GREEN)
    arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_HEIGHT/2,arcade.color.SKY_BLUE)

def draw_brid(x,y,scale):
    arcade.draw_arc_outline(x,y,30*scale,20*scale,arcade.color.BLACK,0,90)
    arcade.draw_arc_outline(x+(60*scale),y,30*scale,20*scale,arcade.color.BLACK,90,180)

def draw_tree(x,y,scale):
    arcade.draw_lrtb_rectangle_filled(x-5*scale,x+5*scale,y+20*scale,y,arcade.color.ROSEWOOD)
    arcade.draw_triangle_filled(x-30*scale,y+20*scale,x,y+60*scale,x+30*scale,y+20*scale,arcade.color.SAP_GREEN)
    arcade.draw_triangle_outline(x-30*scale,y+20*scale,x,y+60*scale,x+30*scale,y+20*scale,arcade.color.UP_FOREST_GREEN,0.5)
def create_brids(x1,y1,x2,y2,amount):
        for n in range(amount):
            x = randint(x1,x2)
            y = randint(y1,y2)
            size = choice((0.3,0.5,0.8))
            draw_brid(x,y,size)

def create_tree(x1,y1,x2,y2,amount):
        for n in range(amount):
            x = randint(x1,x2)
            y = randint(y1,y2)
            size = choice((0.5,0.8,1,1.2,1.5))
            draw_tree(x,y,size)


def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,'Function')
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    draw_background()
    create_tree(0,0,SCREEN_WIDTH,SCREEN_HEIGHT/2,20)
    create_brids(0,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,20)



    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
