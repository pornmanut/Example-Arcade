"""
List of Basic.py
    Sector Basic Draw:
    1 Point
    2 Points
    3 Line
    4 Lines
    5 Line_Strip
    6 Polygon_outline
    7 Polygon_filled
    8 Images_spirte
    9
    10
    11
    12
    13
    14
    15
    16
"""


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

arcade.draw_text('draw_line_strip',20,SCREEN_HEIGHT-285,arcade.color.BLACK,12)
list_of_strip = ((20,SCREEN_HEIGHT-185),(20,SCREEN_HEIGHT-250),
                 (40,SCREEN_HEIGHT-185),(40,SCREEN_HEIGHT-250),
                 (60,SCREEN_HEIGHT-185),(60,SCREEN_HEIGHT-250),
                 (80,SCREEN_HEIGHT-185),(80,SCREEN_HEIGHT-250),
                 (100,SCREEN_HEIGHT-185),(100,SCREEN_HEIGHT-250),
                 (120,SCREEN_HEIGHT-185),(120,SCREEN_HEIGHT-250))

#arcade.draw_line_strip(tuple(x,y),color,size)
arcade.draw_line_strip(list_of_strip,arcade.color.FOREST_GREEN,2)

arcade.draw_text('draw_line_polygon',155,SCREEN_HEIGHT-260,arcade.color.BLACK,12)
arcade.draw_text('outline',200,SCREEN_HEIGHT-285,arcade.color.BLACK,12)
list_of_poloygon_outline = ((170,SCREEN_HEIGHT-185),
                            (280,SCREEN_HEIGHT-200),
                            (200,SCREEN_HEIGHT-230),
                            (160,SCREEN_HEIGHT-190))
#aracde.draw_polygon_outline(tuple(x,y),color,size)
arcade.draw_polygon_outline(list_of_poloygon_outline,arcade.color.AIR_FORCE_BLUE,2)

arcade.draw_text('draw_line_polygon',305,SCREEN_HEIGHT-260,arcade.color.BLACK,12)
arcade.draw_text('filled',350,SCREEN_HEIGHT-285,arcade.color.BLACK,12)

list_of_poloygon_filled = ((320,SCREEN_HEIGHT-185),
                            (430,SCREEN_HEIGHT-200),
                            (350,SCREEN_HEIGHT-230),
                            (310,SCREEN_HEIGHT-190))
#arcade.draw_polygon_filled(list,color)
arcade.draw_polygon_filled(list_of_poloygon_filled,arcade.color.ONYX)

arcade.draw_text('draw_image',475,SCREEN_HEIGHT-280,arcade.color.BLACK,12)
texture_sprite = arcade.load_texture('Images/block.png')
scale = 1.5;
#arcade.draw_texture_rectangle(centerx,centery,width,height,texture,angle)
arcade.draw_texture_rectangle(525,SCREEN_HEIGHT-240,texture_sprite.width,texture_sprite.height,texture_sprite,0)

arcade.draw_texture_rectangle(525,SCREEN_HEIGHT-200,texture_sprite.width,texture_sprite.height,texture_sprite,45)



#####
arcade.finish_render()
#keep open
arcade.run()
