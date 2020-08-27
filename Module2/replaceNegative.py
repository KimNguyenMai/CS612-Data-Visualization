ori = [8, 20, -10, 0, 55, -777]

for i in range(len(ori)): 
    if ori[i] < 0: 
        ori[i] = abs(ori[i])

print(ori)