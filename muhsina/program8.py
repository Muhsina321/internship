# using the loops,print this patten of odd numbers only(skip even using continue): 1 3 5 7 9 11 13 15 17 19
for i in range (1,21):
    if i%2==0:
        continue
    print(i,end=" ")