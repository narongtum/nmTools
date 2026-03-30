import maya.cmds as mc

def is_attr_mirrored(attr, mirror_axis):
    """
    Returns True if the given attribute should be inverted based on the StudioLibrary-style mirrorAxis array.
    """
    if mirror_axis == [-1, 1, 1]:
        if attr in ["translateX", "rotateY", "rotateZ"]:
            return True
    elif mirror_axis == [1, -1, 1]:
        if attr in ["translateY", "rotateX", "rotateZ"]:
            return True
    elif mirror_axis == [1, 1, -1]:
        if attr in ["translateZ", "rotateX", "rotateY"]:
            return True
    elif mirror_axis == [-1, -1, -1]:
        if attr in ["translateX", "translateY", "translateZ"]:
            return True
    return False

def mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
                          side_from="RGT", 
                          side_to="LFT",
                          mirror_axis=[-1, 1, 1],
                          auto_key=False):
    """
    Mirrors Local Transforms by mapping a StudioLibrary-style mirror axis array (e.g. [-1, 1, 1]).
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

    # 3. Set up the channels we want to process
    channels_to_process = [
        'translateX', 'translateY', 'translateZ',
        'rotateX', 'rotateY', 'rotateZ'
    ]
    
    # 4. Extract, Invert, and Apply
    success_count = 0
    for attr in channels_to_process:
        try:
            # Check if attribute is keyable/settable
            if mc.getAttr("{}.{}".format(target, attr), settable=True):
                
                # Get local value
                val = mc.getAttr("{}.{}".format(source, attr))
                
                # Check if it should be inverted based on the StudioLibrary logic
                should_invert = is_attr_mirrored(attr, mirror_axis)
                
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
            
    print("# Mirrored Local Pose: {} -> {} (Updated {} channels, MirrorAxis: {}) #".format(source, target, success_count, mirror_axis))

# --- Execution Examples ---

# # Core spine (behavior mirror)
# mc.select('CH004_Shaman_Rig:cog_ctrl')
# mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
#                           side_from="RGT", 
#                           side_to="LFT",
#                           mirror_axis=[-1, 1, 1], # Inverse TX, RY, RZ
#                           auto_key=False)

# # Clavicle (might be orientation mirrored, or require different setup)
# mc.select('CH004_Shaman_Rig:clvRGT_ctrl')
# mirror_animation_pose(target_ns="CH004_Shaman_Rig1", 
#                           side_from="RGT", 
#                           side_to="LFT",
#                           mirror_axis=[1, -1, -1], # Custom non-standard behavior if needed! Wait.. [1, -1, -1] is not in default StudioLib. Note that only the 4 standard combinations will trigger inversion unless you expand the is_attr_mirrored logic.
#                           auto_key=False)
