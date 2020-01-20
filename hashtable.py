import math 

class HashTable:
  """Key should be a string, values can be anything"""
  def __init__(self, size=1024):
    self.size = size
    self.arr = [0] * size

  def add(self, key, value):
    """Adds a key to the HT"""
    index = self.hash(key)
    while self.arr[index] != 0:
      if self.arr[index][0] == key : break ## key was previously added to HashTable at this index
      index = index+1 %self.size
    self.arr[index]= (key,value)

  def get (self, key):
    """Gets the value of a key"""
    index = self.hash(key)
    while True:
      if self.arr[index] == 0:
        return "Key not in Table"
      elif self.arr[index][0] == key:
        break
      else:
        index +=1
    return self.arr[index][1]

  def contains (self, key):
    index = self.hash(key)
    while True:
      if self.arr[index] == 0:
        return False
      elif self.arr[index][0] == key:
        return True
      else:
        index +=1

  def hash(self,key):
    num = self._numberize(key)
    hash_const = math.e**2
    hashed_key = num * hash_const
    hashed_key = hashed_key - int(hashed_key)
    return int(hashed_key*self.size)

  def _numberize(self,key):
    results = 0
    for character in key:
      results += ord(character)
    return results
