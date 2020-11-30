import pygame
import sys
import random

class Snake:
	def __init__(self, body):
		self.body = body
		self.direction = 'up'
		self.dead = False

	def movement(self, apple):
		# called if the snake has len() > 1
		# Moves each of the body forward, except the head

		#When an apple is eaten
		if self.body[-1] == self.body[-2]:
			for pos in range(len(self.body) - 2, 0, -1):
				self.body[pos] = self.body[pos - 1]
		#For other normal cases
		else:
			for pos in range(len(self.body) - 1, 0, -1):
				self.body[pos] = self.body[pos - 1]

		# Moves the head in the right direction
		if self.direction == 'up':
			self.body[0] = [self.body[0][0], self.body[0][1] - 1]
		elif self.direction == 'down':
			self.body[0] = [self.body[0][0], self.body[0][1] + 1]
		elif self.direction == 'left':
			self.body[0] = [self.body[0][0] - 1, self.body[0][1]]
		elif self.direction == 'right':
			self.body[0] = [self.body[0][0] + 1, self.body[0][1]]

		print(self.body)
		if self.body[0] in self.body[1:]:
			self.dead = True

		return self.grow(apple)

	def grow(self, apple):
		if apple == self.body[-1] and apple is not None:
			self.body.append(apple)
			return None
		return apple


def board_update(screen, grid, multiplier, snake, apple):
	screen.fill((255,255,255))
	for i in range(0, grid * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, grid * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (grid * multiplier, i))

	#draw the apple
	pygame.draw.rect(screen, (255, 0, 0),(apple[0] * multiplier + 1, apple[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	for body in snake.body:
		pygame.draw.rect(screen, (0, 0, 0),(body[0] * multiplier + 1, body[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	pygame.display.update()



def game(screen, multiplier, snake, grid, Clock):
	apple = None

	while True:
		print(snake.dead)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if (pygame.key.get_pressed()[pygame.K_UP] or snake.direction == 'up') and snake.direction != 'down':
			snake.direction = 'up'
			apple = snake.movement(apple)

		if (pygame.key.get_pressed()[pygame.K_DOWN] or snake.direction == 'down') and snake.direction != 'up':
			snake.direction = 'down'
			apple = snake.movement(apple)

		if (pygame.key.get_pressed()[pygame.K_LEFT] or snake.direction == 'left') and snake.direction != 'right':
			snake.direction = 'left'
			apple = snake.movement(apple)

		if (pygame.key.get_pressed()[pygame.K_RIGHT] or snake.direction == 'right') and snake.direction != 'left':
			snake.direction = 'right'
			apple = snake.movement(apple)

		leave = False
		while leave == False:
			if apple == None:
				apple = [random.randint(1,grid), random.randint(1,grid)]
				if apple not in snake.body:
					leave = True
			leave = True

		Clock.tick(10)
		board_update(screen, grid, multiplier, snake, apple)



def main():
	snake = Snake([[25, 25]])
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