from linked_list import Linked_List, List_Node
import pytest

def test_new_null_list():
  ll = Linked_List()
  assert ll.head == None

def test_create_and_append(make_list):
  assert make_list.head.data==1
  assert make_list.head.next.data==2
  assert make_list.head.next.next.data==3
  assert make_list.tail.data == 9

def test_prepend():
  ll = Linked_List()
  ll.prepend(List_Node(11))
  assert ll.head.data==11
  ll.prepend(List_Node(4))
  assert ll.head.data==4

def test_to_string(make_list):
  expected = "1  2  3  4  5  6  7  8  9  "
  assert make_list.to_string() == expected

def test_contains(make_list):
  assert make_list.contains(4) == True
  assert make_list.contains(7) == True
  assert make_list.contains(11) == False
  assert make_list.contains(0) == False 

def test_purge_data(make_list):
  make_list.append2(List_Node(2))
  make_list.remove_head()
  make_list.purge_data(2)
  assert make_list.to_string() == "3  4  5  6  7  8  9  "

def test_sum_of_list(make_list):
  assert make_list.sum_of_list() == 45

def test_kth_from_end(make_list):
  for i in range (0,5):
    assert make_list.nth_from_end(i).data == 9-i
  with pytest.raises(AttributeError):
    make_list.nth_from_end(11)
  with pytest.raises(AttributeError):
    make_list.nth_from_end(9)

def test_append(make_list):
  make_list.append(4)
  assert make_list.to_string() == "1  2  3  4  5  6  7  8  9  4  "

def test_insert_after(make_list):
  make_list.insert_after(3,3)
  make_list.insert_after(3,3)
  assert make_list.to_string() == "1  2  3  3  3  4  5  6  7  8  9  "

@pytest.fixture()
def make_list ():
  ll = Linked_List()
  for i in range (1,10):
    node = List_Node(i)
    ll.append2(node)
  return ll