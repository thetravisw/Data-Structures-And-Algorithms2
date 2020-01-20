import pytest
from Data_Structures.stacks_and_queues.stacks_and_queues import Stack, Queue 
from Data_Structures.stacks_and_queues.Challenges.fifo_animal_shelter import FifoAnimalShelter, Cat, Dog

def test_null():
  shelter = FifoAnimalShelter()
  assert shelter.dequeue("dog") == "No animals in the shelter"

def test_no_correct_animal():
  shelter = FifoAnimalShelter()
  shelter.enqueue(Cat())
  assert shelter.dequeue("dog") == "no dogs in the shelter.  Perhaps you want a dinosaur instead?"

def test_normal_functionality():
  shelter = FifoAnimalShelter()
  shelter.enqueue(Cat())
  shelter.enqueue(Dog())
  shelter.enqueue(Dog())
  shelter.enqueue(Cat())
  animal = shelter.dequeue("dog")
  assert animal.type == "dog"
  animal = shelter.dequeue()
  assert animal.type == "cat"
