from collections import deque
#stack with class
class FoodStack:
    def __init__(self):
        self.food = []

    def updateFood(self,foodItem):
        self.food.append(foodItem)
        return self.food
    
    def deleteFood(self):
        self.food.pop()
        return self.food



myFood = FoodStack()
myFood.updateFood("Amala")
myFood.updateFood("Pap")
myFood.updateFood("Rice")

print(myFood.food)

print(myFood.deleteFood())
print(myFood.food)

# Queue with class
class BookQueue:
    def __init__(self):
        self.book = deque()

    def updateBook(self,item):
        self.book.append(item)
        return self.book

    def deleteBook(self):
        return self.book.popleft()

myBook = BookQueue()
myBook.updateBook("Physics")
myBook.updateBook("Chemistry")
myBook.updateBook("Biology")
print(myBook.book)

myBook.deleteBook()
print(myBook.book)


# simulating queue and dique without dique()
class FriendClass:
    def __init__(self):
        self.myFriend = []

    def updateFriend(self,friend):
        self.myFriend.append(friend)
        return self.myFriend

    def deleteFriend(self):
        self.myFriend.pop()
        return self.myFriend


friendList = FriendClass()
friendList.updateFriend("Amaka")
friendList.updateFriend("Ngozi")
friendList.updateFriend("Ade")
print(friendList.myFriend)

friendList.deleteFriend()
print(friendList.myFriend)
print(friendList.myFriend)

friendList.deleteFriend()
print(friendList.myFriend)

#Try and catch in python
try:
    num = int(input("Enter a number: "))
    print(f"Your input is {num}")
except ValueError:
    print("Enter a valid number")