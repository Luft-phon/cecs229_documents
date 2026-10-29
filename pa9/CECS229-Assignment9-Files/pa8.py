import math

class Matrix:
  def __init__(self, rows=[]):
    """Initializes a Matrix with given rows (1 based indexing)
    :param rows: the list of rows for this Matrix object.
    """
    self.rows = rows

  def copy(self):
    new_matrix = []
    for i in range(len(self.rows)):
      new_row = []
      for j in range(len(self.rows[0])):
        new_row.append(self.rows[i][j])
      new_matrix.append(new_row)
    return Matrix(new_matrix) 

  def swap_rows(self, i, j):
    temp = self.rows[i-1]
    self.rows[i-1] = self.rows[j-1]
    self.rows[j-1] = temp
    return self

  def scale_row(self, i, c):
    scaled_row = self.get_row(i)
    for j in range(len(scaled_row)):
      scaled_row[j] *= c
    self.set_row(i, scaled_row)
    return self

  def add_row_multiple(self, src, tar, c):
    source = self.get_row(src)
    target = self.get_row(tar)
    new_row = []
    for j in range(self.dim()[1]):
      value = target[j] + source[j] * c
      new_row.append(value)

    target = self.set_row(tar, new_row)
    return self
  

  def set_row(self, i, v):
    """Sets the i-th row to be the list v"""
    if len(v) != len(self.rows[0]):  # TODO check if row length is correct 
      raise ValueError("ERROR: Incompatible row length.")
    else:
      # TODO: assign the vector to the row
      self.rows[i-1] = v

  def set_col(self, j, u):
    """Sets the j-th column to be the list u."""
    if len(u) != len(self.rows):  # TODO check if column length is correct 
      raise ValueError("ERROR: Incompatible column space.")
    else:
      # TODO: assign the vector to the column
      for i in range(len(u)):
        self.rows[i][j-1] = u[i]
      

  def set_entry(self, i, j, a):
    """Sets the ij-th entry to be a."""
    # TODO: assign the element to the specified location
    self.rows[i-1][j-1] = a

  def get_row(self, i):
    """Gets the ith row.
    :return: list of elements in the ith row of the matrix.
    """
    return self.rows[i-1]# TODO: return the specified row

  def get_col(self, j):
    """Gets the jth column.
    :return: list of elements in the jth column of the matrix.
    """
    col = []
        # TODO: populate list with correct elements 
    for i in range(len(self.rows)):
        col.append(self.rows[i][j-1])
    return col 

  def get_element(self, i, j):
    """Gets the ijth element.
    :return: element at location ij in the matrix.
    """
    return self.rows[i-1][j-1]# TODO: return the specified element

  def get_columns(self):
    """Gets the list of columns.
    :return: list of columns in the matrix.
    """
    cols = []
        # TODO: populate list with column vectors
    for j in range(len(self.rows[0])):
        col = []
        for i in range(len(self.rows)):
            col.append(self.rows[i][j])
        cols.append(col)
    return cols

  def get_rows(self):
    """Gets the list of rows.
    :return: list of rows in the matrix.
    """
    return self.rows # TODO: return the list of row vectors

  def dim(self):
    """Gets the dimensions of the mxn matrix where m = number of rows, n = number of columns.
    :return: integer tuple - the dimensions of the matrix (m, n).
    """
    m = len(self.rows) # TODO: find the number of rows
    n = len(self.rows[0]) # TODO: find the number of cols
    return (m, n)

  def get_diag(self):
    """Gets the main diagonal. 
    :return: list of elements in the main diagonal of the matrix.
    """
    d = []
    
    # TODO: populate the list with the elements in the main diagonal starting from 1,1
    num_rows = len(self.rows)
    num_cols = len(self.rows[0]) if num_rows > 0 else 0
    size = min(num_rows, num_cols)
    
    for i in range(size):
        d.append(self.rows[i][i])
    return d


  def __add__(self, other):
    """Overloads the + operator to support Matrix + Matrix
    :param other: the other Matrix object
    :raises: ValueError if the Matrix objects have mismatching dimensions
    :raises: TypeError if other is not of Matrix type
    :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
    """
    if not isinstance(other, Matrix):  # TODO: check other type
      raise TypeError(f"Matrix + {type(other)} is not supported.")

    
    if self.dim() != other.dim():  # TODO: check the matrix dimensions
      raise ValueError("Matrix dimension mismatch. Can not add matrices of different dimensions.")
    
    #  TODO: create a new matrix using matrix addition
    new_matrix = []
    # for i in range(len(self.rows)):   the same as dim()[0]   0 is for rows, 1 is for columns
    for i in range(self.dim()[0]):
        new_row = []
        # for j in range(len(self.rows[0])):    the same as dim()[1]   1 is for rows, 0 is for columns
        for j in range(self.dim()[1]):
            new_row.append(self.rows[i][j] + other.rows[i][j])
        new_matrix.append(new_row)
    return Matrix(new_matrix) # TODO: return the resulting matrix

  def __sub__(self, other):
    """Overloads the - operator to support Matrix - Matrix
    :param other: the other Matrix object
    :raises: ValueError if the Matrix objects have mismatching dimensions
    :raises: TypeError if other is not of Matrix type
    :return: Matrix type; the Matrix object resulting from Matrix - Matrix operation
    """
    if not isinstance(other, Matrix):  # TODO: check other type
      raise TypeError(f"Matrix - {type(other)} is not supported.")
      
    if self.dim() != other.dim(): # TODO: check the matrix dimensions
      raise ValueError("Matrix dimension mismatch. Can not subtract matrices of different dimensions.")
      
    #  TODO: create a new matrix using matrix subtraction
    new_matrix = []
    for i in range(self.dim()[0]):
        new_row = []
        for j in range(self.dim()[1]):
            new_row.append(self.rows[i][j] - other.rows[i][j])
        new_matrix.append(new_row)
    return Matrix(new_matrix) # TODO: return the resulting matrix

  def __mul__(self, other):
    """Overloads the * operator to support Matrix * Matrix and Matrix * Scalar
    :param other: the other Matrix object or a Scalar
    :raises: ValueError if the Matrix objects have mismatching dimensions in M * M multiplication.
    :raises: TypeError if other is not of Matrix type
    :return: Matrix type; the Matrix object resulting from Matrix * Matrix or Matrix * Scalar operation
    """
    if isinstance(other, (int, float)):# TODO: check if other is a scalar
      #  TODO: create a new matrix using scalar multiplication 
      new_matrix = []
      for i in range(self.dim()[0]):
        new_row = []
        for j in range(self.dim()[1]):
          new_row.append(self.rows[i][j] * other)
        new_matrix.append(new_row)
      return Matrix(new_matrix) 
      # new_matrix = [[val * other for val in row] for row in self.rows]
      # return Matrix(new_matrix) # TODO: return the resulting matrix
    elif isinstance(other, Matrix): 
      if self.dim()[1] == other.dim()[0]:# TODO: check the matrix dimensions
        #  TODO: create a new matrix using matrix multiplication
        new_matrix_data = []
        for i in range(self.dim()[0]):
            new_row = []
            for j in range(other.dim()[1]):
                dot_product = 0
                for k in range(self.dim()[1]): 
                    dot_product += self.rows[i][k] * other.rows[k][j]
                new_row.append(dot_product)
            new_matrix_data.append(new_row)
            
        return Matrix(new_matrix_data)  # TODO: return the resulting matrix 
      else:
        raise ValueError("Incompatible dimensions")
    else:
      raise TypeError(f"Matrix * {type(other)} is not supported")
    return

  def __rmul__(self, other):
    """Overloads the * operator to support Scalar * Matrix
    :param other: the Scalar value
    :raises: TypeError if other is not a scalar 
    :return: Matrix type; the Matrix object resulting from Scalar * Matrix operation
    """
    if isinstance(other, (int, float)): # TODO: check if other is a scalar
      #  TODO: create a new matrix using scalar multiplication 
      return self.__mul__(other) # TODO: return the resulting matrix
    else:
      raise TypeError(f" {type(other)} * Matrix is not supported")
    return

  def __eq__(self, other):
    """Overloads the == operator to return True if
    two Matrix objects have the same elements in the same orientation
    """
    if not isinstance(other, Matrix):# TODO: check if other is not a matrix
      return False
    if self.dim() != other.dim():# TODO: check the matrix dimensions
      return False
    for i in range(self.dim()[0]):
      for j in range(self.dim()[1]):
        if self.rows[i][j] != other.rows[i][j]:
          return False
    return True # TODO: return true if the matrices are the same


    
  def __str__(self):
    """String representation of a Matrix."""
    mat_str = ""
    for row in self.rows:
      mat_str += str(row) + "\n"
    return mat_str

