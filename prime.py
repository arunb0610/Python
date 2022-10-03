import math
num = int(input("Enter a limit :"))
for i in range(1,num):
    prime = int(math.sqrt(i))
    for j in range(2,prime+1):
        if i%j == 0 :break
        else:
            print(i)
