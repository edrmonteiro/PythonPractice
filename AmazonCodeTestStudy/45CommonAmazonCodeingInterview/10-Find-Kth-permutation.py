"""
Given a set of n elements, find their Kth permutation. 
Consider the following set of elements. 
Click here to view the solution in C++, Java, JavaScript, and Ruby.

"""

def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1 )
 
def find_kth_permutation(v, k, result):
  if not v:
    return
  
  n = len(v)
  # count is number of permutations starting with first digit
  count = factorial(n - 1)
  selected = (k - 1) // count
  
  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  find_kth_permutation(v, k, result)
  
def get_permutation(n, k):
  v = list(range(1, n + 1))
  result = []
  find_kth_permutation(v, k, result)
  return ''.join(result)
 
def main():
  n = factorial(4)
  for i in range(1, n + 1):
    print(str(i) + "th permutation = \t", get_permutation(4, i))
 
main()

stop = True