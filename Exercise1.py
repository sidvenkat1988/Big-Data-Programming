S1 = "ABAZDC"
S2 = "BACBAD"
A = ""

#Matching the earliest existence of S1[0] in S2
if S1[0] == S2[0]:
    A = S2[0]
elif S1[0] == S2[1]:
    A = S2[1]
elif S1[0] == S2[2]:
    A = S2[2]
elif S1[0] == S2[3]:
    A = S2[3]
elif S1[0] == S2[4]:
    A = S2[4]
elif S1[0] == S2[5]:
    A = S2[5]
else:
    A = ''
print(A)

#Matching the earliest existence of S1[1] in S2
if S1[1] == S2[0] and (S1[0] != S2[0] or S1[0] != S2[1]):
    A = A + S2[0]
elif S1[1] == S2[1] and (S1[0] != S2[1] or S1[0] != S2[2]):
    A = A + S2[1]
elif S1[1] == S2[2] and (S1[0] != S2[2] or S1[0] != S2[3]):
    A = A + S2[2]
elif S1[1] == S2[3] and (S1[0] != S2[3] or S1[0] != S2[4]):
    A = A + S2[3]
elif S1[1] == S2[4] and (S1[0] != S2[4] or S1[0] != S2[5]):
    A = A + S2[4]
elif S1[1] == S2[5] and (S1[0] != S2[5]):
    A = A + S2[5]
else:
    A = A
print(A)

#Matching the earliest existence of S1[2] in S2
if S1[2] == S2[0] and ((S2[0] != (S1[0] or S1[1])) or (S2[1] != (S1[0] or S1[1]))):
    A = A + S2[0]
elif S1[2] == S2[1] and ((S2[1] != (S1[1] or S1[2])) or (S2[2] != (S1[1] or S1[2]))):
    A = A + S2[1]
elif S1[2] == S2[2] and ((S2[2] != (S1[2] or S1[3])) or (S2[3] != (S1[2] or S1[3]))):
    A = A + S2[2]
elif S1[2] == S2[3] and ((S2[3] != (S1[3] or S1[4])) or (S2[4] != (S1[3] or S1[4]))):
    A = A + S2[3]
elif S1[2] == S2[4] and ((S2[4] != (S1[4] or S1[5])) or (S2[5] != (S1[4] or S1[5]))):
    A = A + S2[4]
elif S1[2] == S2[5] and (S2[5] != S1[5]):
    A = A + S2[5]
else:
    A = A
print(A)

#Matching the earliest existence of S1[3] in S2
if S1[3] == S2[0] and ((S2[0] != (S1[0] or S1[1] or S1[2])) or (S2[1] != (S1[0] or S1[1] or S1[2])) or (S2[2] != (S1[0] or S1[1] or S1[2]))):
    A = A + S2[0]
elif S1[3] == S2[1] and ((S2[1] != (S1[1] or S1[2] or S1[3])) or (S2[2] != (S1[1] or S1[2] or S1[3])) or (S2[3] != (S1[1] or S1[2] or S1[3]))):
    A = A + S2[1]
elif S1[3] == S2[2] and ((S2[2] != (S1[2] or S1[3] or S1[4])) or (S2[3] != (S1[2] or S1[3] or S1[4])) or (S2[4] != (S1[2] or S1[3] or S1[4]))):
    A = A + S2[2]
elif S1[3] == S2[3] and ((S2[3] != (S1[3] or S1[4] or S1[5])) or (S2[4] != (S1[3] or S1[4] or S1[5])) or (S2[5] != (S1[3] or S1[4] or S1[5]))):
    A = A + S2[3]   
elif S1[3] == S2[4] and ((S2[4] != (S1[4] or S1[5])) or (S2[5] != (S1[4] or S1[5]))):
    A = A + S2[4]
elif S1[3] == S2[5] and ((S2[5] != (S1[5]))):
    A = A + S2[5]
else:
    A = A
print(A)

#Matching the earliest existence of S1[4] in S2
if S1[4] == S2[0] and ((S2[0] != (S1[0] or S1[1] or S1[2] or S1[3])) or (S2[1] != (S1[0] or S1[1] or S1[2] or S1[3])) or
(S2[2] != (S1[0] or S1[1] or S1[2] or S1[3])) or (S2[3] != (S1[0] or S1[1] or S1[2] or S1[3]))):
    A = A + S2[0]
elif S1[4] == S2[1] and ((S2[1] != (S1[1] or S1[2] or S1[3] or S1[4])) or (S2[2] != (S1[1] or S1[2] or S1[3] or S1[4])) or
(S2[3] != (S1[1] or S1[2] or S1[3] or S1[4])) or (S2[4] != (S1[1] or S1[2] or S1[3] or S1[4]))):
    A = A + S2[1]
elif S1[4] == S2[2] and ((S2[2] != (S1[2] or S1[3] or S1[4] or S1[5])) or (S2[3] != (S1[2] or S1[3] or S1[4] or S1[5])) or
(S2[4] != (S1[2] or S1[3] or S1[4] or S1[5])) or (S2[5] != (S1[2] or S1[3] or S1[4] or S1[5]))):
    A = A + S2[2]
elif S1[4] == S2[3] and ((S2[3] != (S1[3] or S1[4] or S1[5])) or (S2[4] != (S1[3] or S1[4] or S1[5])) or
(S2[5] != (S1[3] or S1[4] or S1[5]))):
    A = A + S2[3]
elif S1[4] == S2[4] and ((S2[4] != (S1[4] or S1[5])) or (S2[5] != (S1[4] or S1[5]))):
    A = A + S2[4]
elif S1[4] == S2[5] and ((S2[5] != (S1[5]))):
    A = A + S2[5]
else:
    A = A
print(A)

#Matching the earliest existence of S1[5] in S2
if S1[5] == S2[0] and ((S2[0] != (S1[0] or S1[1] or S1[2] or S1[3] or S1[4])) or (S2[1] != (S1[0] or S1[1] or S1[2] or S1[3] or S1[4])) or (S2[2] != (S1[0] or S1[1] or S1[2] or S1[3] or S1[4])) or (S2[3] != (S1[0] or S1[1] or S1[2] or S1[3] or S1[4])) or (S2[4] != (S1[0] or S1[1] or S1[2] or S1[3] or S1[4]))):
    A = A + S2[0]
elif S1[5] == S2[1] and ((S2[1] != (S1[1] or S1[2] or S1[3] or S1[4] or S1[5])) or (S2[2] != (S1[1] or S1[2] or S1[3] or S1[4] or S1[5])) or (S2[3] != (S1[1] or S1[2] or S1[3] or S1[4] or S1[5])) or (S2[4] != (S1[1] or S1[2] or S1[3] or S1[4] or S1[5])) or (S2[5] != (S1[1] or S1[2] or S1[3] or S1[4] or S1[5]))):
    A = A + S2[1]
elif S1[5] == S2[2] and ((S2[2] != (S1[2] or S1[3] or S1[4] or S1[5])) or (S2[3] != (S1[2] or S1[3] or S1[4] or S1[5])) or (S2[4] != (S1[2] or S1[3] or S1[4] or S1[5])) or (S2[5] != (S1[2] or S1[3] or S1[4] or S1[5]))):
    A = A + S2[2]
elif S1[5] == S2[3] and ((S2[3] != (S1[3] or S1[4] or S1[5])) or (S2[4] != (S1[3] or S1[4] or S1[5])) or (S2[5] != (S1[3] or S1[4] or S1[5]))):
    A = A + S2[3]
elif S1[5] == S2[4] and ((S2[4] != (S1[4] or S1[5])) or (S2[5] != (S1[4] or S1[5]))):
    A = A + S2[4]
elif S1[5] == S2[5] and ((S2[5] != (S1[5]))):
    A = A + S2[5]
else:
    A = A
print(A)