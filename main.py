from constants import *
import pygame
import player

updateables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
player.Player.containers = (updateables, drawables)
def main():
	pygame.init
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	plyr = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.Surface.fill(screen, pygame.Color("black"))
		updateables.update(dt)
		for drawable in drawables:			
			drawable.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
if __name__ == "__main__":
	main()
