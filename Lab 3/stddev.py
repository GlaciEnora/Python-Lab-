def stddev(*x):
    xmean = 0
    for i in range(len(x)):
        xmean += x[i]
    xmean /= len(x)
    s = 0
    for i in range(len(x)):
        s += (xmean - x[i])**2
    s /= len(x)
    s = s**0.5
    return s

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print("Standard deviation for a given set of values: ", stddev(a, b, c, d, e))

if __name__ == "__main__":
    main()
