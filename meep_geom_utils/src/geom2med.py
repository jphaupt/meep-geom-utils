"""
:author: JPHaupt
:date: 26 Feb 2020

simple module that contains a function that takes a list of mp.GeometricObject
and Shape and returns a function of mp.Vector3 that returns the medium at that
point
"""

import meep as mp
from src import shapes

def geom2med(geometries, point, default_material=mp.Medium(epsilon=1.0)):
    """
    takes a mixed list of mp.GeometricObject and Shape (defined in this module)
    and returns a function of mp.Vector3 that returns the medium at the point
    
    :param geometries: list of geometric objects/shapes
    :type geometries: [mp.GeometricObject or Shape]
    :param point: point to be checked for medium
    :type point: mp.Vector3
    :default_material: the material to be chosen if point not in any of the objects
                        Default is air (epsilon=1.0)
    :type default_material: mp.Medium
    """
    return lambda v: _geom2med_helper(geometries, v, default_material)

def _geom2med_helper(geometries, point, default_material):
    """
    Function that geom2med wraps around 
    """
    for geom in geometries:
        if isinstance(geom, mp.GeometricObject):
            if mp.is_point_in_object(point, geom):
                return geom.material
        elif isinstance(geom, shapes.Shape):
            if geom.contains(point):
                return geom.material 
    return default_material