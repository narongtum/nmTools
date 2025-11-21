import maya.cmds as mc

def smooth_curve_weights(curve_name, iterations=1, pin_ends=True):
	"""
	Smooth skin weights for a NURBS curve by averaging neighbors (1D Smoothing).
	
	Args:
		curve_name (str): Name of the curve.
		iterations (int): How many times to run the smoothing pass.
		pin_ends (bool): If True, skip the first and last CVs to keep anchors solid.
	"""
	
	# 1. Get SkinCluster
	skin_cluster = mc.ls(mc.listHistory(curve_name), type='skinCluster')
	if not skin_cluster:
		mc.error(f'No SkinCluster found on {curve_name}')
	skin_cls = skin_cluster[0]

	# 2. Get Geometry Info
	# Assuming cvs are in order e.g., curve.cv[0] to curve.cv[n]
	num_cvs = mc.getAttr(f'{curve_name}.degree') + mc.getAttr(f'{curve_name}.spans')
	
	# 3. Get Influences
	influences = mc.skinCluster(skin_cls, query=True, influence=True)
	
	print(f'# Smoothing weights for {curve_name} | Iterations: {iterations}')

	for _ in range(iterations):
		
		# Store current weights to calculate properly (Snapshot)
		current_weights = []
		for i in range(num_cvs):
			wt = mc.skinPercent(skin_cls, f'{curve_name}.cv[{i}]', query=True, value=True)
			current_weights.append(wt)
		
		# Calculate New Weights
		new_weights_map = {} # Key: index, Value: list of weights
		
		start_idx = 1 if pin_ends else 0
		end_idx = num_cvs - 1 if pin_ends else num_cvs
		
		for i in range(start_idx, end_idx):
			# Skip pure start/end if pin_ends is True (Logic handled by range)
			# But strictly: if i is 0 or last, we need neighbor logic adjustment
			
			prev_w = current_weights[i-1] if i > 0 else current_weights[i]
			curr_w = current_weights[i]
			next_w = current_weights[i+1] if i < num_cvs - 1 else current_weights[i]
			
			# Average: (Prev + Curr + Next) / 3
			# Note: We average per influence
			averaged_w = []
			for j in range(len(influences)):
				val = (prev_w[j] + curr_w[j] + next_w[j]) / 3.0
				averaged_w.append(val)
			
			new_weights_map[i] = averaged_w

		# Apply New Weights
		for i, weights in new_weights_map.items():
			# Transform list of values into transformValue list [(jnt, val), ...]
			val_list = list(zip(influences, weights))
			
			mc.skinPercent(
				skin_cls, 
				f'{curve_name}.cv[{i}]', 
				transformValue=val_list, 
				normalize=True
			)

	print(f'# Smoothing Complete.')

# --- How to use ---
# smooth_curve_weights('spine_crv', iterations=3, pin_ends=True)





import maya.cmds as mc

def create_proxy_from_curve(curve_name, width=1.0):
	"""
	Create a polyPlane proxy aligned to the curve for easier weight painting.
	"""
	# 1. Get Curve Info
	spans = mc.getAttr(f'{curve_name}.spans')
	degree = mc.getAttr(f'{curve_name}.degree')
	form = mc.getAttr(f'{curve_name}.form') # 0=Open, 1=Closed, 2=Periodic
	
	# Calculate required subdivisions to match CVs roughly
	# For degree 3 curve, CVs = spans + 3. 
	# We want vertices to align somewhat with CVs.
	subdiv_h = spans 
	if degree > 1:
		subdiv_h = spans * degree # Increase density to cover CVs well
		
	# 2. Create Plane
	# Axis along Z usually fits spine best, adjust as needed
	mesh_name = f'{curve_name}_proxy_geo'
	proxy = mc.polyPlane(
		name=mesh_name, 
		width=width, 
		height=10, # Arbitrary length, will be deformed
		subdivisionsX=1, 
		subdivisionsY=subdiv_h, 
		axis=[0, 1, 0], 
		createUVs=2, 
		constructionHistory=False
	)[0]
	
	# 3. Snap Mesh to Curve (Quick Align)
	# In complex scenarios, we might wire deform this, 
	# but for simple spine, we just match bounds or origin.
	bbox = mc.exactWorldBoundingBox(curve_name)
	# Move plane to center of curve
	center_x = (bbox[0] + bbox[3]) / 2
	center_y = (bbox[1] + bbox[4]) / 2
	center_z = (bbox[2] + bbox[5]) / 2
	
	mc.xform(proxy, t=(center_x, center_y, center_z), ws=True)
	
	# *Better Approach*: Wire Deform or Wrap temporarily to match shape?
	# For simple usage: Just ask user to align manually or use Wire.
	# Let's add a Wire deformer automatically so it snaps to curve shape!
	
	wire = mc.wire(proxy, w=curve_name, dropoffDistance=[0, 100])[0]
	# Freeze deformation to bake the shape
	mc.delete(proxy, constructionHistory=True)
	
	print(f'# Proxy mesh created: {proxy}. Please Bind Skin to this mesh and paint.')
	return proxy

def transfer_mesh_to_curve(source_mesh, target_curve):
	"""
	Copy skin weights from Proxy Mesh to Target Curve.
	"""
	# 1. Get SkinClusters
	src_skin = mc.ls(mc.listHistory(source_mesh), type='skinCluster')
	dst_skin = mc.ls(mc.listHistory(target_curve), type='skinCluster')
	
	if not src_skin or not dst_skin:
		mc.error('Both Mesh and Curve must have SkinClusters attached.')
		
	src_sc = src_skin[0]
	dst_sc = dst_skin[0]
	
	# 2. Select Source then Target
	mc.select(source_mesh, r=True)
	mc.select(target_curve, add=True)
	
	# 3. Copy Weights
	# Surface Association: Closest point on surface is critical here
	mc.copySkinWeights(
		ss=src_sc, 
		ds=dst_sc, 
		noMirror=True, 
		surfaceAssociation='closestPoint', 
		influenceAssociation=['oneToOne', 'name']
	)
	
	print(f'# Weights transferred from {source_mesh} to {target_curve}')

# --- Usage Example ---
# 1. Run create proxy
# create_proxy_from_curve('spine_crv')

# 2. (Manually) Bind the new mesh to joints and paint weights smoothly...

# 3. Run transfer
# transfer_mesh_to_curve('spine_crv_proxy_geo', 'spine_crv')