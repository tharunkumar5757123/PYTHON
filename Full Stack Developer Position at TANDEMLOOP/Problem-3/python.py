a = int(input("Enter a number: "))

if a % 2 == 0:
    a -= 1

for i in range(1, a + 1):
    print(2 * i - 1, end=" ")

