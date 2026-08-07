# turples
signature = ("Vanilla", "Caramel", "Hazelnut")
print(type(signature))
first_flavor = signature[1]
print(first_flavor)
print(signature[-3])
print(signature[-2])

signature_blend = ("Vanilla", "Caramel", "Hazelnut")
print(f"To make the House Blend, use: {signature_blend[0]} and {signature_blend[1]}")

# unpacking turple
baking_recipe = ("sugar","flour","egg","water","salt")
first_recipe,second_recipe,third_recipe,fourth_recipe,fiffh_recipe = baking_recipe
print(third_recipe)

# first name and rest
qualified_name = ("Giwa","James","Bola","Ade")
first_name, *others = qualified_name
print(first_name)
print(others)

# Ommit name/names
first_name,_,second_name,_, = qualified_name
print(second_name)


# Dictionary
my_data = {
    "name": "Giwa",
    "age": 16,
    "school": "Learn2earn",
    "course": "Software engineering"
}
friend = "Hassan"

print(my_data)
my_age = my_data["age"]
print(my_age)

print(friend)
friend = my_data.get("friend","not available")
print(friend)

print(my_data.get("age"))

# set
fruit = {"Apple","Mango","Banana"}
print("Apple" in fruit)
print("mango" in fruit)
print("Mango" in fruit)

print(fruit)
print()
set_a = {"Vanilla", "Caramel", "Mocha"}
set_b = {"Caramel"}
print(set_a - set_b)
print()
first_set = {"school","book","pen","eraser"}
second_set = {"book","sharpner","eraser"}

combine_list = first_set | second_set
print(combine_list)

mutual_list = first_set & second_set
print(mutual_list)

print(first_set & second_set)
print(first_set | second_set)
print()
# set add and update
student_name = {"Giwa","Ajayi","Wale","Samuel"}
student_name.add("Bola")
print(student_name)

# student_name.update(["ibrahim","ismail"])
# print(student_name)
add_name = ["ibrahim","ismail"]
student_name.update(add_name)
print(student_name)

student_name.remove("Giwa")
print(student_name)