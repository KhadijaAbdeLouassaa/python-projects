
l1 = [9, 9, 9]
l2 = [9, 9, 9, 9]
rest = []
carry = 0
l1_val = 0
l2_val = 0 

while  l1_val < len(l1) or l2_val < len(l2) :
    if l1_val == len(l1) and l2_val < len(l2):
        sum =  l2[l2_val] + carry
        rest.append(sum % 10)
        carry = sum // 10
        l2_val += 1
    elif l2_val == len(l2) and l1_val < len(l1):
        sum =  l1[l1_val] + carry
        rest.append(sum % 10 )
        carry = sum // 10
        l1_val += 1
    else :
        sum = l1[l1_val] + l2[l2_val] + carry
        rest.append(sum % 10)
        carry = sum // 10
        l1_val += 1
        l2_val += 1
if carry != 0 :
    rest.append(carry)

print(rest)














    
#st_num(l1, l2, carry)

































'''
l1 = [2, 1 ,3]
l2 = [1, 7, 2]
x = 0
y = 0
for i in range(len(l1)-1,-1, -1):
    x += l1[i]*10**i
for i in range(len(l2)-1,-1, -1):
    y += l2[i]*10**i
rest = y + x
for k i in range(len(rest)):

print()
'''




























'''
x = ""
y = ""

for i in l1 :
    x += str(i)
for i in l2 :
    y += str(i)

sult = int(x) + int(y)
print(list(str(sult)))
'''






