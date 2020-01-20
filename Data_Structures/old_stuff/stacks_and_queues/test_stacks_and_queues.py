import pytest
from stacks_and_queues import Stack, Queue 

def test_stack_up(make_stack):
  assert make_stack.peek() == 5
  assert make_stack.pop() == 5
  assert make_stack.is_empty == False
  for _ in range (4):
    make_stack.pop()
  assert make_stack.is_empty()==True
  

def test_enqueue(make_q):
  assert make_q.peek() == 1
  assert make_q.dequeue() == 1
  assert make_q.is_empty == False
  for _ in range (4):
    make_q.dequeue()
  assert make_q.is_empty()==True
  

@pytest.fixture()
def make_stack ():
  ss = Stack()
  for i in range (1,6):
    ss.push(i)
  return ss

@pytest.fixture()
def make_q ():
  qq = Queue()
  for i in range (1,6):
    qq.enqueue(i)
  return qq