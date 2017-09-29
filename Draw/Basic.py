import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,'Basic')
arcade.set_background_color(arcade.color.WHEAT)
arcade.start_render()
#for start,end,step
for x in range(0,SCREEN_WIDTH+1,120):
    #aracde.draw_line(startx,starty,endx,endy,color,size)
    arcade.draw_line(x,0,x,SCREEN_HEIGHT,arcade.color.FLAME,2)

for y in range(0,SCREEN_HEIGHT,120):
    arcade.draw_line(0,y,SCREEN_HEIGHT,y,arcade.color.FLAME,2)

arcade.finish_render()
#keep open
arcade.run()
