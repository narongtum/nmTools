popup = ('Sweating', 'Sigh', 'Stunned', 'Shock', 'Confused', 'Uncomfortable', 'Joy' , 'Love', 'AngryP', 'Shy_L','Shy_R', )

from function.rigging.autoRig.base import core
reload(core)

facialSwitch_ctrl = core.Dag('facialSwitch_ctrl')

for each in popup:
	facialSwitch_ctrl.addAttribute( at = 'enum', keyable = True , en = 'off:on:', longName = each  )




popup = ('Sweating', 'Sigh', 'Stunned', 'Shock', 'Confused', 'Uncomfortable', 'Joy' , 'Love')



for each in popup:
	mc.connectAttr(f'{facialSwitch_ctrl.name}.{each}', f'popup{each}_cnd.firstTerm')
	