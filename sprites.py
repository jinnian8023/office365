import random
from tools import *
from settings import *
 
vec = pg.math.Vector2
 
 
class Mario(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sheet = load_image('mario.png')
        self.load_from_sheet()
        self.walking_timer = pg.time.get_ticks()
        self.image_index = 4
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH * 0.5, GROUND_HEIGHT - 70)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.landing = False
        self.dead = False
 
    def update(self):
        self.acc = vec(0, GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.walk('right')
            if self.vel.x > 0:
                self.acc.x = TURNAROUND
            if self.vel.x <= 0:
                self.acc.x = ACC
            self.pos.x += 5
        elif keys[pg.K_LEFT]:
            self.walk('left')
            if self.vel.x < 0:
                self.acc.x = -TURNAROUND
            if self.vel.x >= 0:
                self.acc.x = -ACC
        else:
            self.image_index = 0
        if abs(self.vel.x) < MAX_SPEED:
            self.vel.x += self.acc.x
        elif keys[pg.K_LEFT]:
            self.vel.x = -MAX_SPEED
        elif keys[pg.K_RIGHT]:
            self.vel.x = MAX_SPEED
        if keys[pg.K_SPACE]:
            if self.landing:
                self.vel.y = -JUMP
        if not self.landing:
            self.image_index = 4
        self.image = self.frames[self.image_index]
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
 
        self.rect.midbottom = self.pos
 
    def calculate_animation_speed(self):
        if self.vel.x == 0:
            animation_speed = 130
        elif self.vel.x > 0:
            animation_speed = 130 - (self.vel.x * 12)
        else:
            animation_speed = 130 - (self.vel.x * 12 * -1)
        return animation_speed
 
    def walk(self, facing):
        if self.image_index == 0:
            self.image_index += 1
            self.walking_timer = pg.time.get_ticks()
        else:
            if (pg.time.get_ticks() - self.walking_timer >
                    self.calculate_animation_speed()):
                self.image_index += 1
                self.walking_timer = pg.time.get_ticks()
        if facing == 'right':
            if self.image_index > 3:
                self.image_index = 0
        if facing == 'left':
            if self.image_index > 8:
                self.image_index = 5
            if self.image_index < 5:
                self.image_index = 5
 
    def load_from_sheet(self):
        self.right_frames = []
        self.left_frames = []
 
        self.right_frames.append(
            self.get_image(178, 32, 12, 16))
        self.right_frames.append(
            self.get_image(80, 32, 15, 16))
        self.right_frames.append(
            self.get_image(96, 32, 16, 16))
        self.right_frames.append(
            self.get_image(112, 32, 16, 16))
        self.right_frames.append(
            self.get_image(144, 32, 16, 16))
 
        for frame in self.right_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_frames.append(new_image)
 
        self.frames = self.right_frames + self.left_frames
 
    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height])
        rect = image.get_rect()
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width * MARIO_SIZE),
                                    int(rect.height * MARIO_SIZE)))
        return image
 
 
class Collider(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
