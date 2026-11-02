#Develop a Python program to determine the maximum amount that can be collected without selecting two adjacent houses.
n = int(input("Enter the number of houses: "))
houses = []
print("Enter the amount in each house:")
for i in range(n):
    houses.append(int(input()))
if n == 0:
    print("Maximum possible amount:", 0)
elif n == 1:
    print("Maximum possible amount:", houses[0])
else:
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
    print("Maximum possible amount:", dp[n - 1])