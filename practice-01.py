count = 10

def increase():
    global count
    count = count+1

increase()
print(count)


age = 23

def increaseAge():
    age = 20
    def inner():
        global age
        age = age+10
        print(age)

    inner()
    print(age)

increaseAge()
print(age)


age = 23

def increaseAge():
    age = 20

    def inner():
        global age
        age = age + 10
        print("Inside inner:", age)

    inner()                     # <-- outside inner()
    print("Inside increaseAge:", age)

increaseAge()
print("Global:", age)



total_sales = 0.0

def record_sale(amount):
    global total_sales
    total_sales = total_sales + amount
    print(f"Sale recorded: ₦{amount:.2f}")

record_sale(4.50)
