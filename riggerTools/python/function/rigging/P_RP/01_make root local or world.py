from function.rigging.autoRig.base import core
reload(core)

#... for making root motion local or world that can switch off and on to be used in animation



baseName = 'rootFk'
rootWorld_ctrl = core.Dag(f'{baseName}_ctrl')
rootWorld_ctrl.nmCreateController('circle_ctrlShape')
rootWorld_ctrl.editCtrlShape( axis = 1 * 10 )
rootWorld_ctrl.color = 'yellow'



rig_grp = core.Null(f'{baseName}Rig_grp')
offset_grp = core.Null(f'{baseName}Offset_grp')
zro_grp = core.Null(f'{baseName}Zro_grp')

local_grp = core.Null(f'{baseName}Loc_grp')

local_grp.parent(rig_grp)



rootWorld_ctrl.parent(zro_grp)
zro_grp.parent(offset_grp)
offset_grp.parent(rig_grp)
mc.parent(rig_grp.name, 'placement_ctrl')


rootGimbal_name = core.createGimbal(rootWorld_ctrl.name)


root_psCon = core.parentConstraint(local_grp.name,'noTouch_grp', zro_grp.name , name = f'{baseName}_psCon')

rootWorld_ctrlShape = core.Dag(rootWorld_ctrl.shape)
rootWorld_ctrlShape.addAttribute( at = 'long'  , min = 0  , max = 1, longName = 'Local_World', keyable = True, defaultValue = 1  )
root_rev = core.ReverseNam(f'{baseName}')
rootWorld_ctrlShape.attr('Local_World') >> root_rev.attr('inputX')
root_rev.attr('outputX') >> root_psCon.attr(f'{local_grp}W0')
rootWorld_ctrlShape.attr('Local_World') >> root_psCon.attr('noTouch_grpW1')
root_jnt_psCon = core.parentConstraint(rootWorld_ctrl.name,'root', name = f'{baseName}Jnt_psCon')

