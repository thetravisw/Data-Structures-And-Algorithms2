class Linked_List:
  
  def __init__ (self):
    self.head = None
    self.tail = None

  def append(self,node):
    if self.head == None:
      self.head = node
      self.tail = node
      return
    self.tail.next = node
    self.tail = node

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

  def remove_head(self):
    self.head = self.head.next

  def remove_non_head_node(self,node_before_target):
    node_before_target.next = node_before_target.next.next

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

  def insert_after(self, target_node, inserted_node):
    inserted_node.next = target_node.next
    target_node.next = inserted_node
    if self.tail == target_node:
      self.tail = inserted_node

  def nth_from_end(self, n):
    current = self.head
    future = current
    for i in range (0,n):
      if future.next:
        future = future.next
      else:
        return "Too Small"
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

