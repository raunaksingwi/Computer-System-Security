from utility_arithmatic import extended_euclidean

def chainese_remainder(a1,a2,M1,M2):
  M = M1 * M2

  M1 = M//M1
  M2 = M//M2

  M1_INVERSE = extended_euclidean(int(equation1[1]), M1)
  M2_INVERSE = extended_euclidean(int(equation2[1]), M2)

  x = (a1 * M1 * M1_INVERSE + a2 * M2 * M2_INVERSE) % M
  return x