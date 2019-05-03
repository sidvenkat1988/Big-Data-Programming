#Entering the 2 string values for A and B
A = str(input("Input values for A: "))
B = str(input("Input values for B: "))
C = abs(len(A) - len(B))
print(C)

#Putting a condition for * to replace it with the previous character
#If A and B have similar lengths or if B is longer than A, then * will be replaced only once
#If A is longer than B, then * will be replaced with multiple instances of previous values until the lengths of A and B become equal
for i in range(0, len(B)):
    
    if B[i] == "*":
        if len(A) > len(B):
            B = B.replace(B[i], (C + 1)*(B[i-1]), 1)
        else:
            B = B.replace(B[i], B[i-1], 1)
        print("Now B is ", B)
        
        
#Putting a condition to replace "." with previous character
for i in range(0, len(B)):   
    if B[i] == ".":
        B = B.replace(B[i], B[i-1], 1)
    else:
        B = B
    print("Now B is ", B)

#If the string B begins with a value of ".", then replace it with the first index of A
if B[0] == ".":
    B = B.replace(B[0], A[0])
print("Now B is ", B)


    
print(A in B)