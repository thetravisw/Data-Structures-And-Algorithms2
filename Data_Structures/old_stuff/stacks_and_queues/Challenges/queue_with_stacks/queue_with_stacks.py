from Data_Structures.stacks_and_queues.stacks_and_queues import *

class Pseudo_Queue:
  def __init__(self):
    
    self.s1 = Stack()
    self.s2 = Stack()

  def enqueue(self, val):
    node = Node(val)
    while self.s1.head:
      v = self.s1.pop()
      self.s2.push(v)
    self.s2.push(val)
    while self.s2.head:
      v = self.s2.pop()
      self.s1.push(v)

  def dequeue (self):
    if self.s1.head:
      return self.s1.pop()
    return "Queue is empty"

  

