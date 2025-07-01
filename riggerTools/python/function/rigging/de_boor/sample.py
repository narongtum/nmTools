#.................................... splite weight to curve

from function.rigging.de_boor import hh_de_boor_to_curve as hh
reload(hh)
#... smooth weight 
jnts = hh.list_joints_from_skincluster('skinCluster4')

hh.split_curve_cvs_with_de_boor_v4(jnts, 'ik_crv', degree=3)


#.................................... splite weight to mesh
from function.rigging.de_boor import hh_de_boor_to_mesh as hm
reload(hm)
jnts = hh.list_joints_from_skincluster('skinCluster5')

hm.split_with_curve_to_mesh_V2('mesh', jnts, 'ik_crv', d=None, tol=0.000001)



#.................................... splite weight to nurbe surface
from function.rigging.de_boor import hh_de_boor_to_surface as hs
reload(hs)

hs.split_with_surface(mesh, jnt_grid, surface, d=None, tol=0.000001, visualize=True)