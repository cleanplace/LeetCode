def findTheWinner(n, k):
    prev = 0
    for i in range(1, n + 1):
        prev = (prev + k) % i
    return prev + 1

if __name__ == "__main__":
    n=5
    k=2
    print(findTheWinner(n, k))
