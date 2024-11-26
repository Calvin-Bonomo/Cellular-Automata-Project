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

    (self.x, self.y) = dimension
    self.grid = np.zeros(dimension)
    self.convolution = convolution
  
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

    self.grid[x, y] = val

  def tick_simulation(self):
    """
    Step the simulation forward by one tick by applying `convolution` at each cell.
    """
    pass