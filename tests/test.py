import os
import pytest
import sys

current = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current + '/../')

import simple

def setup_function():
    print("setup function called")

def teardown_function():
    print("teardown function called")

def test1():
    print("test1")
    assert simple.sum(1,1) == 3

def test2():
    print("test2")
    assert simple.sum(1,1) == 2

def test3():
    print("test3")
    assert simple.sum(1,1) == 1
