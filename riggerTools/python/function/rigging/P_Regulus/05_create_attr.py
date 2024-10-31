from function.rigging.autoRig.base import core
reload(core)



face_ctrl = core.Dag('facialSwitch_ctrl')
# face_ctrl.addAttribute( at = 'enum', keyable = True , en = 'FACIAL', longName = '-------' )
face_ctrl.addAttribute( longName = 'FACIAL', at = 'enum', keyable = True, enumName = 'FACIAL', niceName = '-------' )