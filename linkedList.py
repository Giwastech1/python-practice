class CupNode:
    def __init__(self,data):
        self.data = data
        self.next = None

cup_one = CupNode(1)
cup_two = CupNode(2)
cup_three = CupNode(3)
cup_four = CupNode(4)

cup_one.next = cup_two
cup_two.next = cup_three
cup_three.next = cup_four

print(cup_one.next.next.data)
print()
print(cup_two.next.data)
print()
cup_two.next.data = 12
print(cup_two.next.data)
print()
current_node = cup_one
while(current_node is not None):
    print(current_node.data)
    current_node = current_node.next
