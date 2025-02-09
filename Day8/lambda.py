l = [2,4,7,3,14,19]
for i in l:
    my_lambda = lambda i : i%2 == 1
    print(my_lambda(i))