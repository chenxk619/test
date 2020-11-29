import pygame
import sys


def board_update(screen, grid, multiplier):
	screen.fill((255,255,255))
	for i in range(0, grid * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, grid * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (grid * multiplier, i))
	pygame.display.update()



def game(screen, snake, multiplier, grid):
	start, game_start = True, True
	state = None
	while start == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#To start the game
		if pygame.key.get_pressed()[pygame.K_SPACE]:
			game_start = True

		if pygame.key.get_pressed()[pygame.K_UP] or state == 'up':
			state = 'up'

		elif pygame.key.get_pressed()[pygame.K_UP] or state == 'down':
			state = 'down'

		elif pygame.key.get_pressed()[pygame.K_UP] or state == 'left':
			state = 'left'

		elif pygame.key.get_pressed()[pygame.K_UP] or state == 'right':
			state = 'right'

		board_update(screen, grid, multiplier)




def main():
	cells = []
	multiplier = 15
	grid = 50
	pygame.init()
	pygame.display.set_caption('Snake')
	size = width, height = 750, 750
	screen = pygame.display.set_mode(size)
	game(screen, cells, multiplier, grid)

while __name__ == '__main__':
	main()