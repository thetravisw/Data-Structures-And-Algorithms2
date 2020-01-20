import pytest
from Data_Structures.stacks_and_queues.stacks_and_queues import Stack, Queue 
from Data_Structures.stacks_and_queues.Challenges.queue_with_stacks import Pseudo_Queue

def test_functionality():
  qq  = Pseudo_Queue()
  qq.enqueue(8)
  qq.enqueue(6)
  qq.enqueue(7)
  qq.enqueue(5)
  qq.enqueue(3)
  qq.enqueue(0)
  qq.enqueue(9)

  assert qq.dequeue() == 8
  assert qq.dequeue() == 6
  assert qq.dequeue() == 7




