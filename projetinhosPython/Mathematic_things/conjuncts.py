def Union (A, B):
  return list({ x for x in A or B})

def Intersection(A, B):
  return list({ x for x in A if x in B })

def Diference(A, B):
  return list({ x for x in A if x not in B })

def Complement(A, B):
  return Diference(B, A)


A = [1, 2, 3, 4, 7, 5, 12, 17]
B = [2, 3, 5, 7, 12]

C = [1, 5, 7]

print(Complement(Intersection(B, C), A))

print(Union(Complement(B, A), Complement(C, A)))