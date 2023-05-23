def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-10):  # bug: for loop excluding the last element | fix: range(1, n-10+1)
            out *= i
    else:
        # formula for sum of n natural number = (n**n + n) / 2
        lim = n - 20  
        out = lim * lim
        out = out - lim # bug: substracting lim from out | fix: out = out + lim
        out = out / 2 
    print(out)


n = int(input("Enter an integer: "))
compute(n)

