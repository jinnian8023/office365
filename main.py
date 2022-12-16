from level import *
from sprites import *
 
 
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.rect = self.screen.get_rect()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.playing = True
        self.all_group = pg.sprite.Group()
        self.viewpoint = self.rect
 
    def new(self):
        self.level_surface = pg.Surface((WIDTH, HEIGHT)).convert()
        self.background = load_image('level.png')
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.back_rect.width * BACKGROUND_SIZE),
                                              int(self.back_rect.height * BACKGROUND_SIZE))).convert()
        self.level = Level()
        self.all_group.add(self.level.mario)
 
    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
 
    def update(self):
        self.all_group.update()
        self.level.update()
        if self.level.mario.pos.x < self.viewpoint.x + 15:
            self.level.mario.pos.x -= self.level.mario.vel.x
        if self.level.mario.vel.x > 0:
            if self.level.mario.pos.x > WIDTH * 0.55 + self.viewpoint.x:
                self.viewpoint.x += int(self.level.mario.vel.x * 1.1)
        if self.level.mario.dead:
            self.playing = False
 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
 
    def draw(self):
        pg.display.flip()
        self.background_clean = self.background.copy()
        self.all_group.draw(self.background_clean)
        self.screen.blit(self.background, (0, 0), self.viewpoint)
        self.all_group.draw(self.screen)
 
    def show_start_screen(self):
        pass
 
    def show_end_screen(self):
        pass
 
 
game = Game()
game.show_start_screen()
game.new()
game.run()
game.show_end_screen()
