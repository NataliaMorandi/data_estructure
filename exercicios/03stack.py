class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def add(self, new_node):
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.height += 1

    def remove(self):
        if self.top == None:
            print("empty stack")
        else:
            pointer = self.top
            self.top = self.top.next
            pointer.next = None
            self.height -= 1
            return pointer.value

    def print_stack(self):
        if self.top == None:
            print("empty stack")
        else:
            pointer = self.top
            while pointer:
                print(pointer.value)
                pointer = pointer.next
            print(self.height)


stack = Stack('AB')

n2 = Node('CD')
n3 = Node('EF')

stack.add(n2)
stack.add(n3)
stack.print_stack()
print(stack.remove(), '\n')
stack.print_stack()
