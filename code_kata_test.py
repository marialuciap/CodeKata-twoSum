from main import twoSum
import pytest


def test1():
    assert set([0,1]) == set(twoSum([2,7,11,15],9))

def test2():
    assert set([1,2]) == twoSum([3,2,4],6)

def test3():
    assert set([0,1]) == twoSum([3,3], 6)

def test4():
    assert  set([6,7]) == twoSum([-1,-1,-1,-1,-1,-1, 10, 0],10)

def test5():
    assert  set([0,1]) == twoSum([0,0, 10, 20, 30 ,40 ,50, 60],0)    