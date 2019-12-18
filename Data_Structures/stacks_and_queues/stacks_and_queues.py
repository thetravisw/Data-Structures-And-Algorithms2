class Node:
  data = None
  next = None

  def __init__(self, val):
    self.data = val

class Stack:
  def __init__(self):
    head = None
    
  def push(self, val):
    """pushes a value to the stack"""
    node = Node(val)
    if not self.head:
      self.head = node
    else:
      self.head, node.next = node, self.head

  def pop(self):
    """Pops off the top Node"""
    data = self.head.data
    if self.head.next:
      self.head.next, self.head = None, self.head.next
    else: self.head == None

  def peek(self):
    """Returns the data of the top node"""
    if self.head:
      return self.head.data
    else:
      return None

  def is_empty(self):
    return self.head == None

class Queue:

  def __init__(self):
    self.back = None
    self.front = None

  def enqueue(self,val):
    """Enqueue's a value"""
    node = Node(val)
    if self.back == None:
      self.back, self.front = node, node
    else:
      self.back, self.back.next = node, node

  def dequeue (self):
    """removes the node from the front and returns it's data"""
    data = self.front.data
    if self.front.next:
      self.front, self.front.next  = self.front.next, None
    else:
       self.front = None
    return data

  def peek (self):
    """returns the data of the front node"""
    if self.front:
      return self.front.data
    else:
      return None

  def is_empty (self):
    return self.front == None 