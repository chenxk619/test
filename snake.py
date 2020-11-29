import pygame
import sys


def board_update(screen, grid, multiplier, snake):
	screen.fill((255,255,255))
	for i in range(0, grid * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, grid * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (grid * multiplier, i))

	for body in snake:
		pygame.draw.rect(screen, (0, 0, 0),(body[0] * multiplier + 1, body[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	pygame.display.update()

def movement(snake, direction):
	#called if the snake has len() > 1
	#Moves each of the body forward, except the head
	for pos in range(len(snake)-1, 0, -1):
		snake[pos] = snake[pos - 1]

	#Moves the head in the right direction
	if direction == 'up':
		snake[0] = [snake[0][0], snake[0][1] + 1]
	elif direction == 'down':
		snake[0] = [snake[0][0], snake[0][1] - 1]
	elif direction == 'left':
		snake[0] = [snake[0][0] - 1, snake[0][1]]
	elif direction == 'right':
		snake[0] = [snake[0][0] + 1, snake[0][1]]


def game(screen, snake, multiplier, grid, Clock):
	start = True
	state = 'up'
	while start == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if (pygame.key.get_pressed()[pygame.K_UP] or state == 'up') and state != 'down':
			state = 'up'
			movement(snake, state)

		elif (pygame.key.get_pressed()[pygame.K_DOWN] or state == 'down') and state != 'up':
			state = 'down'
			movement(snake, state)

		elif (pygame.key.get_pressed()[pygame.K_LEFT] or state == 'left') and state != 'right':
			state = 'left'
			movement(snake, state)

		elif (pygame.key.get_pressed()[pygame.K_RIGHT] or state == 'right') and state != 'left':
			state = 'right'
			movement(snake, state)

		Clock.tick(5)
		board_update(screen, grid, multiplier, snake)




def main():
	snake = [[25,25],[25,24]]
	multiplier = 15
	grid = 50
	pygame.init()
	pygame.display.set_caption('Snake')
	size = width, height = 750, 750
	Clock = pygame.time.Clock()
	screen = pygame.display.set_mode(size)
	game(screen, snake, multiplier, grid, Clock)

while __name__ == '__main__':
	main()