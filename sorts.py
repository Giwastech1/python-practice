numbers = [3,4,1,5,2]
n = len(numbers)

for i in range(n):
    for j in range(n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
print(numbers)

# iter
items = (2,4,5,7)

iterator = iter(items)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(type(iterator))


# zip iterator
cars = ["Mazda","Volvo","Toyota"]
prices = [12000, 13500, 13000]

for car_brand in zip(cars,prices):
    print(f"car: {cars}, amount: {prices}")
print(car_brand)