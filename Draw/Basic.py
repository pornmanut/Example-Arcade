import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,'Basic')
arcade.set_background_color(arcade.color.WHEAT)
arcade.start_render()
####
#for start,end,step
#Horizontal
for x in range(0,SCREEN_WIDTH+1,150):
    #aracde.draw_line(startx,starty,endx,endy,color,size)
    arcade.draw_line(x,0,x,SCREEN_HEIGHT,arcade.color.FLAME,2)
#Vertical
for y in range(0,SCREEN_HEIGHT,150):
    arcade.draw_line(0,y,SCREEN_HEIGHT,y,arcade.color.FLAME,2)

#aracde.draw_text('text',x,y,color,size)
arcade.draw_text("draw_point", 35, SCREEN_HEIGHT-135, arcade.color.BLACK,12)
#aracde.draw_point(x,y,color,size)
arcade.draw_point(75,SCREEN_HEIGHT-75,arcade.color.RUBY,10)

arcade.draw_text("draw_points",185,SCREEN_HEIGHT-135,arcade.color.BLACK,12)
list_of_point = ((185,SCREEN_HEIGHT-75),(205,SCREEN_HEIGHT-75),(225,SCREEN_HEIGHT-75),
                 (245,SCREEN_HEIGHT-75),(265,SCREEN_HEIGHT-75))
#aracde.draw_points(tuple(x,y),color,size)
arcade.draw_points(list_of_point,arcade.color.RUBY,10)

arcade.draw_text("draw_line",335,SCREEN_HEIGHT-135,arcade.color.BLACK,12)
#aracde.drawline(start x,start y,end x, endy,color,size)
arcade.draw_line(320,SCREEN_HEIGHT-75,430,SCREEN_HEIGHT-75,arcade.color.WINE,2)

arcade.draw_text("draw_lines",485,SCREEN_HEIGHT-135,arcade.color.BLACK,12)
#((startx,starty),(end x,end y))
list_of_lines = ((480,SCREEN_HEIGHT-35),(480,SCREEN_HEIGHT-100),
                 (500,SCREEN_HEIGHT-35),(500,SCREEN_HEIGHT-100),
                 (520,SCREEN_HEIGHT-35),(520,SCREEN_HEIGHT-100),
                 (540,SCREEN_HEIGHT-35),(540,SCREEN_HEIGHT-100),
                 (560,SCREEN_HEIGHT-35),(560,SCREEN_HEIGHT-100),
                 (580,SCREEN_HEIGHT-35),(580,SCREEN_HEIGHT-100))
#arcade.draw_lines(listoflines,color,size)
arcade.draw_lines(list_of_lines,arcade.color.WOOD_BROWN,2)


#####
arcade.finish_render()
#keep open
arcade.run()
