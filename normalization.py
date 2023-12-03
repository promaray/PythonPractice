import numpy as np

def normalize_rows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).
    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    axis = 1 is normalize by row
    axis = 0 is normalize by column
    
    Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    x_norm =
    Divide x by its norm.
   """

    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    x = np.divide(x,x_norm)
    return x

x = np.array([[0, 3, 4],
              [1, 6, 4]])
print("normalizeRows(x) = " + str(normalize_rows(x)))