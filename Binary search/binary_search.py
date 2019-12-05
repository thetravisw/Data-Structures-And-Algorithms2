def binary_search(lst, key):
  # A simple function to locate a given Key
  # in a sorted list of numbers.
  if lst == []:
    return -1
  leftbound = 0
  rightbound = len(lst) -1

  while leftbound != rightbound:
    index = (leftbound+rightbound)//2
    if lst[index] == key:
      break
    elif lst[index] > key:
      rightbound = index
    else:
      leftbound = index 
  if lst[index] == key:
    return index
  return -1