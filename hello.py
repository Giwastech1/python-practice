myAge = 18
if myAge >= 18 :
    print("You are an adult")
else :
    print("You are an underage")

milk_ounces = 16
pour_amount = 6
remaining = milk_ounces - pour_amount
print(remaining)

print(False or False)

print(2 + 3 * 4)
print((2 + 3) * 4)

firstPrice = "55"
secondPrince = "20"
print(firstPrice+secondPrince)

firstPrice = int(firstPrice)
secondPrince = int(secondPrince)
print(firstPrice+secondPrince)

convertFirst = int(firstPrice)
convertSecond = int(secondPrince)
print(convertFirst+convertSecond)

myName = "Giwa Toheeb"
price = 12.5

print(type(convertFirst),type(firstPrice))
print(type(myName),type(price))

myName = "Giwa Toheeb"

if myName.isdigit() :
    print(myName)
else :
    print("Error during conversion")

#try :
    #myAge = int(input("Enter your age: "))
  ##  print(myAge)
#except ValueError :
   # print("Enter a valid number")

tempPemp = 100
teaType = "Black tea"
if (teaType == "Black tea") :
    tempPemp = 80
    print("Your black tea is being processed at")
print(tempPemp)


for count in range(1,11):
    if count % 2 == 0 :
        print(str(count) + " even")
    else :
        print(count)


drink = "fanta"
firstTwo = drink[0:2]
print(firstTwo)
firstCap = drink.capitalize()
print(firstCap)

name = "Alice"
drink = "latte"
price = 4.50

# The f-string automatically formats the variables inside the string
receipt = f"Order for {name}: {drink} — ₦{price:.2f}"
print(receipt)

orderList = "Book,Food,Basket"
finalString = ""
splitPath = orderList.split(",")
finalString = "\n".join(splitPath)
print(finalString)

words = "Iamaboy"
finalStr = ""
splitPath = words.split("a")
print(splitPath)
finalStr = "\n".join(splitPath)
print(finalStr)

long_str = "espresso with milk and caramel and chocolate with water"
split_path = long_str.split("with",1)
print(split_path)

for num in range(1,11):
    if num % 2 != 0:
        print(num)
        continue


def print_label():
    print("Name on cup: " + current_customer)
current_customer = "Ali"
print_label()

def label(name, drink, size="medium"):
    print(name + " wants a " + size + " " + drink)

# Attempt to place a positional argument AFTER a keyword argument
label("Alice",drink="espresso")


def cofee(*args):
    print(args)

cofee("chocolate","sprinkles","whipped")

def coffee(*args):
    for cofee_list in args:
        print(f"-{cofee_list}")
coffee("chocolate","sprinkles","whipped")