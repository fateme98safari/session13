
import arcade

COLUMN_SPACING = 12
ROW_SPACING = 12
LEFT_MARGIN = 100
BOTTOM_MARGIN = 100



arcade.open_window(300, 300, "My Squre")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        if row % 2 ==0 and column % 2==0 or row % 2 !=0 and column % 2!=0:
            arcade.draw_rectangle_filled(x,y,8,8,arcade.color.RED,45)
        else:
            arcade.draw_rectangle_filled(x,y,8,8,arcade.color.BLUE,45)

        



arcade.finish_render()

arcade.run()