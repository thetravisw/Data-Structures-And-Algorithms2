import pytest

def test_add(ht):
  ht.add("key","value")
  assert ht.get("key") == "value"
  assert ht.contains("key") == True

def test_collisions(ht):
  ht.add("key","value1")
  ht.add("kye","value2")
  assert ht.get("key") == "value1"
  assert ht.get("kye") == "value2"

@pytest.fixture()
def ht ():
  ht = HashTable()
  return ss
