class CupNode:
    def __init__(self,data):
        self.data = data
        self.next = None

headCup = CupNode(1)
cupTwo = CupNode(2)
cupThree = CupNode(3)
cupFour = CupNode(5)

headCup.next = cupTwo
cupTwo.next = cupThree
cupThree.next = cupFour

print(headCup.next.next.next.data)