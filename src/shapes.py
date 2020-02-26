"""
:author JP Haupt
:date 17 February 2020

class definitions for Shape objects

definition for the general Shape object, as well as specific examples (pyramid,
etc.). A Shape object is part geometric shape of some sort (sphere, oblique 
cone, etc.) along with a Material as defined in the meep library. 

The whole motivation for me writing this package is that I felt meep did not
handle custom shapes very well, and that their selection of shapes is rather
limited.
"""

import meep as mp 


class Plane(object):
    """
    a plane parametrised by a normal vector and a point in the plane, useful for
    polyhedron shapes.
    """
    def __init__(self, normal, point):
        self.n = normal
        self.p = point
    
    def sameSide(self, point):
        # TODO 
        v = point - self.p 
        proj = v.cdot(self.n)
        return (proj > 0)

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

        :returns: whether or not the point is inside the Shape
        :type: bool

        .. note:: points on the surface of the Shape is considered inside 
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

        .. note:: currently, we require that the points on the base of the 
                pyramid be given counterclockwise relative to outside (i.e. side
                **without** the apex). 
        
        TODO remove this requirement (in the note above)
        """
        # TODO implement such that we don't need to add them counterclockwise
        self.planes = []
        # make base normal (pointing outside), partner with arbitrary point 
        base_normal = (b2-b1).cross(b3-b1)
        self.planes.append(Plane(base_normal, b1))

        # make triangular sides' normals, partner with (apex) point
        # TODO carefully proofread with diagrams
        # TODO ? normalise the normal vectors? not sure if matters
        n1 = (apex-b1).cross(b2-b1)
        # n1 /= n1.norm()
        self.planes.append(Plane(n1, apex))
        n2 = (apex-b2).cross(b3-b2)
        # n2 /= n2.norm()
        self.planes.append(Plane(n2, apex))
        n3 = (apex-b3).cross(b4-b3)
        # n3 /= n3.norm()
        self.planes.append(Plane(n3, apex))
        n4 = (apex-b4).cross(b1-b4)
        # n4 /= n4.norm()
        self.planes.append(Plane(n4, apex))

        # do the rest, i.e. material
        super(Pyramid, self).__init__(**kwargs)

    # override the contains function 
    def contains(self, point):
        """
        checks to see if the point is in the pyramid or not

        this is achieved by taking the projection of the vector connecting a 
        point on a given plane to the point in question onto the normal vector 
        of that same plane. If all of these projections are nonpositive, then 
        the point is inside the pyramid. If any one of them is positive, then it
        is outside the pyramid.
        
        :param point: a point to be checked if inside or outside the pyramid
        :type point: mp.Vector3
        """
        for plane in self.planes:
            if plane.sameSide(point):
                return False 
        return True
    # TODO prioritise this one!

class Cone(Shape):
    print("stub")
    # TODO stub
    # NOTE this could be a slanted (oblique) cone!
