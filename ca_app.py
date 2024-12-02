import sys
from cellular_automata import CellularAutomata
import numpy as np
import pygame
import pygame.surfarray

def run_sim(ca: CellularAutomata, screen_size: tuple[int, int]) -> None:
  """
  Contains the main loop for running the simulation.

  ...

  Parameters:
  ca: CellularAutomata
    The simulation controller.
  screen_size: tuple[int, int]
    2-tuple containing the size of the pygame window.
  """

  pygame.init()
  screen = pygame.display.set_mode(screen_size)
  clock = pygame.time.Clock()
  running = True
  paused = False

  while running:
    (running, paused) = handle_pygame_events(ca)
    if not paused:
      ca.tick_sim()
    surface = pygame.surfarray.make_surface(ca.grid)
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    clock.tick()
  pygame.quit()

def handle_pygame_events(ca: CellularAutomata) -> tuple[bool, bool]:
  """
  Handler for all pygame events. To be called each tick

  ...

  Parameters:
  ----------
  ca: CellularAutomata
    The simulation controller.

  Returns:
  ----------
  tuple[bool, bool]
    The running state and paused state respectively.
  """
  pass

def read_settings(filename: str) -> CellularAutomata:
  """
  Read simulation settings from a file.

  ...

  Parameters:
  ----------
  filename: str
    The name of the file where the settings are stored.
  
  Returns:
  ----------
  CellularAutomata
    The simulation controller class.
  """
  pass

pygame.quit()

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print(f"{sys.argv[0]} <sim settings filename>")
    exit(0)
  simulator = read_settings(sys.argv[1])
  run_sim(simulator, (512, 512))