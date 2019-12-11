class Linked_List:
  
  def __init__ (self):
    self.head = None
    self.tail = None

  def append2(self,node):
    if self.head == None:
      self.head = node
      self.tail = node
      return
    self.tail.next = node
    self.tail = node

  def remove_head(self):
    self.head = self.head.next

  def append(self, val):
    node = List_Node(val)
    if self.head == None:
      self.head=node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = node

  def prepend (self, node):
    self.head = node.next
    self.head = node

  def sum_of_list(self):
    sum=0
    current=self.head
    while current:
      sum+= current.data
      current = current.next
    return sum

  def remove_node(self,node):
    if self.head == node:
      self.head = self.head.next
    else:
      current = self.head
      while current.next != node:
        current = current.next
      node.next = node.next.next

  def purge_data(self, data):
    node=self.head
    while node.data == data:
      self.head = node.next
      node=node.next
    while node.next:
      if node.next.data == data:
        try:
          node.next = node.next.next
        except:
          node.next = None
      if node.next:
        node=node.next

  def insert_after(self, target_val, inserted_val):
    node = List_Node(inserted_val)
    current = self.head
    while current:
      if current.data == inserted_val:
        node.next = current.next
        current.next=node
        if self.tail == current:
          self.tail = node
        break
      current=current.next

  def insert_before(self, target_val, inserted_val):
    node = List_Node(inserted_val)
    if self.head.data==target_val:
      node.next=self.head
      self.head=node
    else:
      current=self.head
      while current.next:
        if current.next.data == inserted_val:
          node.next = current.next
          current.next = node
          break
        current = current.next

  def kth_from_end(self, k):
    current = self.head
    future = current
    for i in range (0,k):
      try:
        future = future.next
      except AttributeError:
        raise AttributeError 
    while future.next:
      current = current.next
      future = future.next
    return current
      
  def contains(self, target):
    found_it = False
    node = self.head
    while node:
      if node.data == target:
        found_it = True
        break
      node=node.next
    return found_it

  def __str__(self):
    results = ''
    node = self.head
    while node:
      results += str(node.data) + "  "
      node=node.next
    print(results)
    return results

  def to_string(self):
    results = ''
    node = self.head
    while node:
      results += str(node.data) + "  "
      node=node.next
    print(results)
    return results


class List_Node:
  def __init__ (self, val, next=None ):
    self.data = val
    self.next = None

