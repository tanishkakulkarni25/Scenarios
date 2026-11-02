#Develop a Python program to determine the maximum value that can be carried in a bag of limited capacity.
n = int(input("Enter the number of items: "))
weights = list(map(int, input("Enter the weights of items: ").split()))
values = list(map(int, input("Enter the values of items: ").split()))
capacity = int(input("Enter the bag capacity: "))
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]
print("Maximum obtainable value:", dp[n][capacity])