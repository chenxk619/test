import pygame
import sys
import random

class Snake:
	def __init__(self, body):
		self.body = body
		self.len = len(self.body)
		self.head = self.body[0]
		self.tail = self.body[-1]
		self.direction = 'up'

	def movement(self):
		# called if the snake has len() > 1
		# Moves each of the body forward, except the head
		for pos in range(self.len - 1, 0, -1):
			self.body[pos] = self.body[pos - 1]

		# Moves the head in the right direction
		if self.direction == 'up':
			self.head = [self.head[0], self.head[1] - 1]
		elif self.direction == 'down':
			self.head = [self.head[0], self.head[1] + 1]
		elif self.direction == 'left':
			self.head = [self.head[0] - 1, self.head[1]]
		elif self.direction == 'right':
			self.head = [self.head[0] + 1, self.head[1]]

	def grow(self, no_apple, apple_pos):
		pass
		# if no_apple > 0:
		# 	if pos[-1] in apple_pos:
		# 		if direction == 'up':
		# 			snake[0] = [snake[0][0], snake[0][1] - 1]
		# 		elif direction == 'down':
		# 			snake[0] = [snake[0][0], snake[0][1] + 1]
		# 		elif direction == 'left':
		# 			snake[0] = [snake[0][0] - 1, snake[0][1]]
		# 		elif direction == 'right':
		# 			snake[0] = [snake[0][0] + 1, snake[0][1]]


def board_update(screen, grid, multiplier, snake):
	screen.fill((255,255,255))
	for i in range(0, grid * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, grid * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (grid * multiplier, i))

	for body in snake.body:
		pygame.draw.rect(screen, (0, 0, 0),(body[0] * multiplier + 1, body[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	pygame.display.update()




def game(screen, multiplier, snake, grid, Clock):
	start = True
	no_apples = 0
	apple_pos = []

	while start == True:

		while True:
			apple = [random.randint(1, grid), random.randint(1, grid)]
			if apple not in snake.body:
				break

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if (pygame.key.get_pressed()[pygame.K_UP] or snake.direction == 'up') and snake.direction != 'down':
			snake.direction = 'up'
			snake.movement()

		if (pygame.key.get_pressed()[pygame.K_DOWN] or snake.direction == 'down') and snake.direction != 'up':
			snake.direction = 'down'
			snake.movement()

		if (pygame.key.get_pressed()[pygame.K_LEFT] or snake.direction == 'left') and snake.direction != 'right':
			snake.direction = 'left'
			snake.movement()

		if (pygame.key.get_pressed()[pygame.K_RIGHT] or snake.direction == 'right') and snake.direction != 'left':
			snake.direction = 'right'
			snake.movement()

		if snake.body[0] == apple:
			no_apples += 1
			apple_pos.append(apple)

		grow(no_apples, apple_pos)

		Clock.tick(7)
		board_update(screen, grid, multiplier, snake)


def main():
	snake = Snake([[25, 25], [25, 24], [25, 23]])
	multiplier = 15
	grid = 50
	pygame.init()
	pygame.display.set_caption('Snake')
	size = width, height = 750, 750
	Clock = pygame.time.Clock()
	screen = pygame.display.set_mode(size)
	game(screen, multiplier, snake, grid, Clock)

while __name__ == '__main__':
	main()