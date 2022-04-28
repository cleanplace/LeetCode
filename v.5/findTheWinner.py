def findTheWinner(n, k):
    res = 0
    for i in range(1, n + 1):
        res = (res + k) % i
    return res + 1

if __name__ == "__main__":
    n=5
    k=2
    print(findTheWinner(n, k))
