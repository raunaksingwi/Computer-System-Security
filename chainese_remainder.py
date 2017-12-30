from utility_arithmatic import extended_euclidean

equation1 = input("x = ").split("mod")
equation2 = input("x = ").split("mod")
equation3 = input("x = ").split("mod")

M1 = int(equation1[1])
M2 = int(equation2[1])
M3 = int(equation3[1])

a1 = int(equation1[0])
a2 = int(equation2[0])
a3 = int(equation3[0])

M = M1 * M2 * M3

M1 = M//M1
M2 = M//M2
M3 = M//M3

M1_INVERSE = extended_euclidean(int(equation1[1]), M1)
M2_INVERSE = extended_euclidean(int(equation2[1]), M2)
M3_INVERSE = extended_euclidean(int(equation3[1]), M3)

x = (a1 * M1 * M1_INVERSE + a2 * M2 * M2_INVERSE + a3 * M3 * M3_INVERSE) % M
print(x)