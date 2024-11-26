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
  `padding`: `int`
    Padding added to the simulation space.
  
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
    # Require square convolution
    assert convolution.shape[0] == convolution.shape[1]
    # Require convolution to be odd
    assert convolution.shape[0] % 2 == 1
    # Require 2d simulation space
    assert len(dimension) == 2 
    # Require convolution to be smaller than simulation space
    assert convolution.shape[0] < dimension[0] and convolution.shape[1] < dimension[1] 

    (self.x, self.y) = dimension
    self.convolution = convolution
    self.padding = (convolution.shape[0] - 1) / 2
    # Init grid with padding for the convolution's width and height
    self.grid = np.zeros((self.x + self.padding * 2, self.y + self.padding * 2))
  
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

    self.grid[x + self.padding, y + self.padding] = val

  def tick_simulation(self):
    """
    Step the simulation forward by one tick by applying `convolution` at each cell.
    """
    
    write = np.zeros(self.grid.shape)
    for i in range(self.padding, self.x + self.padding):
      for j in range(self.padding, self.y + self.padding):
        write[i, j] = self.__apply_convolution(i, j)
    self.grid = write
  
  def __apply_convolution(self, x, y):
    """
    Returns the value of the convolution applied to the grid at (`x`, `y`).

    ...

    Parameters:
    ----------
    `x`: int
      X-position to apply the convolution to.
    `y`: int
      Y-position to apply the convolution to.
    """

    res = 0

    for i in range(-self.padding, self.padding + 1):
      for j in range(-self.padding, self.padding + 1):
        res += self.convolution[i + self.padding, j + self.padding] * self.grid[x + i, y + j]
    return res