import random
import arcade


class Monster(arcade.Sprite):
    def __init__(self , h):
        super().__init__("my-project\session13\mmm.png")
        self.center_x=60
        self.center_y=h//2
        self.width=110
        self.height=110
        self.speed=8



class Enemy(arcade.Sprite):
    def __init__(self , w, h):
        super().__init__("my-project\session13\monster1.png")
        self.center_x=  w+50
        self.center_y=random.randint(0,h)
        self.width=100
        self.height=100
        self.speed=1



class Game(arcade.Window):
    def __init__(self):
      super().__init__(width=600 , height=450 , title="War")
      arcade.set_background_color(arcade.color.BLUE_YONDER)
      self.background = arcade.load_texture("my-project\session13\sea-background-video-conferencing_23-2148626865.webp")
      self.me=Monster(self.height)
      self.enemy=Enemy(self.width , self.height)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,600,450, self.background)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
       if symbol==119:
            self.me.center_y += self.me.speed
       elif symbol==115:
            self.me.center_y -= self.me.speed
          

    def update(self, delta_time: float):
        self.enemy.center_x -= self.enemy.speed

window=Game()

arcade.run()