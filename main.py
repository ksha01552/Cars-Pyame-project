import pygame
from pygame.locals import *
import random

size = width, height = (800,800)
road_width = width // 1.6
roadmark_w = width // 80
# initialise game
pygame.init()
# window size
screen = pygame.display.set_mode(size)
# background color fill
screen.fill((60,220,0))
# set title of window
pygame.display.set_caption('Kshama Car Game')
pygame.display.update()
running = True

right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4
speed = 1

car = pygame.image.load('car2.png')
car = pygame.transform.scale(car, (200,200))
car = pygame.transform.rotate(car, 180)
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8
leff = 0

car2 = pygame.image.load('aa.png')
car2 = pygame.transform.scale(car2, (200,200))
car2 = pygame.transform.rotate(car2, 180)
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0
while running:
    counter+=1
    if counter == 1024:
        speed+=0.25
        counter=0
        print("levelup", speed)
    car2_loc[1] = car2_loc[1] + speed
    if car2_loc[1] > height:
        x = random.randint(0,1)
        if x:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    
    # end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] -200:
        print("Game Over")
        break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('bye')
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a] and not leff:
                car_loc = car_loc.move([-(road_width//2), 0])
                leff = 1
            if event.key in [pygame.K_RIGHT, pygame.K_d] and leff:
                car_loc = car_loc.move([(road_width//2), 0])
                leff = 0
    pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2 - road_width/2, 0, road_width, height)
    )
    pygame.draw.rect(
        screen,
        (255,240,60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2 - road_width/2 + roadmark_w*2, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2 + road_width/2 - roadmark_w*3, 0, roadmark_w, height)
    )
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()

pygame.quit()