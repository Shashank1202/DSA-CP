def star(n):
    for i in range(n):
        for j in range(i+1):
            print(" *", end="")
        print()

star(5)