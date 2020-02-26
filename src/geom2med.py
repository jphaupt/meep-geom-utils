"""
:author: JPHaupt
:date: 26 Feb 2020

simple module that contains a function that takes a list of mp.GeometricObject
and Shape and returns a function of mp.Vector3 that returns the medium at that
point
"""

import meep as mp
import src.shapes

def geom2med(geometries):
    """
    takes a mixed list of mp.GeometricObject and Shape (defined in this module)
    and returns a function of mp.Vector3 that returns the medium at the point
    
    :param geometries: list of geometric objects/shapes
    :type geometries: [mp.GeometricObject or Shape]
    """
    # TODO stub 
    print("stub")