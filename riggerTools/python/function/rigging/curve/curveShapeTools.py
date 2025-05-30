#... stable version it can run
#... Add A to B not work
#... Substract A to B not work

import maya.api.OpenMaya as om
import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc
reload(misc)


class CurveShapeTools(object):
	def __init__(self, tol=0.001):
		self.baseCVs = []     # list of [x, y, z]
		self.baseCVCount = 0
		self.baseCurveName = None  # เก็บชื่อ curve


	def getDagPath(self, nodeName):
		sel = om.MSelectionList()
		sel.add(nodeName)
		return sel.getDagPath(0)  # ✅ ใช้ API 2.0 ล้วน ๆ


	def storeBaseCurve(self, curve):
		self.baseCurveName = curve  # ✅ เก็บชื่อไว้ใช้ภายหลัง
		dagPath = self.getDagPath(curve)
		curveFn = om.MFnNurbsCurve(dagPath)

		self.baseCVs = []
		self.baseCVCount = curveFn.numCVs


		for i in range(curveFn.numCVs):
			pt = curveFn.cvPosition(i, om.MSpace.kObject)  # ✅ API 2.0 ถูกต้อง
			self.baseCVs.append([pt.x, pt.y, pt.z])


		om.MGlobal.displayInfo(f"Base curve data from '{curve}' stored.")

	def revertToBase(self, curve, indices=None):
		mc.undoInfo(openChunk=True)

		try:
			
			if not self.baseCVs:
				om.MGlobal.displayError("No base curve data stored.")
				return

			dagPath = self.getDagPath(curve)
			curveFn = om.MFnNurbsCurve(dagPath)

			if curveFn.numCVs != self.baseCVCount:
				om.MGlobal.displayError("CV count does not match base.")
				return

			# Default: revert all
			if indices is None:
				indices = range(self.baseCVCount)

			for i in indices:
				if i >= self.baseCVCount:
					om.MGlobal.displayWarning(f"Index {i} is out of range.")
					continue

				basePos = self.baseCVs[i]
				curveFn.setCVPosition(i, om.MPoint(*basePos), om.MSpace.kObject)

			curveFn.updateCurve()
		finally:
			mc.undoInfo(closeChunk=True)
		om.MGlobal.displayInfo(f"Reverted CVs {indices} of '{curve}' to base.")
		


	def mirror_curve_cvs(self, curve, right_to_left=False):
		cvs = mc.ls(f'{curve}.cv[*]', flatten=True)
		cv_count = len(cvs)
		mid_index = cv_count // 2
		center_x = (mc.xform(f'{curve}.cv[{mid_index - 1}]', q=True, ws=True, t=True)[0] + mc.xform(f'{curve}.cv[{mid_index}]', q=True, ws=True, t=True)[0]) / 2.0 if cv_count % 2 == 0 else mc.xform(f'{curve}.cv[{mid_index}]', q=True, ws=True, t=True)[0]
		for i in range(0, mid_index):
			src_i = mid_index + i if right_to_left else mid_index - 1 - i
			tgt_i = mid_index - 1 - i if right_to_left else mid_index + i
			pos = mc.xform(f'{curve}.cv[{src_i}]', q=True, ws=True, t=True)
			mirrored_pos = [center_x - (pos[0] - center_x), pos[1], pos[2]]
			mc.xform(f'{curve}.cv[{tgt_i}]', ws=True, t=mirrored_pos)
		
	def flipCurve(self, curve, axis='x'):
		dagPath = self.getDagPath(curve)
		curveFn = om.MFnNurbsCurve(dagPath)

		for i in range(curveFn.numCVs):
			pt = curveFn.cvPosition(i, om.MSpace.kObject)  # ✅ API 2.0
			# curveFn.cvPosition(index, space)(i, pt, om.MSpace.kObject)

			if axis == 'x':
				pt.x *= -1
			elif axis == 'y':
				pt.y *= -1
			elif axis == 'z':
				pt.z *= -1
			else:
				om.MGlobal.displayError("Invalid mirror axis.")
				return

			curveFn.setCVPosition(i, pt, om.MSpace.kObject)  # ✅ ใช้ setCVPosition แทน setCV

		curveFn.updateCurve()
		om.MGlobal.displayInfo(f"Curve '{curve}' mirrored on {axis}-axis.")





	def add_curve_shape_relative_from_base(self, modified, target):
		if not self.baseCVs:
			mc.warning("No base curve stored.")
			return

		# ✅ ใช้ชื่อ base curve ที่เก็บไว้
		baseFn = om.MFnNurbsCurve(self.getDagPath(self.baseCurveName)) # ✅ ใช้ชื่อที่เคยเก็บไว้
		baseCVCount = baseFn.numCVs
		baseCVs = [baseFn.cvPosition(i, om.MSpace.kObject) for i in range(baseCVCount)]

		# Prepare function sets for modified and target
		modPath = getDagPath(modified)
		tgtPath = getDagPath(target)
		modFn   = om.MFnNurbsCurve(modPath)
		tgtFn   = om.MFnNurbsCurve(tgtPath)

		# Validate CV count
		if modFn.numCVs != baseCVCount or tgtFn.numCVs != baseCVCount:
			om.MGlobal.displayError("CV count mismatch.")
		else:
			mc.undoInfo(openChunk=True)
			try:
				# Matrix for A→B transformation
				mat_mod = modPath.inclusiveMatrix()
				mat_tgt = tgtPath.inclusiveMatrix()
				mat_mod_to_tgt = mat_mod * mat_tgt.inverse()

				for i in range(baseCVCount):
					pos_base = baseCVs[i]
					pos_mod  = modFn.cvPosition(i, om.MSpace.kObject)
					pos_tgt  = tgtFn.cvPosition(i, om.MSpace.kObject)

					delta = pos_mod - pos_base
					new_pos = pos_tgt + (delta * mat_mod_to_tgt)

					tgtFn.setCVPosition(i, new_pos, om.MSpace.kObject)

				tgtFn.updateCurve()
				om.MGlobal.displayInfo("✅ Shape applied successfully (relative to base).")
			finally:
				mc.undoInfo(closeChunk=True)



	def subtract_curve_shape(self, modified, target):
		if not self.baseCVs:
			mc.warning("No base curve stored.")
			return

		baseFn = om.MFnNurbsCurve(self.getDagPath(self.baseCurveName))
		baseCVCount = baseFn.numCVs
		baseCVs = [baseFn.cvPosition(i, om.MSpace.kObject) for i in range(baseCVCount)]

		modPath = self.getDagPath(modified)
		tgtPath = self.getDagPath(target)
		modFn   = om.MFnNurbsCurve(modPath)
		tgtFn   = om.MFnNurbsCurve(tgtPath)

		if modFn.numCVs != baseCVCount or tgtFn.numCVs != baseCVCount:
			om.MGlobal.displayError("CV count mismatch.")
		else:
			mc.undoInfo(openChunk=True)
			try:
				mat_mod = modPath.inclusiveMatrix()
				mat_tgt = tgtPath.inclusiveMatrix()
				mat_mod_to_tgt = mat_mod * mat_tgt.inverse()

				for i in range(baseCVCount):
					pos_base = baseCVs[i]
					pos_mod  = modFn.cvPosition(i, om.MSpace.kObject)
					pos_tgt  = tgtFn.cvPosition(i, om.MSpace.kObject)

					delta = pos_mod - pos_base
					new_pos = pos_tgt - (delta * mat_mod_to_tgt)  # ✅ ลบ delta แทนบวก

					tgtFn.setCVPosition(i, new_pos, om.MSpace.kObject)

				tgtFn.updateCurve()
				om.MGlobal.displayInfo("✅ Subtracted shape from base (relative).")
			finally:
				mc.undoInfo(closeChunk=True)



	def copy_curve_shape_via_blendShape(self, source, target, weight=1.0):
		"""
		Copy curve shape from source to target using temporary blendShape connection.
		This method preserves history and keeps blendShape compatibility.

		Args:
			source (str): source curve (shape donor)
			target (str): target curve (to receive shape)
			weight (float): blendShape weight to apply (default=1.0)
		"""
		if not (mc.objExists(source) and mc.objExists(target)):
			mc.warning("Source or target does not exist.")
			return

		# Make sure both have same number of CVs
		source_cvs = mc.ls(f'{source}.cv[*]', flatten=True)
		target_cvs = mc.ls(f'{target}.cv[*]', flatten=True)
		if len(source_cvs) != len(target_cvs):
			mc.warning("Source and target CV count do not match.")
			return

		# Create temporary blendShape
		bsh_node = mc.blendShape(source, target, origin='local')[0]
		mc.setAttr(f'{bsh_node}.{source}', weight)

		# Delete blendShape node
		mc.delete(target, ch=True)


		mc.inViewMessage(amg=f"Copied shape from <hl>{source}</hl> → <hl>{target}</hl>", pos='midCenterTop', fade=True)




def create_ui():
	if mc.window("curveToolUI", exists=True):
		mc.deleteUI("curveToolUI")
	window = mc.window("curveToolUI", title="Curve Tool", widthHeight=(240, 300))
	mc.columnLayout(adjustableColumn=True, rowSpacing=6)

	tool = CurveReflector()

	def select_base():
		global base_curve
		sel = mc.ls(sl=True)
		if sel:
			base_curve = sel[0]
			tool.storeBaseCurve(base_curve)
			mc.inViewMessage(amg=f"<hl>{base_curve}</hl> set as base", pos='midCenterTop', fade=True)

	def revert_to_base():
		global base_curve
		sel = mc.ls(sl=True)
		if not base_curve or not sel:
			mc.warning("No base or selection")
			return
		for tgt in sel:
			if tgt != base_curve:
				tool.revertToBase(tgt)

	def call_add_shape_relative_via_base():
		sel = mc.ls(sl=True)
		if len(sel) < 2:
			mc.warning("Please select 2 curves: modified (A) and target (B)")
			return
		modified, target = sel[0], sel[1]
		tool.add_curve_shape_relative_from_base(modified, target)



	mc.button(label="Select base curve", c=lambda *_: select_base())
	mc.separator(h=8)

	mc.button(label="Mirror Selected", c=lambda *_: [tool.mirror_curve_cvs(obj, True) for obj in mc.ls(sl=True)])
	mc.button(label="Flip Selected", c=lambda *_: [tool.flipCurve(obj) for obj in mc.ls(sl=True)])
	mc.button(label="Revert Selected to Base", c=lambda *_: revert_to_base())
	mc.separator(h=8)

	mc.button(label="Copy A to B", c=lambda *_: tool.copy_curve_shape_via_blendShape(*mc.ls(sl=True)[:2], weight=1.0))
	mc.button(label="Add A to B", c=lambda *_: call_add_shape_relative_via_base())
	mc.button(label="Subtract A to B", c=lambda *_: tool.subtract_curve_shape(*mc.ls(sl=True)[:2]))


	mc.showWindow(window)

# เรียก UI
create_ui()


'''
selected = mc.ls(sl=True)[0]
				
tool = CurveReflector()		
tool.storeBaseCurve(selected)
tool.revertToBase(selected)
tool.mirror_curve_cvs(selected, right_to_left=False)
tool.flipCurve(selected)
'''