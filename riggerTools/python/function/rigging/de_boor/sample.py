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
jnts = hh.list_joints_from_skincluster('skinCluster5')
'''
jnts = [
    ['j00', 'j01', 'j02'],  # V = 0
    ['j10', 'j11', 'j12'],  # V = 1
    ['j20', 'j21', 'j22']   # V = 2
]
'''
hs.split_with_surface(mesh, jnts, surface, d=None, tol=0.000001, visualize=True)