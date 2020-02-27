"""
:Author JP Haupt
:Date 25 Feb 2020

Pytests for the shapes module

note: this is also my first time using pytest, so this may contain some code for
me just messing around to get the hang of it.

note: must start name of test function with "test"
"""

# import "../src/shapes"
from ..src import shapes
from meep import Vector3 as V # shorthand due to laziness

def test_dummy():
    assert True
    assert not False
    # assert False 

def test_pyramid_contains():
    """
    tests the Pyramid class's contains(point) method

    TODO test *without* counterclockwise ordering
    """
    v = V(1,1,1) # constant offset to be away from origin
    # base and apex
    # NOTE b's must be listed clockwise w.r.t. a
    b1=V(0,0,0)+v
    b2=V(0,1,0)+v
    b3=V(1,1,0)+v 
    b4=V(1,0,0)+v
    a =V(0.5,0.5,1)+v

    pyr = shapes.Pyramid(a,b1,b2,b3,b4)
    
    # check point obviously not in pyramid
    assert not pyr.contains(V(10,10,10)+v)

    # check point inside pyramid 
    assert pyr.contains(V(0.5,0.5,0.5)+v)

    # check point inside block but outside pyramid
    assert not pyr.contains(V(0.9,0.9,0.9)+v)

    # check centre of base 
    assert pyr.contains(V(0.5,0.5,0)+v)