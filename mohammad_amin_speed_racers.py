import pygame, random

pygame.init()

screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("....speed racers....")
icon  = pygame.image.load("speed_racers.jpg")
pygame.display.set_icon(icon)


car_yellow_img = pygame.image.load("yellow_car.png")
car_yellow_img = pygame.transform.scale(car_yellow_img, (50, 100))
car_yellow_x = 600
car_yellow_y = 700
car_yellow_speed = 0.5


car1_img = pygame.image.load("car1.png")
car1_img = pygame.transform.scale(car1_img, (50, 90))
car1_x = random.randint(350, 650)
car1_y = -100

car2_img = pygame.image.load("car2.png")
car2_img = pygame.transform.scale(car2_img, (50, 90))
car2_x = random.randint(350, 650)
car2_y = -100

car3_img = pygame.image.load("car3.png")
car3_img = pygame.transform.scale(car3_img, (50, 90))
car3_x = random.randint(350, 650)
car3_y = -100

car4_img = pygame.image.load("car4.png")
car4_img = pygame.transform.scale(car4_img, (50, 90))
car4_x = random.randint(350, 650)
car4_y = -100


running = True
while running:
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_yellow_x -= car_yellow_speed
    if keys[pygame.K_RIGHT]:
        car_yellow_x += car_yellow_speed
    if keys[pygame.K_UP]:
        car_yellow_y -= car_yellow_speed
    if keys[pygame.K_DOWN]:
        car_yellow_y += car_yellow_speed

    if car_yellow_x < 0:
        car_yellow_x = 0
    if car_yellow_x > 1150:
        car_yellow_x = 1150
    if car_yellow_y < 0:
        car_yellow_y = 0
    if car_yellow_y > 700:
        car_yellow_y = 700


    if car1_y < 800:
        car1_y += 1.8
            
    elif car2_y < 800:
        car2_y += 1.8
           
    elif car3_y < 800:
        car3_y += 1.8
          
    elif car4_y < 800:
        car4_y += 1.8
          
    screen.fill((55, 93, 15))
    screen.blit(car_yellow_img, (car_yellow_x, car_yellow_y))
    screen.blit(car1_img, (car1_x, car1_y))
    screen.blit(car2_img, (car2_x, car2_y))
    screen.blit(car3_img, (car3_x, car3_y))
    screen.blit(car4_img, (car4_x, car4_y))
    pygame.display.update()