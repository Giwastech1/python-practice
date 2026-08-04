def my_info(name,age,school):
    return f"My name is {name}, I am {age} years old, my school name is {school}"

printInfo = my_info("Giwa",16,"Learn2earn.")
print(printInfo)


def my_info(age,school,name="Giwa"):
    return f"My name is {name}, I am {age} years old, my school name is {school}"

# printInfo = my_info(school="Brighton",age=16)
printInfo = my_info(16,school="Brighton")
print(printInfo)


# Higher order function
def multiplyByTwo(number):
    return number*2


num = [2,4,10]
result = map(multiplyByTwo,num)
print(list(result))

numbers = [2,4,10]
result = list(map(lambda num:num*4,numbers))
print(result)


def deleteItem(num):
    return num >= 10

x = [2,7,10,20,17]
result = filter(deleteItem,x)
print(list(result))


numbers = [20,17,11,100,23,24,8,5]
grater_than_eleven = filter(lambda x:x>11,numbers)
print(list(grater_than_eleven))

grater_than_twenty = list(filter(lambda x:x>20,numbers))
print(grater_than_twenty)


menu_items = [
      {"name": "Espresso", "price": 3.50},
      {"name": "Latte", "price": 4.50},
      {"name": "Mocha", "price": 5.00}
    ]

print_price = filter(lambda price:price["price"]<=4.50,menu_items)
print(list(print_price))

# using separate function
def filter_price(price):
    return price["price"] >= 4.50

filtered_price = list(filter(filter_price,menu_items))
print(filtered_price)


students = [
    {"name": "John", "age": 20},
    {"name": "Mary", "age": 22},
    {"name": "Peter", "age": 19},
    {"name": "Giwa", "age": 18},
    {"name": "Tosin", "age": 15}
]

grater_than_nineteen = list(filter(lambda age:age["age"]>19,students))
print(grater_than_nineteen)

# Filter using a single function
def filter_age(students_data):
    result = []
    for student in students_data:
        if student["age"] >= 15 and student["age"] <=18:
            result.append(student)
    return result
print(filter_age(students))