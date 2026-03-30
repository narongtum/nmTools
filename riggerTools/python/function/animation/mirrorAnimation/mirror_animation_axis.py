import maya.cmds as mc

def mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
						  side_from="RGT", 
						  side_to="LFT",
						  invert_tx=True, invert_ty=False, invert_tz=False, 
						  invert_rx=False, invert_ry=True, invert_rz=True,
						  auto_key=False):
	"""
	Mirrors Local Transforms by multiplying -1 on specified channels.
	Perfect for mirroring animation poses while keeping the Graph Editor clean.
	"""
	
	# 1. Get Source Selection
	selection = mc.ls(sl=True)
	if not selection:
		mc.warning("Please select a source controller to mirror.")
		return

	source = selection[0]
	
	# 2. String Manipulation for Target
	short_name = source.split(':')[-1]
	
	# Bi-directional replace logic
	if side_from in short_name:
		target_short_name = short_name.replace(side_from, side_to)
	elif side_to in short_name:
		target_short_name = short_name.replace(side_to, side_from)
	else:
		target_short_name = short_name # Center controls
		
	target = "{}:{}".format(target_ns, target_short_name)
	
	if not mc.objExists(target):
		mc.error("Target object not found: {}".format(target))
		return

	# 3. Channel Mapping
	channels = {
		'translateX': invert_tx, 'translateY': invert_ty, 'translateZ': invert_tz,
		'rotateX': invert_rx, 'rotateY': invert_ry, 'rotateZ': invert_rz
	}
	
	# 4. Extract, Invert, and Apply
	success_count = 0
	for attr, should_invert in channels.items():
		try:
			# Check if attribute is keyable/settable
			if mc.getAttr("{}.{}".format(target, attr), settable=True):
				
				# Get local value
				val = mc.getAttr("{}.{}".format(source, attr))
				
				# Multiply by -1.0 if marked as True
				final_val = (val * -1.0) if should_invert else val
				
				# Set value
				mc.setAttr("{}.{}".format(target, attr), final_val)
				
				# Auto Keyframe (Optional but recommended for animation)
				if auto_key:
					mc.setKeyframe(target, attribute=attr)
					
				success_count += 1
				
		except Exception as e:
			# Silently pass locked/connected attributes to avoid stopping the loop
			pass
			
	print("# Mirrored Local Pose: {} -> {} (Updated {} channels) #".format(source, target, success_count))

# --- Execution ---

# core spine
mc.select('CH004_Shaman_Rig:cog_ctrl')
mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
						  side_from="RGT", 
						  side_to="LFT",
						  invert_tx=True, invert_ty=False, invert_tz=False, 
						  invert_rx=False, invert_ry=True, invert_rz=True,
						  auto_key=False)
						  
						  



mc.select('CH004_Shaman_Rig:spine01FK_ctrl')
mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
						  side_from="RGT", 
						  side_to="LFT",
						  invert_tx=True, invert_ty=False, invert_tz=False, 
						  invert_rx=False, invert_ry=True, invert_rz=True,
						  auto_key=False)






# core spine
mc.select('CH004_Shaman_Rig:clvRGT_ctrl')
mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
						  side_from="RGT", 
						  side_to="LFT",
						  invert_tx=False, invert_ty=True, invert_tz=True, 
						  invert_rx=False, invert_ry=True, invert_rz=True,
						  auto_key=False)
						  
						  
						  
mc.select('CH004_Shaman_Rig:upperArmRGTIK_ctrl')
mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
						  side_from="RGT", 
						  side_to="LFT",
						  invert_tx=False, invert_ty=True, invert_tz=True, 
						  invert_rx=False, invert_ry=True, invert_rz=True,
						  auto_key=False)                          
						  
						  
mc.select('CH004_Shaman_Rig:armRGTIK_ctrl')
mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
						  side_from="RGT", 
						  side_to="LFT",
						  invert_tx=False, invert_ty=True, invert_tz=True, 
						  invert_rx=False, invert_ry=False, invert_rz=False)  
						  
						  
						  
						  
mc.select('CH004_Shaman_Rig1:neck_ctrl',replace=True)
mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
						  side_from="RGT", 
						  side_to="LFT",
						  invert_tx=True, invert_ty=False, invert_tz=False, 
						  invert_rx=False, invert_ry=False, invert_rz=False)                         