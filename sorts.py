numbers = [3,4,1,5,2]
n = len(numbers)

for i in range(n):
    for j in range(n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
print(numbers)