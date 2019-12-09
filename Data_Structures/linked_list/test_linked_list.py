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

def test_prepend(make_list):
  ln = List_Node(4)
  make_list = make_list.prepend(ln)
  assert make_list.head.data==4

def test_to_string(make_list):
  expected = "1  2  3  4  5  6  7  8  9  "
  assert make_list.to_string() == expected

def test_contains(make_list):
  assert make_list.contains(4) == True
  assert make_list.contains(7) == True
  assert make_list.contains(11) == False
  assert make_list.contains(0) == False 

def test_insert_after(make_list):
  for i in range (0,3):
    appended_node = List_Node(2-i)
    make_list.insert_after(make_list.head.next.next,appended_node)
  expected = "1  2  3  0  1  2  4  5  6  7  8  9  "
  assert make_list.to_string() == expected

def test_final_node(make_list):
  final_node = List_Node(2)
  make_list.insert_after(make_list.tail,final_node)
  assert make_list.tail.data == 2

def test_purge_data(make_list):
  make_list.append(List_Node(2))
  make_list.remove_head()
  make_list.purge_data(2)
  assert make_list.to_string() == "3  4  5  6  7  8  9  "

def test_sum_of_list(make_list):
  assert make_list.sum_of_list() == 45

def test_nth_from_end(make_list):
  for i in range (0,5):
    assert make_list.nth_from_end(i).data == 9-i

@pytest.fixture()
def make_list ():
  ll = Linked_List()
  for i in range (1,10):
    node = List_Node(i)
    ll.append(node)
  return ll