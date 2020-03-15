# Space Rock / Asteroid
# By To Hung Sze
# implementation of Spaceship - program template for RiceRocks
# Explosion image included
# additional changes on top of requirements:
#    - ignore keys until game starts
#    - plays explosion sound when ship / missile hits rock
# Sound continues to play if you close the window without finishing the game.
# Work around is to let the game finish - ship hits rocks 3 times.
# Suggested solution: to this problem:
# https://www.coursera.org/learn/interactive-python-2/discussions/weeks/4/threads/w-ar_btCEeimQgpwhYYAng

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False

rock_group = set()
missile_group = set()
explosion_group = set()


class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5, 5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
soundtrack = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
# soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# helper function to handle group collide
def group_collide(setA, other_object):
    holder = list(setA)
    collided = False
    for a in holder:
        if a.collide(other_object):
            setA.remove(a)
            collided = True
            # explosion_sound.rewind()
            # explosion_sound.play()	# play sound when there is a collion

            # create explosion
            new_explosion = Sprite(a.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, sound=None)
            explosion_group.add(new_explosion)
    return collided


# helper function to handle group-group collide
def group_group_collide(set1, set2):
    holder1 = list(set1)
    holder2 = list(set2)
    collisions = 0

    for element1 in holder1:
        if group_collide(set2, element1) == True:
            set1.discard(element1)
            collisions += 1
            # explosion_sound.pause()   # didn't help with getting two explosion sound when explosions happens too close together
            explosion_sound.rewind()
            explosion_sound.play()  # play sound when missile hits rock
    return collisions


# Ship class
class Ship:
    global HEIGHT, WIDTH

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def draw(self, canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]],
                              self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        # update angle
        self.angle += self.angle_vel

        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1

        self.vel[0] *= .98
        self.vel[1] *= .98

    def set_thrust(self, on):
        self.thrust = True
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
            self.thrust = False  # needed to make ship stop

    def increment_angle_vel(self):
        self.angle_vel += .05

    def decrement_angle_vel(self):
        self.angle_vel -= .05

    def get_position(self):
        return self.pos

    def get_positionX(self):
        return self.pos[0]

    def get_positionY(self):
        return self.pos[1]

    def get_radius(self):
        return self.radius

    def shoot(self):
        global missile_group

        # generate a missile
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)

    # put ship back to start position etc
    def reset(self):
        self.pos = [WIDTH / 2, HEIGHT / 2]
        self.thrust = False
        self.vel = [0, 0]
        self.angle = 0
        self.angle_vel = 0
        ship_thrust_sound.pause()


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        # version that worked before explosion image
        # canvas.draw_image(self.image, self.image_center, self.image_size,
        #                  self.pos, self.image_size, self.angle)

        # version that adds explosion image
        if self.animated is True:
            # image_size: [128,128], image_center: [64, 64], age represents the index, image contains 24 'frames'
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0] * self.age, 64], self.image_size,
                              self.pos, self.image_size, self.angle)

        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel

        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # handle age
        self.age += 1
        if self.age <= self.lifespan:
            return False  # False means keep
        else:
            return True  # True means delete

    def get_position(self):
        return [self.pos[0], self.pos[1]]

    def get_radius(self):
        return self.radius

    def collide(self, another_object):
        an_object = another_object
        if math.sqrt((self.pos[0] - an_object.get_position()[0]) ** 2 + (
                self.pos[1] - an_object.get_position()[1]) ** 2) <= self.radius + an_object.get_radius():
            # explosion_sound.pause()   # didn't help with getting two explosion sound when explosions happens too close together
            explosion_sound.rewind()
            explosion_sound.play()  # play sound when ship collides
            return True
        else:
            return False


# key handlers to control ship
def keydown(key):
    if started:  # only accept keys when game started
        if key == simplegui.KEY_MAP['left']:
            my_ship.decrement_angle_vel()
        elif key == simplegui.KEY_MAP['right']:
            my_ship.increment_angle_vel()
        elif key == simplegui.KEY_MAP['up']:
            my_ship.set_thrust(True)
        elif key == simplegui.KEY_MAP['space']:
            my_ship.shoot()


def keyup(key):
    if started:
        if key == simplegui.KEY_MAP['left']:
            my_ship.increment_angle_vel()
        elif key == simplegui.KEY_MAP['right']:
            my_ship.decrement_angle_vel()
        elif key == simplegui.KEY_MAP['up']:
            my_ship.set_thrust(False)


# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, soundtrack, lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        score = 0
        lives = 3

        rock_group = set()
        missile_group = set()

        soundtrack.rewind()
        soundtrack.play()


# help group to draw sprit
def process_sprite_group(canvas, sprite_group):
    holder = list(sprite_group)

    for sprite in holder:
        sprite.update()
        sprite.draw(canvas)
        if sprite.update() == True:  # True means remove, see update method in Sprite class
            sprite_group.remove(sprite)


def draw(canvas):
    global time, started, rock_group, lives, my_ship, missile_group, score

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw UI
    canvas.draw_text("Lives", [50, 50], 22, "White")
    canvas.draw_text("Score", [680, 50], 22, "White")
    canvas.draw_text(str(lives), [50, 80], 22, "White")
    canvas.draw_text(str(score), [680, 80], 22, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(canvas, rock_group)
    process_sprite_group(canvas, missile_group)

    process_sprite_group(canvas, explosion_group)

    # update ship and sprites
    my_ship.update()

    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())

    # determine if ship collided with a rock
    if group_collide(rock_group, my_ship):
        if lives > 0:
            lives -= 1

    # reset game when lives gets to 0 or below after checking rock / ship collision
    if lives == 0:
        rock_group = set()
        soundtrack.pause()
        started = False
        my_ship.reset()

    # get score while iterating through this method and remove rocks
    score += group_group_collide(missile_group, rock_group)


# timer handler that spawns a rock
def rock_spawner():
    global rock_group, width, height, started, my_ship

    # loop to generate rock until 12 rocks
    if len(rock_group) < 12:
        # a_rock = Sprite([WIDTH / 3, HEIGHT / 3], (random.random()*WIDTH, random.random()*HEIGHT), 0, .1, asteroid_image, asteroid_info)
        # rock_group.add(a_rock)

        # random position
        x = random.random() * WIDTH
        y = random.random() * HEIGHT

        # random speed
        x_vel = random.random()
        y_vel = random.random()

        # random angle, angle_vel
        angle = random.random()
        angle_vel = random.random() * random.choice([1, -1]) * 0.1  # slow down spinning

        # generate a rock if started is not False
        if started != False:
            # if rock is too close to ship, ignore
            if dist(my_ship.get_position(), [x, y]) > 3 * my_ship.get_radius():
                a_rock = Sprite([x, y], [x_vel, y_vel], angle, angle_vel, asteroid_image, asteroid_info)
                rock_group.add(a_rock)


# initialize stuff
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

# register handlers
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
# http://www.codeskulptor.org/#user47_bhTBqhMbTN_12.py