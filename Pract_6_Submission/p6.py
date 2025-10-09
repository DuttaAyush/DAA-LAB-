INF = int(1e9)
n = 4

dist = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]

dp = [[-1] * n for _ in range(1 << n)]
parent = [[-1] * n for _ in range(1 << n)]

def tsp(mask, pos):
    if mask == (1 << n) - 1:
        return dist[pos][0]

    if dp[mask][pos] != -1:
        return dp[mask][pos]

    ans = INF
    next_city = -1

    for city in range(n):
        if (mask & (1 << city)) == 0:
            new_dist = dist[pos][city] + tsp(mask | (1 << city), city)
            if new_dist < ans:
                ans = new_dist
                next_city = city

    parent[mask][pos] = next_city
    dp[mask][pos] = ans
    return ans

def print_path():
    mask = 1
    pos = 0
    print("Preferred Path: 0", end="")
    while True:
        next = parent[mask][pos]
        if next == -1:
            break
        print(" ->", next, end="")
        mask |= (1 << next)
        pos = next
        if mask == (1 << n) - 1:
            break
    print(" -> 0")

def main():
    min_cost = tsp(1, 0)
    print("\nMinimum Distance:", min_cost)
    print_path()

if __name__ == "__main__":
    main()