import numpy as np
import pygame
import pygame.surfarray

# Setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True

arr = np.zeros((512, 512))

# Main loop
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # Logic here
  surface = pygame.surfarray.make_surface(arr)
  screen.blit(surface, (0, 0))

  pygame.display.flip()

  clock.tick()

pygame.quit()