import numpy as np

# dim: dimension
def initialize_with_zeroes(dim):
  """
  w: vector of shape (dim,1)
  b: 0 (float or int)
  """
  w = np.zeros(shape=(dim,1), dtype=np.float32)
  b = .0
  return w, b

if __name__ == "__main__":
  
  w,b = initialize_with_zeroes(3)
  print(w)
  print(b)


