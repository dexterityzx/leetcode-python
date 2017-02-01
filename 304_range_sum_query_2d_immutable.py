'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

dp[i][j] = dp[i - 1][j] + dp[i][j - 1] -dp[i - 1][j - 1] + matrix[i - 1][j - 1] ;

'''

# n, m = len(matrix), len(matrix[0])
# sums = [ [0 for j in xrange(m+1)] for i in xrange(n+1) ]
# for i in xrange(1, n+1):
#     for j in xrange(1, m+1):
#         sums[i][j] = matrix[i-1][j-1] + sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1]
# print sums

'''
sums = [
 [0, 0, 0, 0, 0, 0], 
 [0, 3, 3, 4, 8, 10], 
 [0, 8, 14, 18, 24, 27], 
 [0, 9, 17, 21, 28, 36], 
 [0, 13, 22, 26, 34, 49], 
 [0, 14, 23, 30, 38, 58]
]
'''
def sumRegion(row1, col1, row2, col2):
    """
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    _sum = 0
    for i in xrange(row1,row2+1):
        _sum += sum(matrix[i][col1:col2+1])
    return _sum

def getSumMrx(matrix):
  n = len(matrix)
  m = len(matrix[0])
  _sum = [ [0 for _ in xrange(m+1)] for _ in xrange(n+1) ]
  for i in xrange(1,n+1):
    for j in xrange(1,m+1):
      _sum[i][j] = _sum[i-1][j] + _sum[i][j-1] - _sum[i-1][j-1] + matrix[i-1][j-1]
  return _sum

def sumRegion2(row1, col1, row2, col2):
    """
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    print sumMrx
    row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1
    _sum = sumMrx[row2][col2] - sumMrx[row2][col1-1] - sumMrx[row1-1][col2] + sumMrx[row1-1][col1-1]
    return _sum

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumMrx = getSumMrx(matrix)
print sumRegion2(1, 1, 2, 2)
