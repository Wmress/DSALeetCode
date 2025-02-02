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
        #create a new node with the value stored in the node
        new_node = Node(value)
        #if there is no node in the list
        if self.head == None:
            #then set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            #add the node to the end of the list
            self.tail.next = new_node
            self.tail = new_node
        #expand the length by one
        self.length += 1

my_linked_list = LinkedList(1)    

my_linked_list.append(2)

my_linked_list.print_list()