class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

        def print_list(self):
            #set a temp var to the head of the list
            temp = self.head
            #if temp has a value then run this loop
            while temp is not None:
                #print the value stored in temp
                print(temp.value)
                #set temp to the next node
                temp = temp.next

        def append(self, value):
            new_node = Node(value)
            temp = self.head
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.lenght += 1
            return True
            

my_linked_list = LinkedList(4)

print(my_linked_list)