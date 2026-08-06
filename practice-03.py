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
