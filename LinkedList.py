# ## # ## # ## # ## 
# A single node of data in our list
class Node:
  # constructor
  def __init__(self, value):
    # value of the node
    self.value = value
    # reference to the next node
    self.next = None

  # method override for printing
  # like __str__ but you can use any data type
  def __str__(self):
    return f'{self.value}'

# test_node = Node('test string node')
# print(test_node)

# ## # ## # ## # ## 
# the linked list 'manager' class
class LinkedList:
  def __init__(self):
    # a reference to the head (first node)
    self.head = None
    # the current size of the linked list
    self.length = -1

  # helper function that checks if the linked list is empty
  def is_empty(self):
    return self.length == -1

  # add a node to the end of the list return the new length
  def append(self, value):
    # create a new node from the given value
    new_node = Node(value)
    # check list is empty -- make the new node the head if so
    if self.is_empty():
      self.head = new_node
    else:
      # loop to the end of the linked list
      # start at the beginning (the head node)
      current_node = self.head
      while current_node.next != None:
        current_node = current_node.next
      # set the last node's next to be new node
      current_node.next = new_node

    # increment the self.length
    self.length += 1
    return self.length

  # remove the last node and return it 
  def pop(self):
    pass

  # print out out linked list 
  # def __repr__(self):
  #   pass








  # return the sum of all the values in the linked list
  def sum(self):
    pass

  # return a [list] (regular python list) from all the values in the linked list
  def to_list(self):
    pass

  # search for a given value in the list. 
  # If it is found, return True otherwise return False
  def search(self, value):
    pass
  
  # add a node with the given value to the beginning of the list
  # this doesn't need a loop -- remember the head is the beginning 
  # of the list. unshift should return the new length of the list
  def unshift(self, value):
    pass

  # reomve the value at beginning of the list
  def shift(self):
    pass

