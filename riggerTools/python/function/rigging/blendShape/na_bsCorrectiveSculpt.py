'''
Corrective Blendshape Model Sculpt Helper
Version 1.0
Created by Noah Alzayer
Last Modified 7/28/13
nalzay89@gmail.com
www.noahalzayer.net

To use- Just pose your model, select the mesh then run cbsStart, make the corrections, then run cbsTrans.
Once the corrective is made, if wanted, run cbsMirror to mirror the blendshape and if the driving of the shape is simple, run cbsHookup

Note- For the most user-friendly experience, run na_bsCorrectiveSculptUI
'''

import pymel.core as pm


def gatherInfo(*args):
    base, shape, tweak, skin = args
    
    #weed out any mistakes
    if not base:
        pm.error('No objects are selected')
        
    #gather info
    if not shape: shape = pm.listRelatives(base, s=True)[0]
    
    if not pm.objectType(shape, isType='mesh'):
        pm.error('This script is only approved to work with polygons')
    
    shapeConns = pm.listHistory(shape)
    
    for i in shapeConns:
        if pm.objectType(i, isType='tweak') and not tweak:
            tweak = i
        elif pm.objectType(i, isType='skinCluster') and not skin:
            skin = i
        else:
            continue
    
    return base, shape, tweak, skin


def cbsStart(*args, **kwargs):
    base = kwargs.setdefault('base', pm.ls(sl=True)[0]) # (string) The base model for the character
    shape = kwargs.setdefault('shape') # (string) The shape node of the base model
    tweak = kwargs.setdefault('tweak') # (string) The tweak node of the base model that is being skinned
    skin = kwargs.setdefault('skin') # (string) The skinCluster node that is driving the base model
    
    #gather some info
    base, shape, tweak, skin =  gatherInfo(base, shape, tweak, skin)
    verts= pm.polyEvaluate(base, v=True)
    
    #do a quick check to make sure this part hasn't been done before
    if 'baseTransform' in pm.listAttr(base, ud=True):
        pm.error('You have already run the "Start" function on this model, so it is already ready to go.' +
                 'If corrections have already been made, click "Extract Shape to finish the process"')
    
    
    #turn off a couple things that might mess with things
    pm.symmetricModelling(e=True, symmetry= False)
    pm.softSelect(e=True, softSelectEnabled=False)
    
    
    for i in range(verts):
        
        x = pm.getAttr(('%s.vlist[0].vertex[%i].xVertex'%(tweak, i)))
        y = pm.getAttr(('%s.vlist[0].vertex[%i].yVertex'%(tweak, i)))
        z = pm.getAttr(('%s.vlist[0].vertex[%i].zVertex'%(tweak, i)))     
        
        if not (x+y+z) == 0:
            pm.error('You have used the tweak node. No me gusta. If you really wanna clear it, run clearTweaks and try again. It will save what you have')
    
    #ok, let's get started, first instance the original mesh
    sculptTrans = pm.instance(base, n=('%s_corrective_sculpt'%base))[0]
    pm.reorderDeformers(skin, tweak, base)
    pm.setAttr('%s.v'%base, False)
    
    #Here, we'll make a duplicate of the base to look back on later if need be (for instance, using sculpt geometry tends to not register on tweak)
    baseRef = pm.duplicate(base, n='%s_editReference'%base)[0]
    pm.connectAttr(('%s.outMesh' %baseRef.getShapes()[1]), ('%s.inMesh' %baseRef.getShape()))
    
    #We'll also hook up the original so we can get it later
    pm.addAttr(sculptTrans, ln='baseTransform', at='message')
    pm.addAttr(sculptTrans, ln='baseReference', at='message')
    pm.connectAttr('%s.message'%base, '%s.baseTransform'%sculptTrans)
    pm.connectAttr('%s.message'%baseRef, '%s.baseReference'%sculptTrans)
    
    #now to keep things from changing between functions, we'll lock the three nodes involved in the 
    #other script so our pesky little user won't delete or rename anything
    pm.lockNode(base, l=True)
    pm.lockNode(sculptTrans, l=True)


def cbsTrans(*args, **kwargs):
    
    sculptTrans = kwargs.setdefault('sculptTrans', pm.ls(sl=True)[0])# (string) The mesh to get the tweak edits extracted from
    shape = kwargs.setdefault('shape') # (string) The shape node of the sculptTrans node
    tweak = kwargs.setdefault('tweak') # (string) The tweak node that is going to be cleared
    skin = kwargs.setdefault('skin') # (string) The skinCluster node that drives the base mesh
    base = kwargs.setdefault('base') # (string) The base mesh for the character
    
    #get some info
    sculptTrans, shape, tweak, skin =  gatherInfo(sculptTrans, shape, tweak, skin)
    if not 'baseTransform' in pm.listAttr(sculptTrans, ud=True): 
        pm.error('This model has not been prepared for sculpting. If you accidentally started, simply run Clear Tweaks to extract what has been done')
    if not base: base = pm.getAttr('%s.baseTransform'%sculptTrans)
    baseRef = pm.getAttr('%s.baseReference'%sculptTrans)
    
    #turn off a couple things that might mess with things
    pm.symmetricModelling(e=True, symmetry= False)
    pm.softSelect(e=True, softSelectEnabled=False)
    
    #first, let's unlock the guys from the old function
    pm.lockNode(base, l=False)
    pm.lockNode(sculptTrans, l=False)
    pm.setAttr('%s.v'%base, True)
    
    #extract from the sculpted shape
    newShape = clearTweaks(base=base, tweak=tweak)
    
    pm.delete(sculptTrans)
    
    newOrig = pm.duplicate(base, n='%s_editReference'%base)[0]
    pm.connectAttr(('%s.outMesh' %newOrig.getShapes()[1]), ('%s.inMesh' %newOrig.getShape()))
    
    pm.select(cl=True)
    deviation = False
    for v in range(pm.polyEvaluate(base, v=True)):
        refPos = pm.xform('%s.vtx[%i]'%(baseRef, v), q=True, t=True)
        adjPos = pm.xform('%s.vtx[%i]'%(newOrig, v), q=True, t=True)
        
        if not refPos == adjPos:
            deviation=True
            pm.move('%s.vtx[%i]' %(newShape, v), (refPos[0]-adjPos[0], refPos[1]-adjPos[1], refPos[2]-adjPos[2]), r=True)
            pm.move('%s.vtx[%i]'%(base, v), (refPos[0]-adjPos[0], refPos[1]-adjPos[1], refPos[2]-adjPos[2]), os=True, r=True)
            pm.select('%s.vtx[%i]' %(base, v), add=True)
    
    if deviation:
        #pm.connectAttr(('%s.outMesh' %newOrig.getShape(), ('%s.inMesh' %base.getShapes()[1])))
        pm.warning('It appears there were issues extracting from the mesh, steps have been taken to try and remedy, but unexpected results may occur')        
    
    pm.delete(newOrig, baseRef)
    return newShape


def clearTweaks(*args, **kwargs):
    
    base = kwargs.setdefault('base', pm.ls(sl=True)[0]) # (string) The mesh to get the tweak edits extracted from
    tweak = kwargs.setdefault('tweak') # (string) The tweak node that is going to be cleared
    
    #gathering info just in case it wasn't provided
    baseRep, notUsed, tweakRep, notUsed =  gatherInfo(base, None, tweak, None)
    
    #assigning the variables if needed, finishing the gathering of info
    if not base: base = baseRep
    if not tweak: tweak = tweakRep
    verts= pm.polyEvaluate(base, v=True)
    
    #setting up the output shape
    outputShape = pm.duplicate(base, n='%s_corrective'%base)[0]
    outputShape.getShape().rename('%sShape'%outputShape)
    pm.delete(outputShape.getShapes()[1:]) #deleting any other shape nodes
    for at in 'trs':
        for vec in 'xyz':
            pm.setAttr('%s.%s%s'%(outputShape, at, vec), l=False)
    
    #moving the output shape over and getting the shape right
    outputShape.tx.set(outputShape.boundingBoxSizeX.get())
    pm.connectAttr(('%s.outMesh' %base.getShapes()[1]), ('%s.inMesh' %outputShape.getShape()))
    
    #copying the values in the tweak node to the output shape
    for i in range(verts):

        x = pm.getAttr(('%s.vlist[0].vertex[%i].xVertex'%(tweak, i)))
        y = pm.getAttr(('%s.vlist[0].vertex[%i].yVertex'%(tweak, i)))
        z = pm.getAttr(('%s.vlist[0].vertex[%i].zVertex'%(tweak, i)))     
        
        pm.move('%s.vtx[%i]' %(outputShape, i), (x, y, z), r=True)
        
        pm.setAttr(('%s.vlist[0].vertex[%i].xVertex'%(tweak, i)), 0)
        pm.setAttr(('%s.vlist[0].vertex[%i].yVertex'%(tweak, i)), 0)
        pm.setAttr(('%s.vlist[0].vertex[%i].zVertex'%(tweak, i)), 0)
    
    return outputShape


def cbsHookup(*args, **kwargs):
    
    base = kwargs.setdefault('base') #(string) The base mesh for the character
    bs = kwargs.setdefault('bs') #(string) The blendshape deformer to which the shape should be added (if blank, a new deformer will be created
    shape = kwargs.setdefault('shape') #(string) The new target to add to the blendshape
    driver = kwargs.setdefault('driver') #(string) Node and attribute to have drive the blendshape target weight
    driveRange = kwargs.setdefault('driveRange', [0, 1]) #(2 float list) The range of the driver to go from 0-1. [0]=target weight of 0, [1]=weight of 1 
    tan = kwargs.setdefault('tan', ['spline', 'spline']) # (2 string list) The tangent types for the set driven keys. [0]=start, [1]=end
    infinity = kwargs.setdefault('infinity', [False, False]) # (2 bool list) sets whether or not to give the set driven key pre or post infinity. [0]=pre, [1]=post  
    
    #create a blendshape deformer if one hasn't been specified
    if not bs:
        bs = pm.blendShape(base, frontOfChain=True, n='%s_corrective_bs'%base)[0]
    
    #add the new target to the blendshape
    targs = pm.blendShape(bs, q=True, t=True)
    for targ in targs:
        if str(shape).split('|')[-1] == str(targ).split('|')[-1]:
            pm.error('It appears you already have a blendshape target named %s in the node %s. Please rename the new target with a unique name.'%(shape, bs))
    pm.blendShape(bs, e=True, t=[base, len(targs), shape, 1])
    
    #set up the set driven key to drive the blendshape
    pm.setDrivenKeyframe('%s.%s'%(bs, shape), cd=driver, dv=driveRange[0], v=0, itt=tan[0], ott=tan[0])
    pm.setDrivenKeyframe('%s.%s'%(bs, shape), cd=driver, dv=driveRange[1], v=1, itt=tan[1], ott=tan[1])
    
    #set up infinity if requested
    if infinity[0]:
        pm.setInfinity('%s.%s'%(bs, shape), pri='linear')
    if infinity[1]:
        pm.setInfinity('%s.%s'%(bs, shape), poi='linear')
    

def cbsMirror(blend=None, base=None, *args):
    import maya.mel as mel
    
    if len(pm.ls(sl=True))==2:
        if not blend: blend = pm.ls(sl=True)[0] # (string) The mesh that is desired to be mirrored
        if not base: base = pm.ls(sl=True)[1] # (string) The mesh that serves as the base to mirror (the skinned mesh)
        
    #setting up the new blendshape
    newBase = pm.duplicate(base)[0]
    for at in 'trs':
        for vec in 'xyz':
            pm.setAttr('%s.%s%s'%(newBase, at, vec), l=False)
    
    #creating the new base mesh
    pm.delete(newBase.getShapes()[1:]) #deleting the second shape node
    pm.connectAttr(('%s.outMesh' %pm.listRelatives(base, s=True)[1]), ('%s.inMesh' %newBase.getShape()))
    
    #setting up mirror target
    mirShape = pm.duplicate(newBase)[0]
    mirShape.sx.set(-1)
    bs = pm.blendShape(blend, mirShape)[0]
    
    #creating a wrap deformer
    pm.select([newBase, mirShape], r=True)
    mel.eval('CreateWrap')
    
    #deforming blendshape to deform the new base
    pm.setAttr('%s.%s'%(bs, blend), 1)
    
    #duplicating the result to prevent any tag-alongs
    outShape = pm.duplicate(newBase, n='%s_mirrored'%blend)[0]
    pm.delete(outShape.getShapes()[1:])
    outShape.tx.set(-outShape.boundingBoxSizeX.get())
    
    #clean things up
    pm.delete(mirShape, newBase)
    
    return outShape    