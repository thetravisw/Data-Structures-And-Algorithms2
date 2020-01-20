from array_shift import insert_shift_array

def test_AS1():
  expected = [7]
  actual = insert_shift_array([],7)
  assert actual == expected

def test_AS2():
  expected = [8,6,7,5,3,0,9]
  actual = insert_shift_array([8,6,7,3,0,9],5)
  assert actual == expected

def test_AS3():
  expected = [1,2,3,4]
  actual = insert_shift_array([1,2,4],3)
  assert actual == expected