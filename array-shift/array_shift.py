def insert_shift_array (lst, val):
  """Takes in an array (lst), and a value (val)
  returns the array with val inserted at the 
  middle index"""

  result = []
  key_index = (len(lst)+1)//2
  for i in range(0,key_index):
    result.append(lst[i])
  result.append(val)
  for i in range(key_index,len(lst)):
    result.append(lst[i])
  return result