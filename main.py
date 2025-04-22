from constants import *
import pygame
import player
import asteroid
import asteroidfield
import sys
import bullets


updateables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
asteroidfield.AsteroidField.containers = (updateables)
player.Player.containers = (updateables, drawables)
asteroid.Asteroid.containers = (asteroids, updateables, drawables)
bullets.Shot.containers = (shots, updateables, drawables)
def main():
	pygame.init
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	asteroid_field = asteroidfield.AsteroidField()
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
		for object in asteroids:
			if object.collision(plyr):
				sys.exit("Game over!")
			for shot in shots:
				if object.collision(shot):
					object.split()
					shot.kill()

		dt = clock.tick(60) / 1000
if __name__ == "__main__":
	main()
