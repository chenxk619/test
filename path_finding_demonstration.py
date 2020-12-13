import pygame
import sys

def render():
	pass

def update():
	pass

def setup():
	pass

def game(screen, multiplayer):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


def main():
	multiplier = 15
	pygame.init()
	pygame.display.set_caption('A* pathing algo')
	size = width, height = 50 * multiplier, 50 * multiplier
	screen = pygame.display.set_mode(size)
	game(screen, multiplier)
	time.sleep(5)


main()
