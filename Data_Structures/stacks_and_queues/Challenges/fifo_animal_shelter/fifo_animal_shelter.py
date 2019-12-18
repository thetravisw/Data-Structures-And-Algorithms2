from Data_Structures.stacks_and_queues.stacks_and_queues import *
class Cat:
  def __init__(self):
    self.type="cat"

class Dog:
  def __init__(self):
    self.type="dog"


class FifoAnimalShelter:
  def __init__(self):
    
    self.s1 = Stack()
    self.s2 = Stack()

  def enqueue(self, animal):
    while self.s1.head:
      v = self.s1.pop()
      self.s2.push(v)
    self.s2.push(animal)
    while self.s2.head:
      v = self.s2.pop()
      self.s1.push(v)

  def dequeue (self, pref=None):
    if self.s1.head:
      if pref == None:
        return self.s1.pop()
      else:
        results = None
        while self.s1.head:
          node = self.s1.pop()
          if node.type == pref:
            results = node
            break
          else:
            self.s2.push(node.data)
        while self.s2.head:
          self.s1.push(self.s2.pop().data)
      if results == None:
        results = f"no {pref}s in the shelter.  Perhaps you want a dinosaur instead?"
      return results
    return "No animals in the shelter"