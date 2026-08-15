#stack with class
class FoodStack:
    def __init__(self):
        self.food = []

    def updateFood(self,foodItem):
        foodList = self.food.append(foodItem)
        return foodList
    
    def deleteFood(self):
        foodList = self.food.pop()
        return foodList



myFood = FoodStack()
myFood.updateFood("Amala")
myFood.updateFood("Pap")
myFood.updateFood("Rice")

print(myFood.food)

print(myFood.deleteFood())
print(myFood.food)