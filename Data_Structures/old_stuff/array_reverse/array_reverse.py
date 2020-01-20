def ArrayReverse(arr):
  output = []
  size = len(arr)
  for i in range (0, size):
    data = arr[size-(i+1)]
    output.append(data)
  return output