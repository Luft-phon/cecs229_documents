import pa8

def pivot_index(i, j, A):
  """Finds the pivot position of Matrix A at or after location (i, j).
  Returns a tuple (row, col) using 1-based indexing.
  If no pivot exists, returns None.
  """
  m, n = A.dim()
  
  # TODO: Iterate through the locations in the matrix to find the pivot at or after i, j
  for col in range(j, n+1):
    for row in range(i, m+1):
      if A.get_element(row, col) != 0:
        return (row, col)
  return None
  
  
def ref(A):
    """
    Returns the Row Echelon Form of matrix A as a new Matrix.
    Does not modify the original matrix.
    """
    # Create a copy so we don't mutate the input
    R = A.copy()
    m, n = R.dim()
    
    current_row = 1
    current_col = 1
    #TODO: loop through the matrix
    while current_row <= m and current_col <= n:
        # TODO: Find the pivot index
        pivot = pivot_index(current_row, current_col, R)

        if pivot is None:
            # If no pivot is found, skip this column and move to the next
            current_col += 1
            continue

        pivot_row, pivot_col = pivot
        # TODO: Move pivot row into correct position by swapping rows if needed
        if pivot_row != current_row:
            R.swap_rows(pivot_row, current_row)
        # TODO: Eliminate entries below the pivot for that row
        pivot_val = R.get_element(current_row, pivot_col)

        R.scale_row(current_row, 1.0 / pivot_val)

        for i in range(current_row + 1, m + 1):
            entry_below = R.get_element(i, pivot_col)
            if entry_below != 0:
                R.add_row_multiple(current_row, i, -entry_below)

        current_row += 1
        current_col = pivot_col + 1

    return R