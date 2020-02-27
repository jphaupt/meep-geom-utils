
"""
TODO proper documentation

TODO inverted pyramid

TODO add extra utility functions in the module like as written in free_si.py
"""
import meep as mp 
from meep import Vector3 as V # lazy shorthand
# TODO figure out how to import properly (i.e. not needing to be in this folder)
import meep_geom_utils as mp_util
from meep_geom_utils.src.shapes import Pyramid
from meep_geom_utils.src.geom2med import geom2med
from meep.materials import cSi 
from matplotlib import pyplot as plt 
from math import pi, tan, sin

# sx = 

# NOTE I am copying Yi-Peng's code, including naming convention

t1_ARC = 0.1 # first ARC layer thickness 
t2_ARC = 0.045 # second ARC layer thickness
n1_ARC = 1.4 # first ARC layer index of refraction
n2_ARC = 2.6 # second ARC layer index of refraction

H = 10.0 # semiconductor wafer thickness
t_PEC = 0.1 # 0.1 # PEC thickness
t_sio2 = 0.05 # sio2 thickness 
n_sio2 = 1.45 # sio2 index of refraction

# TODO I will probably handle this a little differently
L = 2.5 # pyramid side length
h = tan(54.7*pi/180)*L/2 # pyramid height
b = L/2 # centre to vetex of pyramid base 

h1_ARC = t1_ARC/(sin(35.3*pi/180))
h2_ARC = t2_ARC/(sin(35.3*pi/180))

# TODO I will probably have to handle this differently because of MEEP
lay_pml = 0.5 # PML thickness 
lay_refl = 0 + lay_pml # reflection plane 
lay_tfsf = lay_refl + lay_pml/2.0 # field scattering plane
lay_arc1 = lay_tfsf + lay_pml        #      start of first ARC
lay_arc2 = lay_arc1 + h1_ARC        #      start of second ARC
lay_si = lay_arc2 + h2_ARC        #      start of SI
lay_sio2 = lay_si + H   #      start of SiO2
lay_PEC = lay_sio2 + t_sio2        #      start of PEC
lay_tran = lay_PEC+lay_pml       #      transmission plane
h_bound = lay_tran + lay_pml   #      total cell boundary

dr = 0.02 # TODO this is the EMTL parameter
resolution = 1 / dr # I *think* this is the relation between EMTL & MEEP
k = mp.Vector3(0,0,0) # makes PBC
pml_layers = [mp.PML(lay_pml, direction=mp.Z, side=mp.ALL)]
# TODO what is CPML_TYPE in Yi-Peng's code? 

# TODO tmp -- resize after viewing
sx = 10
sy = 10
sz = 10

# recall: **must** put in anticlockwise order!
b1 = V(L/2, L/2, 0)
b2 = V(-L/2, L/2, 0)
b3 = V(-L/2, -L/2, 0)
b4 = V(L/2, -L/2, 0)
apex = V(0,0,-h)
tmp_pyr = Pyramid(apex, b1, b2, b3, b4, material=cSi)

# wavelengths 
# 400-1100 nm => 0.4-1.1 um
wvl_min = 0.3 # minimum wavelength
wvl_max = 1.2 # maximum wavelength

freq_min = 1/wvl_max
freq_max = 1/wvl_min
freq_centre = (freq_max+freq_min)/2
freq_width = freq_max-freq_min

tmp_source = [mp.Source(mp.GaussianSource(frequency=freq_centre, width=freq_width),
                        component=mp.Ex, 
                        center=mp.Vector3(0, 0, 0.5*sz-lay_pml-0.25),
                        # size=mp.Vector3(sx-2*pml_width,sy-2*pml_width,0))]
                        size=mp.Vector3(sx,sy,0))]

sim = mp.Simulation(cell_size=V(sx,sy,sz),
                    boundary_layers=pml_layers,
                    resolution=resolution,
                    k_point=k,
                    sources=[tmp_source],
                    material_function=geom2med([tmp_pyr]),
                    extra_materials=[cSi]) # TODO not sure if extra_materials right 

plt.figure()
sim.plot2D(output_plane=mp.Volume(center=mp.Vector3(0,0,0), size=mp.Vector3(sx,sy,0)))
plt.savefig('tmp.png')

# pt = mp.Vector3(0, 0, -0.5*sz+lay_pml+0.5)
# sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Ex, pt, 1e-12))

# mp.perfect_electric_conductor