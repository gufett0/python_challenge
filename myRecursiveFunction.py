from random import randrange

def myRecursive():
  
  A = randrange(1, 9)
  B = randrange(1, 9)
  C = A*B
  
  if C != 4:
    print("A : %d, C : %d" % (A, C))
    return myRecursive()
  else:
    print("Success!\nA : %d, B : %d" % (A, B))
