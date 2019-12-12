from Data_Structures.linked_list.linked_list import Linked_List, List_Node
from Data_Structures.linked_list.ll_merge.ll_merge import merge_lists

def test_def_merge_lists(make_list):
  ll_b = Linked_List()
  for i in range (13):
    ll_b.append(100*i)
  assert merge_lists(make_list, ll_b).to_string() == "1  0  2  100  3  200  4  300  5  400  6  500  7  600  8  700  9  800  900  1000  1100  1200  "

  ll_a = Linked_List()
  for i in range (5):
    ll_a.append(i)

  ll_b = Linked_List()
  for i in range (2):
    ll_b.append(100*i)

  assert merge_lists(ll_a, ll_b).to_string() == "0  0  1  100  2  3  4  "

  ll = merge_lists(Linked_List(),Linked_List())
  assert ll.to_string() == ""

  ll_a = Linked_List()
  for i in range (5):
    ll_a.append(i)

  assert Linked_List().head == None

  assert merge_lists(ll_a,Linked_List()).to_string() == ll_a.to_string()

  assert merge_lists(Linked_List(),ll_a).to_string() == ll_a.to_string()

@pytest.fixture()
def make_list ():
  ll = Linked_List()
  for i in range (1,10):
    node = List_Node(i)
    ll.append2(node)
  return ll