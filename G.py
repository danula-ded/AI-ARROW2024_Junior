def find_val():
    x = [float(elem) for elem in input().split()]
    y = [float(elem) for elem in input().split()]
    z = [float(0) for _ in range(len(y))]
    for i in range(len(y)):
        z[i] = round(y[i] - x[i], 2)
    print(*z)
find_val()