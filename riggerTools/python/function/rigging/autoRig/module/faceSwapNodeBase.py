#NewfaceSwap
def faceSwapNodeBase(mainCtrl = 'neck_ctrl', faceNum = 8, mat = 'pet_vogelkop01_face_mat'):
    for f in range(faceNum):
        # name
        name = 'faceSwap%02d' %(f+1)
        file = name + '_file'
        con = name + '_con'
        # Func
        mc.createNode( 'condition', n = con)
        mc.setAttr( con + '.secondTerm', f+1)
        mc.setAttr( con + '.operation', 0)
        mc.connectAttr( mainCtrl + '.face', con + '.firstTerm')
        mc.connectAttr( file + '.outColor', con + '.colorIfTrue')
        if f > 0: # connect condition01 to conndition02
            upName = 'faceSwap%02d' %(f)
            upCon = upName + '_con'
            mc.connectAttr( upCon + '.outColor', con + '.colorIfFalse')
            if f == (faceNum-1): # connect Last condition to material
                mc.connectAttr( con + '.outColor', mat + '.color')
        if f < faceNum/2: # connect file to blend [fix color]
            bc = upName = 'faceSwap%02d' %(f+1)
            mc.createNode( 'blendColors', n = bc)
            mc.connectAttr( file + '.outColor', bc + '.color1')
        elif f >= faceNum/2: # connect file to blend [fix color] with save node
            bc = upName = 'faceSwap%02d' %((f+1)-faceNum/2)
            mc.connectAttr( file + '.outColor', bc + '.color2')

faceSwapNodeBase(mainCtrl = 'neck_ctrl', faceNum = 8, mat = 'pet_vogelkop01_face_mat')