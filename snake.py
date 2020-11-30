import pygame
import sys
import random

class Snake:
	def __init__(self, body):
		self.body = body
		self.direction = 'up'
		self.dead = False

	def movement(self, apple, grid):
		# called if the snake has len() > 1
		# Moves each of the body forward, except the head

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

		#Snake dies :((((
		if self.body[0] in self.body[1:] or not (-1 < self.body[0][0] < grid) or not (-1 < self.body[0][1] < grid):
			self.dead = True

		return self.grow(apple)

	def grow(self, apple):
		if apple == self.body[-1] and apple is not None:
			self.body.append(apple)
			return None
		return apple


def board_update(screen, grid, multiplier, snake, apple, text, textRect):
	screen.fill((0,200,0))
	colour = 150
	for i in range(0, grid * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (colour, colour, colour), (i, 0), (i, grid * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (colour, colour, colour), (0, i), (grid * multiplier, i))

	#draw the apple
	pygame.draw.rect(screen, (255, 0, 0),(apple[0] * multiplier + 1, apple[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	for body in snake.body:
		pygame.draw.rect(screen, (0, 0, 0),(body[0] * multiplier + 1, body[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	screen.blit(text, textRect)

	pygame.display.update()



def game(screen, multiplier, snake, grid, Clock):
	apple = None

	while snake.dead == False:
		print(snake.dead)
		key_pressed = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if (pygame.key.get_pressed()[pygame.K_UP] or snake.direction == 'up') and snake.direction != 'down' and key_pressed == False:
			if pygame.key.get_pressed()[pygame.K_UP]:
				key_pressed = True
			snake.direction = 'up'
			apple = snake.movement(apple, grid)

		if (pygame.key.get_pressed()[pygame.K_DOWN] or snake.direction == 'down') and snake.direction != 'up' and key_pressed == False:
			if pygame.key.get_pressed()[pygame.K_DOWN]:
				key_pressed = True
			snake.direction = 'down'
			apple = snake.movement(apple, grid)

		if (pygame.key.get_pressed()[pygame.K_LEFT] or snake.direction == 'left') and snake.direction != 'right' and key_pressed == False:
			if pygame.key.get_pressed()[pygame.K_LEFT]:
				key_pressed = True
			snake.direction = 'left'
			apple = snake.movement(apple, grid)

		if (pygame.key.get_pressed()[pygame.K_RIGHT] or snake.direction == 'right') and snake.direction != 'left' and key_pressed == False:
			if pygame.key.get_pressed()[pygame.K_RIGHT]:
				key_pressed = True
			snake.direction = 'right'
			apple = snake.movement(apple, grid)

		leave = False
		while leave == False:
			if apple == None:
				apple = [random.randint(1, grid - 1), random.randint(1, grid - 1)]
				if apple not in snake.body:
					leave = True
			leave = True
		text, textRect = score(snake)
		Clock.tick(12)
		board_update(screen, grid, multiplier, snake, apple, text, textRect)

def score(snake):
	#create a font and render text on it
	font = pygame.font.Font('freesansbold.ttf', 16)
	text = font.render('Score : {}'.format(len(snake.body) - 1), True, (0,0,0), (0,200,0))
	textRect = text.get_rect()
	textRect.center = (700, 50)
	return text, textRect

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