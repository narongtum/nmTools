def autoStrechIK():
    #BadASS AutoStrech IK
    givePart = ['arm','leg']
    for p in range(len(givePart)):
        part = givePart[p]
        giveSide = ['LFT','RGT']
        for i in range(len(giveSide)):
            side = giveSide[i]

            #NAMING AND STUFF
            
            if part == 'arm':
                name = ['upperArm','lowerArm','hand']
                
            if part == 'leg': 
                name = ['upperLeg','lowerLeg','foot']
            # >>>>>  CHANGE ONLY THIS PART <<<<<
            
            # 3 Joint Name
            strJnt = name[0] + side + '_IK_jnt'
            midJnt = name[1] + side + '_IK_jnt'
            endJnt = name[2] + side + '_IK_jnt'
            # Get joint position
            strJntTy = mc.getAttr( midJnt + '.ty')
            endJntTy = mc.getAttr( endJnt + '.ty')
            if side == 'LFT':
                disJnt = strJntTy + endJntTy
                ampVal = 0.1
            if side == 'RGT':
                disJnt = (strJntTy + endJntTy)*(-1)
                ampVal = (-0.1)
            # 3 Ctrl Name
            strCtrl = name[0] + side + '_FK_ctrl'
            midCtrl = name[1] + side + '_IK_ctrl'
            endCtrl = name[2] + side + '_IK_ctrl'
            # Start End Loc Name
            strLoc = part + 'StartDist' + side + '_loc'
            endLoc = part + 'EndDist' + side + '_loc'
            # Node System
            disNode = part + 'AutoStretch' + side + '_dtw'
            mdvAutoNode = part + 'AutoStretch' + side + '_mdv'
            mdvNode = part + 'Stretch' + side + '_mdv'
            mdvAmpNode = part + 'StretchAmp' + side + '_mdv'
            cndNode = part + 'AutoStretch' + side +  '_cnd'
            bcNode = part + 'AutoStretch' + side + '_bc'
            pmaNode = part + 'Stretch' + side + '_pma'
            minusNode = part + 'MinuseStretch' + side + '_mdv'
            
            #Create Locator
            mc.spaceLocator(n = strLoc)
            mc.spaceLocator(n = endLoc)
            mc.setAttr( strLoc + '.v', 0)
            mc.setAttr( endLoc + '.v', 0)
            mc.parent( strLoc, endLoc, 'NOTOUCH_grp')
            #SnapLocator
            mc.pointConstraint( strJnt, strLoc, mo=0, w=1)
            mc.pointConstraint( endJnt, endLoc, mo=0, w=1)
            mc.delete(strLoc + '_pointConstraint1')
            mc.delete(endLoc + '_pointConstraint1')
            mc.pointConstraint( strCtrl, strLoc, mo=1, w=1)
            mc.pointConstraint( endCtrl, endLoc, mo=1, w=1)
            #measurement
            mc.createNode('distanceBetween', n = disNode)
            mc.connectAttr( strLoc + 'Shape.worldPosition', disNode + '.point1')
            mc.connectAttr( endLoc + 'Shape.worldPosition', disNode + '.point2')
            #Create AutoStretch_mdv and Set
            mc.createNode('multiplyDivide', n = mdvAutoNode)
            mc.setAttr( mdvAutoNode + '.operation', 2)
            mc.setAttr( mdvAutoNode + '.input2.input2X', disJnt)
            #connect
            mc.connectAttr( disNode + '.distance', mdvAutoNode + '.input1.input1X ')
            
            #Create legAutoStretch_cnd
            mc.createNode('condition', n = cndNode)
            mc.setAttr( cndNode + '.operation', 3)
            mc.setAttr( cndNode + '.secondTerm', disJnt)
            #connect
            mc.connectAttr( mdvAutoNode + '.output.outputX', cndNode + '.colorIfTrue.colorIfTrueR')
            mc.connectAttr( disNode + '.distance', cndNode + '.firstTerm')
            
            #Create legStretchLFT_mdv and Set
            mc.createNode('multiplyDivide', n = mdvNode)
            mc.setAttr ( mdvNode + '.operation', 1)
            mc.setAttr( mdvNode + '.input2.input2X', strJntTy)
            mc.setAttr( mdvNode + '.input2.input2Y', endJntTy)
            #connect
            mc.connectAttr( cndNode + '.outColor.outColorR', mdvNode + '.input1.input1X')
            mc.connectAttr( cndNode + '.outColor.outColorR', mdvNode + '.input1.input1Y')
            
            #Create legStretchLFT_mdv and Set
            mc.createNode('multiplyDivide', n = mdvAmpNode)
            mc.setAttr( mdvAmpNode + '.input2X', ampVal)
            mc.setAttr( mdvAmpNode + '.input2Y', ampVal)
            #connect
            mc.connectAttr( endCtrl + '.lowStretch', mdvAmpNode + '.input1.input1Y') # NEED TO BE FIX "lowLegStretch"
            mc.connectAttr( endCtrl + '.upStretch', mdvAmpNode + '.input1.input1X') # NEED TO BE FIX "upLegStretch"
            
            #Create blendColors
            mc.createNode('blendColors', n = bcNode)
            mc.setAttr( bcNode + '.color2R', strJntTy)
            mc.setAttr( bcNode + '.color2G', endJntTy)
            #connect
            mc.connectAttr( mdvNode + '.output', bcNode + '.color1')
            mc.connectAttr( endCtrl + '.autoStretch', bcNode + '.blender')
            
            #Create legStretchLFT_pma
            mc.createNode('plusMinusAverage', n = pmaNode)
            #connect KEY bc
            mc.connectAttr( bcNode + '.outputR', pmaNode + '.input2D[1].input2Dx')
            mc.connectAttr( bcNode + '.outputG', pmaNode + '.input2D[1].input2Dy')
            #connect KEY amp
            mc.connectAttr( mdvAmpNode + '.outputX', pmaNode + '.input2D[2].input2Dx')
            mc.connectAttr( mdvAmpNode + '.outputY', pmaNode + '.input2D[2].input2Dy')
            

            #export translante to Joint
            mc.connectAttr ( pmaNode + '.output2D.output2Dx', midJnt + '.ty')
            mc.connectAttr ( pmaNode + '.output2D.output2Dy', endJnt + '.ty')

autoStrechIK()