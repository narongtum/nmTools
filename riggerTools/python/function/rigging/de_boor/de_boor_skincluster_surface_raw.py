OPEN = 'open'
PERIODIC = 'periodic'
INDEX_TO_KNOT_TYPE = {0: OPEN, 2: PERIODIC}


verts
jnts
srf 
d=None
tol=0.000001

original_sel = om.MGlobal.getActiveSelectionList()

verts = cmds.ls(cmds.polyListComponentConversion(verts, toVertex=True), fl=True)

jnts_copy = jnts[:]