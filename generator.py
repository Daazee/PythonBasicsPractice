def manipulate_generator(generator, n):
    divisor=2
    if(n == 1):
        generator
    else:
        for j in range(divisor,n):
            remainder = n % j
            result.append(remainder)
        if 0 in result:
            reduce(generator,n)
            
        
            
def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)