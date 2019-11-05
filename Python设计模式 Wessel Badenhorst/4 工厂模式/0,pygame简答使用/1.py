# encoding=utf-8
import pygame
import time

pygame.init()
size = (width,heigth) = (800,600)
screen = pygame.display.set_mode(size)

x = 100
y = 100
while True:
	for event in pygame.event.get():
		pressd = pygame.key.get_pressed()
		if pressd[pygame.K_UP]: y -= 4
		if pressd[pygame.K_DOWN]: y += 4
		if pressd[pygame.K_LEFT]: x -= 4
		if pressd[pygame.K_RIGHT]: x += 4
		screen.fill((0,0,0))
		pygame.draw.rect(screen,(255,255,0),pygame.Rect(x,y,20,20))
		pygame.display.flip()


time.sleep(10)

