import pytest # import để xài pytest.raises
import pa8
import pa10


# =========================
# TEST submatrix
# =========================

def test_submatrix_basic():
    A = pa8.Matrix([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
    result = pa10.submatrix(A, 2, 2)
    expected = pa8.Matrix([[1,3],
                           [7,9]])
    assert result == expected

def test_submatrix_edge_cases():
    A = pa8.Matrix([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    result = pa10.submatrix(A,1,1)
    expected = pa8.Matrix([[5,6],
                             [8,9]])
    assert result == expected

    result = pa10.submatrix(A,3,3)
    expected = pa8.Matrix([[1,2],
                            [4,5]])
    assert result == expected
# test trường hợp biên 

def test_submatrix_invalid_index():
    A = pa8.Matrix([[1,2],
                    [3,4]])
    with pytest.raises(IndexError):
        pa10.submatrix(A, 0, 1)
        pa10.submatrix(A, 3, 0)


# =========================
# TEST determinant
# =========================

def test_det_1x1():
    A = pa8.Matrix([[5]])
    result = pa10.determinant(A)
    expected = 5
    assert result == expected

def test_det_2x2():
    A = pa8.Matrix([[1,2],
                    [3,4]])
    result = pa10.determinant(A)
    expected = -2
    assert result == expected

def test_det_3x3():
    A = pa8.Matrix([[1, -3, 0],
                    [-2, 4, 1],
                    [5, -2, 2]])
    result = pa10.determinant(A)
    expected = -17
    assert result == expected

def test_det_non_square():
    A = pa8.Matrix([[1, 2, 3],
                    [4, 5, 6]])
    with pytest.raises(ValueError):
        pa10.determinant(A)
