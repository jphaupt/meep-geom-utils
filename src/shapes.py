"""
:Author JP Haupt
:Date 17 February 2020

class definitions for Shape objects

definition for the general Shape object, as well as specific examples (pyramid,
etc.). A Shape object is part geometric shape of some sort (sphere, oblique 
cone, etc.) along with a Material as defined in the meep library. 

The whole motivation for me writing this package is that I felt meep did not
handle custom shapes very well, and that their selection of shapes is rather
limited.
"""

import meep as mp 

class Shape(object):
    def __init__(self, material=mp.Medium()):
        self.material = material 
    # TODO stub

    # abstract method 
    # TODO figure out how to do this properly
    def contains(self, point):
        """
        checks if the Shape contains the given 3-d point 
        
        :param point: point to check if inside Shape
        :type point: mp.Vector3
        """
        pass 

class Block(Shape):
    print("stub")
    # TODO stub
    # basically copying Meep's Block object, as a test

class Pyramid(Shape):
    def __init__(self, apex, b1, b2, b3, b4, **kwargs):
        """
        initialises a rectangular pyramid object with points on the pyramid 
        given by vectors b1,b2,b3,b4 and the apex vector
        
        geometric object for a pyramid with some medium and consisting of points
        b1,b2,b3,b4 (on the rectangular base) and apex (the apex). Supports 
        oblique rectangular pyramids as well 

        TODO explain how it saves the normal vectors upon initialisation
        
        :param Shape: [description]
        :type Shape: [type]
        :param apex: the apex of the pyramid
        :type apex: mp.Vector3
        :param b1: one of the vertices for the rectangular base of the pyramid
        :type b1: mp.Vector3
        :param b2: one of the vertices for the rectangular base of the pyramid
        :type b2: mp.Vector3
        :param b3: one of the vertices for the rectangular base of the pyramid
        :type b3: mp.Vector3
        :param b4: one of the vertices for the rectangular base of the pyramid
        :type b4: mp.Vector3
        """
        # TODO initialise pyramid
        print("stub")
        super(Pyramid, self).__init__(**kwargs)

    # override the contains function 
    def contains(self, point):
        print("stub")
    print("stub")
    # TODO stub
    # TODO prioritise this one!

class Cone(Shape):
    print("stub")
    # TODO stub
    # NOTE this could be a slanted (oblique) cone!
