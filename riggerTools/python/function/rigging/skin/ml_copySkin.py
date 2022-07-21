# -= ml_copySkin.py =-
#                __   by Morgan Loomis
#     ____ ___  / /  http://morganloomis.com
#    / __ `__ \/ /  Revision 2
#   / / / / / / /  2018-02-17
#  /_/ /_/ /_/_/  _________
#               /_________/
# 
#     ______________
# - -/__ License __/- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# Copyright 2018 Morgan Loomis
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of 
# this software and associated documentation files (the "Software"), to deal in 
# the Software without restriction, including without limitation the rights to use, 
# copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
# Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
#     ___________________
# - -/__ Installation __/- - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# Copy this file into your maya scripts directory, for example:
#     C:/Documents and Settings/user/My Documents/maya/scripts/ml_copySkin.py
# 
# Run the tool in a python shell or shelf button by importing the module, 
# and then calling the primary function:
# 
#     import ml_copySkin
#     ml_copySkin.ui()
# 
# 
#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# Copy a skinCluster from one mesh to another, or to a selection of vertices. If
# no skin exists on the destination, one will be created with the same influences.
# Otherwise any missing influences will be added in order to copy accurate
# weights.
# 
#     ____________
# - -/__ Usage __/- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# Input a source mesh into the "Source Mesh" field by selecting a mesh and
# pressing the "Set Selected" button. Select destination meshes or vertices, and
# press the "Copy Skin" button.
# 
#     _________
# - -/__ Ui __/- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# [Copy Skin] : Copy the Source Skin to selection.
# 
#     ___________________
# - -/__ Requirements __/- - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# This script requires the ml_utilities module, which can be downloaded here:
#     https://raw.githubusercontent.com/morganloomis/ml_tools/master/ml_utilities.py
# 
#                                                             __________
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - /_ Enjoy! _/- - -

__author__ = 'Morgan Loomis'
__license__ = 'MIT'
__category__ = 'None'
__revision__ = 2

import maya.cmds as mc

try:
    # use local path
    from function.rigging.skin import ml_utilities  as utl
    # import ml_utilities as utl
    utl.upToDateCheck(32)
except ImportError:
    result = mc.confirmDialog( title='Module Not Found', 
                message='This tool requires the ml_utilities module. Once downloaded you will need to restart Maya.', 
                button=['Download Module','Cancel'], 
                defaultButton='Cancel', cancelButton='Cancel', dismissString='Cancel' )
    
    if result == 'Download Module':
        mc.showHelp('http://morganloomis.com/tool/ml_utilities/',absolute=True)


def ui():
    '''
    User interface for copy skin
    '''

    CopySkinUI()


class CopySkinUI(utl.MlUi):
    '''Inherited from MlUi
    '''

    def __init__(self):

        super(CopySkinUI, self).__init__('ml_copySkin', 'Copy SkinClusters', width=400, height=180,
                                         info='''Select a skinned mesh to add to the Source Mesh field below.
Select a destination mesh, or vertices to copy the skin to.
Press the button to copy the skin weights.''')

        self.buildWindow()

        self.srcMeshField = self.selectionField(label='Source Mesh',
                                                annotation='Select the mesh to be used as the source skin.',
                                                channel=False,
                                                text='')

        mc.button(label='Copy Skin', command=self.copySkin, annotation='Copy the Source Skin to selection.')

        self.finish()


    def copySkin(self,*args):

        sourceMesh = mc.textFieldButtonGrp(self.srcMeshField, query=True, text=True)

        if not mc.objExists(sourceMesh):
            raise RuntimeError('Input a source mesh into the UI to copy skin from.')

        sel = mc.ls(sl=True, fl=True)

        if not sel:
            raise RuntimeError('Select a mesh or vertices to copy the skin to.')

        meshSel = []
        vtxSel = []
        for each in sel:
            if '.vtx[' in each:
                vtxSel.append(each)
            else:
                meshSel.append(each)

        if vtxSel:
            copySkinComponents(sourceMesh, vtxSel)

        if meshSel:
            for each in meshSel:
                copySkinCluster(sourceMesh, each)


def copySkinInfluences(source, dest):

    sourceSkin = utl.getSkinCluster(source)
    if not sourceSkin:
        return False

    joints = mc.skinCluster(sourceSkin, query=True, influence=True)

    destSkin = utl.getSkinCluster(dest)

    if not destSkin:
        destSkin = mc.skinCluster(joints, dest, toSelectedBones=True)[0]
    else:
        destJoints = mc.skinCluster(destSkin, query=True, influence=True)
        for joint in [x for x in joints if x not in destJoints]:
            mc.skinCluster(destSkin, edit=True, addInfluence=joint, lockWeights=False, weight=0)

    return destSkin


def copySkinComponents(source, destinationVerts):

    if not mc.listRelatives(source, shapes=True):
        raise RuntimeError('Source object must be geometry.')

    sourceSkin = utl.getSkinCluster(source)

    if not sourceSkin:
        raise RuntimeError("Source mesh doesn't have a skinCluster to copy from.")

    destMesh = mc.ls(destinationVerts[0], o=True)[0]
    destMesh = mc.listRelatives(destMesh, parent=True)[0]
    destSkin = copySkinInfluences(source, destMesh)

    tempSet = mc.sets(destinationVerts)

    mc.select(source, tempSet)

    mc.copySkinWeights(noMirror=True,
                       surfaceAssociation='closestPoint',
                       influenceAssociation='closestJoint',
                       normalize=True)

    mc.delete(tempSet)
    mc.select(destinationVerts)


def copySkinCluster(source, destination):

    sourceSkin = utl.getSkinCluster(source)
    if not sourceSkin:
        raise RuntimeError("Source mesh doesn't have a skinCluster to copy from.")

    destSkin = copySkinInfluences(source, destination)

    mc.copySkinWeights(sourceSkin=sourceSkin, destinationSkin=destSkin, noMirror=True,
                       surfaceAssociation='closestPoint',
                       influenceAssociation='closestJoint', normalize=True)

    return destSkin



if __name__ == '__main__':
    ui()

#      ______________________
# - -/__ Revision History __/- - - - - - - - - - - - - - - - - - - - - - - -
#
# Revision 1: 2016-10-31 : First publish.
#
# Revision 2: 2018-02-17 : Updating license to MIT.