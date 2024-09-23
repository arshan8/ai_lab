def toh(a,b,c,n):
    if n == 1:
        print(f"move1 disc {a} to {c} ")
    else:
        toh(a,c,b,n-1)
        print(f"move1 disc {a} to {c} ")
        toh(b,a,c,n-1)

toh('A','B','C',3)