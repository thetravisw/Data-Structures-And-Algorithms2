from Data_Structures.linked_list import Linked_List

def merge_lists (list_a, list_b):
  results = Linked_List()
  if list_a.head == None:
    return list_b
  if list_b.head == None:
    return list_a
  a = list_a.head
  b = list_b.head
  results.head = a
  if a == None:
    results.head = b
  if a != None:
    while a.next and b.next:
      a.next, b.next, a, b = b, a.next, a.next, b.next
    if a.next:
      a.next, b.next = b, a.next
    else:
      if b.next:
        a.next=b
  return results
