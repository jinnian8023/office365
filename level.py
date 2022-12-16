from sprites import *
 
 
class Level(pg.sprite.Sprite):
    def __init__(self):
        self.set_mario()
        self.set_ground()
        self.set_pipes()
        self.set_steps()
        self.set_group()
 
    def set_group(self):
        self.ground_step_pipe_group = pg.sprite.Group(self.ground_group,
                                                      self.pipe_group,
                                                      self.step_group)
 
    def update(self):
        self.check_collide()
        self.adjust_x()
        self.adjust_y()
        self.check_dead()
        print(self.mario.pos)
 
    def set_mario(self):
        self.mario = Mario()
 
    def set_ground(self):
        ground_rect1 = Collider(0, GROUND_HEIGHT, 2953, 60)
        ground_rect2 = Collider(3048, GROUND_HEIGHT, 635, 60)
        ground_rect3 = Collider(3819, GROUND_HEIGHT, 2735, 60)
        ground_rect4 = Collider(6647, GROUND_HEIGHT, 2300, 60)
 
        self.ground_group = pg.sprite.Group(ground_rect1,
                                            ground_rect2,
                                            ground_rect3,
                                            ground_rect4)
 
    def set_pipes(self):
        pipe1 = Collider(1202, 452, 83, 80)
        pipe2 = Collider(1631, 409, 83, 140)
        pipe3 = Collider(1973, 366, 83, 170)
        pipe4 = Collider(2445, 366, 83, 170)
        pipe5 = Collider(6989, 452, 83, 82)
        pipe6 = Collider(7675, 452, 83, 82)
 
        self.pipe_group = pg.sprite.Group(pipe1, pipe2,
                                          pipe3, pipe4,
                                          pipe5, pipe6)
 
    def set_steps(self):
        step1 = Collider(5745, 495, 40, 44)
        step2 = Collider(5788, 452, 40, 88)
        step3 = Collider(5831, 409, 40, 132)
        step4 = Collider(5874, 366, 40, 176)
 
        step5 = Collider(6001, 366, 40, 176)
        step6 = Collider(6044, 408, 40, 40)
        step7 = Collider(6087, 452, 40, 40)
        step8 = Collider(6130, 495, 40, 40)
 
        step9 = Collider(6345, 495, 40, 40)
        step10 = Collider(6388, 452, 40, 40)
        step11 = Collider(6431, 409, 40, 40)
        step12 = Collider(6474, 366, 40, 40)
        step13 = Collider(6517, 366, 40, 176)
 
        step14 = Collider(6644, 366, 40, 176)
        step15 = Collider(6687, 408, 40, 40)
        step16 = Collider(6728, 452, 40, 40)
        step17 = Collider(6771, 495, 40, 40)
 
        step18 = Collider(7760, 495, 40, 40)
        step19 = Collider(7803, 452, 40, 40)
        step20 = Collider(7845, 409, 40, 40)
        step21 = Collider(7888, 366, 40, 40)
        step22 = Collider(7931, 323, 40, 40)
        step23 = Collider(7974, 280, 40, 40)
        step24 = Collider(8017, 237, 40, 40)
        step25 = Collider(8060, 194, 40, 40)
        step26 = Collider(8103, 194, 40, 360)
 
        step27 = Collider(8488, 495, 40, 40)
 
        self.step_group = pg.sprite.Group(step1, step2,
                                          step3, step4,
                                          step5, step6,
                                          step7, step8,
                                          step9, step10,
                                          step11, step12,
                                          step13, step14,
                                          step15, step16,
                                          step17, step18,
                                          step19, step20,
                                          step21, step22,
                                          step23, step24,
                                          step25, step26,
                                          step27)
 
    def check_collide(self):
        self.ground_collide = pg.sprite.spritecollideany(self.mario, self.ground_group)
        self.pipe_collide = pg.sprite.spritecollideany(self.mario, self.pipe_group)
        self.step_collide = pg.sprite.spritecollideany(self.mario, self.step_group)
 
    def adjust_x(self):
        if self.pipe_collide:
            if self.mario.pos.y > self.pipe_collide.rect.y + 10:
                if self.mario.vel.x > 0:
                    self.mario.pos.x -= 5
                    self.mario.vel.x = 0
                if self.mario.vel.x < 0:
                    self.mario.pos.x = 5
                    self.mario.vel.x = 0
        if self.step_collide:
            if self.mario.pos.y > self.step_collide.rect.y + 10:
                if self.mario.vel.x > 0:
                    self.mario.pos.x -= 5
                    self.mario.vel.x = 0
                if self.mario.vel.x < 0:
                    self.mario.pos.x = 5
                    self.mario.vel.x = 0
 
    def adjust_y(self):
        if self.ground_collide:
            if self.ground_collide.rect.top < self.mario.pos.y:
                self.mario.acc.y = 0
                self.mario.vel.y = 0
                self.mario.pos.y = self.ground_collide.rect.top
            self.mario.landing = True
        else:
            self.mario.landing = False
        if self.pipe_collide:
            if self.mario.vel.y > 0:
                if self.pipe_collide.rect.top < self.mario.pos.y:
                    self.mario.acc.y = 0
                    self.mario.vel.y = 0
                    self.mario.pos.y = self.pipe_collide.rect.top
                self.mario.landing = True
        if self.step_collide:
            if self.mario.vel.y > 0:
                if self.step_collide.rect.top < self.mario.pos.y:
                    self.mario.acc.y = 0
                    self.mario.vel.y = 0
                    self.mario.pos.y = self.step_collide.rect.top
                self.mario.landing = True
 
    def check_dead(self):
        if self.mario.pos.y > GROUND_HEIGHT + 50:
            self.mario.dead = True
