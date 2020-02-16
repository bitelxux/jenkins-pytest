import os
import pytest
import sys

current = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current + '/../')

import simple

def setup_function():
    pass

def teardown_function():
    pass

def test1():
    assert simple.sum(1,1) == 2

def test2():
    assert simple.sum(1,1) == 2

def test3():
    assert simple.sum(1,1) == 2
