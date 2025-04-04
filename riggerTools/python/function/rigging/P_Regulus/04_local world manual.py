from function.rigging.autoRig.base import core
reload(core)


#... Define the necessary variables
zro_grp = 'spine03Zro_grp'  # Zero out group
ctrl = 'spine03_ctrl'
local_obj = 'spine02_bJnt'  # Parent object to assign in local space
world_obj = 'ctrl_grp'  # Parent object to assign in world space
base_grp = 'spine03Offset_grp'  # Offset group
body_part = 'spine03'
attr_occur = 'spine03_ctrlShape'
still_grp = 'noTouch_grp'


# def create_localWorld(zro_grp,ctrl,local_obj,world_obj,base_grp,body_part,attr_occur ):
# Function to check if an object exists

def check_obj_exists(obj_name):
	if not mc.objExists(obj_name):
		raise ValueError(f"Object '{obj_name}' does not exist.")

# Check if all necessary objects exist
try:
	check_obj_exists(zro_grp)
	check_obj_exists(local_obj)
	check_obj_exists(world_obj)
	check_obj_exists(base_grp)
	check_obj_exists(attr_occur)
except ValueError as e:
	print(e)
	raise SystemExit(f"Error: {e}")


# Create a null group under zero group
local_world_grp = core.Null(body_part + 'LocalWorld_grp')
local_world_grp.snap(base_grp)
local_world_grp.parent(zro_grp)

# Parent control under it
base_grp = core.Dag(base_grp)
base_grp.parent(local_world_grp)

# Create and snap local and world groups
loc_grp = core.Null()
wor_grp = core.Null()
loc_grp.snap(base_grp)
wor_grp.snap(base_grp)

# Assign names to local and world groups
if body_part:
	loc_grp.name = body_part + '_local'
	wor_grp.name = body_part + '_world'
else:
	loc_grp.name = 'local'
	wor_grp.name = 'world'

# Orient constraints
world_grp_cons = core.orientConstraint(world_obj, wor_grp, mo=True)
base_grp_base_cons = core.orientConstraint(loc_grp, wor_grp, local_world_grp)
reverse_node_rev = core.Reverse()
reverse_node_rev.name = body_part + '_rev'

# Set up attributes for switching between local and world space
controller_shape = core.Dag(attr_occur)
attr = 'localWorld'
controller_shape.addAttribute(ln=attr, k=True, min=0, max=1)

#... Connect attributes
controller_shape.attr(attr) >> base_grp_base_cons.attr('w1')
controller_shape.attr(attr) >> reverse_node_rev.attr('ix')
reverse_node_rev.attr('ox') >> base_grp_base_cons.attr('w0')


#... create top grp
top_grp = core.Null(f'{body_part}LocalWorld_grp')
top_grp.parent(still_grp)
#... Parent local and world groups
loc_grp.parent(still_grp)
loc_grp_cons = core.orientConstraint(local_obj, loc_grp, mo=True)
loc_grp_cons.name = f'{body_part}Local_grp'
wor_grp.parent(still_grp)
wor_grp_cons = core.orientConstraint(world_obj, wor_grp, mo=True)
wor_grp_cons.name = f'{body_part}World_grp'

#... Clear selection and indicate completion
core.clearSel()
print('\n# # # DONE # # #')

# Optional: Return the created objects if needed
# return loc_grp, wor_grp, world_grp_cons, base_grp_base_cons, reverse_node_rev









# create_localWorld(zro_grp,ctrl,local_obj,world_obj,base_grp,body_part,attr_occur )