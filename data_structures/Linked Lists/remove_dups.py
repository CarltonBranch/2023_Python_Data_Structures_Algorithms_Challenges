class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next_node = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            runner = self.head
            while runner.next_node:
                runner = runner.next_node
            runner.next_node = new_node
        self.size += 1

    def print(self):
        runner = self.head
        if runner is None:
            print("Linked list is empty")
        while runner:
            print(f'{runner.value}', end="")
            runner = runner.next_node
            if runner:
                print(' >> ', end="")
        print()

    def remove_dups(self):
        runner = self.head
        while runner:
            target = runner.value
            front_runner = runner
            while front_runner and front_runner.next_node:
                if front_runner.next_node.value == target:
                    front_runner.next_node = front_runner.next_node.next_node
                front_runner = front_runner.next_node
            runner = runner.next_node
        self.size -= 1


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.print()
l.remove_dups()
l.print()
