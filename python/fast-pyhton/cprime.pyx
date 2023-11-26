import cython

def isPrime(n):
  cdef:
    int i
  bool_ = True
  for i in range(2,n):
    if n%i==0:
      bool_ = False
      break
  return bool_
