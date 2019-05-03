# =============================================================================
# A = "ABBD"
# B = "AB*D"
# print(B)
# 
# if A[1] == A[2]:
#     A[2] == B[2]
#     print(A is B)
# =============================================================================

# =============================================================================
# A = "AA"
# B = "A*"
# if A[0] == A[1] and A[0] == B[0]:
#     B = B.replace(B[1], A[1])
# # =============================================================================
# # else:
# #     A[1] != B[1]
# # =============================================================================
# print(B)
# print(A is B)
# =============================================================================
# =============================================================================
# A = str(input("Enter string A: "))
# B = str(input("Enter string B: "))
# 
# for i in range(0,len(B)):
#     if B[i] == ".":
#         B = B.replace(B[i], B[i-1])
#         print(B)
#     if B[i] == "*":
#         B = B.replace(B[i], B[i-1])
#         print(B)
# print(B == A)
# =============================================================================

A = str(input("Input values for A: "))
B = str(input("Input values for B: "))
C = abs(len(A) - len(B))
print(C)


for i in range(0, len(B)):
    
    if B[i] == "*":
        if len(A) > len(B):
            B = B.replace(B[i], (C + 1)*(B[i-1]), 1)
        else:
            B = B.replace(B[i], B[i-1], 1)
        print("Now B is ", B)
        
        

for i in range(0, len(B)):   
    if B[i] == ".":
        B = B.replace(B[i], B[i-1], 1)
    else:
        B = B
    print("Now B is ", B)

if B[0] == ".":
    B = B.replace(B[0], A[0])
print("Now B is ", B)


    
print(A in B)