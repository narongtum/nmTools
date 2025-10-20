from function.rigging.autoRig.base import core
reload(core)

# Define the necessary variables
zro_grp = 'L_pinStrap02Zro_grp'  # Zero out group
ctrl = 'L_pinStrap02_ctrl'
local_obj = 'upperArmLFT_bJnt'  # Parent object to assign in local space
world_obj = 'ctrl_grp'  # Parent object to assign in world space
base_grp = 'L_pinStrap02Offset_grp'  # Offset group
body_part = 'L_pinStrap02'
attr_occur = 'L_pinStrap02_ctrlShape' # attr occur at
no_touch_grp = 'noTouch_grp'
prior_ctrl = 'clvLFTGmbl_ctrl'

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

try:
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
		loc_grp.name = body_part + '_local_grp'
		wor_grp.name = body_part + '_world_grp'
	else:
		loc_grp.name = 'local'
		wor_grp.name = 'world'

	# Orient constraints
	world_grp_cons = core.orientConstraint(world_obj, wor_grp, mo=True)
	world_grp_cons.name = body_part + 'World'
	world_grp_cons.suffix

	base_grp_base_cons = core.orientConstraint(loc_grp, wor_grp, local_world_grp)
	base_grp_base_cons.name = body_part + 'Base'
	base_grp_base_cons.suffix

	reverse_node_rev = core.Reverse()
	reverse_node_rev.name = body_part + '_rev'

	# Set up attributes for switching between local and world space
	controller_shape = core.Dag(attr_occur)
	attr = 'localWorld'
	controller_shape.addAttribute(ln=attr, k=True, min=0, max=1)

	# Connect attributes
	controller_shape.attr(attr) >> base_grp_base_cons.attr('w1')
	controller_shape.attr(attr) >> reverse_node_rev.attr('ix')
	reverse_node_rev.attr('ox') >> base_grp_base_cons.attr('w0')

	# Parent local and world groups to prior controller (prevent cycle warning)
	loc_grp.parent(prior_ctrl)
	wor_grp.parent(prior_ctrl)

	# Clear selection and indicate completion
	core.clearSel()
	print('\n# # # DONE')

	# Optional: Return the created objects if needed
	# return loc_grp, wor_grp, world_grp_cons, base_grp_base_cons, reverse_node_rev

except Exception as e:
	print(f"An error occurred: {e}")
	raise
