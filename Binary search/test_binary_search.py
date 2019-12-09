from binary_search import binary_search

def test_null_case():
  expected = -1
  actual = binary_search([],666)
  actual = -1
  assert actual == expected

def test_lsc():
  expected = 1
  actual = binary_search([0,1],1)
  assert actual == expected

def test_lsc2():
  expected = 0
  actual = binary_search([0,1],0)
  assert actual == expected

def test_linerar_case():
  expected = 1
  actual = binary_search([1,2,3],2)
  assert actual == expected

def test_left_hand_path():
  expected = 1
  actual = binary_search([0,1,2,3,4],1)
  assert actual == expected

def test_right_hand_path():
  expected = 3
  actual = binary_search([0,1,2,3,4],3)
  assert actual == expected


def test_larger_list_size():
  expected = 2
  actual = binary_search([1,2,3,4,5,6,7,8,9,10,11,12,42],3)
  assert actual == expected


def fail_left():
  expected = -1
  actual = binary_search([1,2,3,4,5,6,7,8,9,10,11,12],-5)
  assert actual == expected

def fail_right():
  expected = -1
  actual = binary_search([1,2,3,4,5,6,7,8,9,10,11,12],55)
  assert actual == expected
