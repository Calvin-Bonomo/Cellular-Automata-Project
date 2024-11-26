import numpy as np

class CellularAutomata:
  """
  The controller for the cellular automata simulation.

  ...

  Attributes:
  ----------
  `x`: `int`
    The width of the simulation space.
  `y`: `int`
    The height of the simulation space.
  `grid`: `numpy.array(dtype=int)`
    Array containing the simulation space.
  `convolution`: numpy.array(dtype=float32)
    The convolution to apply to each cell in the simulation.
  
  Methods:
  ----------
  `set_cell`:
    Set the value of the specified cell.
  `tick_simulation`:
    Step the simulation forward by one tick by applying `convolution` at each cell.
  """
  def __init__(self, dimension, convolution):
    """
    Parameters:
    ----------
    `dimension`: `tuple`
      The size of the cellular automata simulation.
    `convolution`: `numpy.array(dtype=float32)`
      The convolution to apply to each cell in the simulation.
    """

    # Require 2d convolution
    assert len(convolution.shape) == 2 
    # Require 2d simulation space
    assert len(dimension) == 2 
    # Require convolution to be smaller than simulation space
    assert convolution.shape[0] < dimension[0] and convolution.shape[1] < dimension[1] 

    (self.x, self.y) = dimension
    self.convolution = convolution
    # Init grid with padding for the convolution's width and height
    self.grid = np.zeros((self.x + (convolution.shape[0] - 1) / 2, \
                           self.y + (convolution.shape[1] - 1) / 2))
  
  def set_cell(self, x, y, val):
    """
    Set the cell at (`x`, `y`) to the specified value.

    ...

    Parameters:
    ----------
    `x`: `int`
      The x-position of the specified cell.
    `y`: `int`
      The y-position of the specified cell.
    `val`: `int`
      The new value of the specified cell.
    """

    # Check x, y in bounds
    assert x >= 0 and x < self.x and y >= 0 and y < self.y

    self.grid[x + 1, y + 1] = val

  def tick_simulation(self):
    """
    Step the simulation forward by one tick by applying `convolution` at each cell.
    """
    
    pass