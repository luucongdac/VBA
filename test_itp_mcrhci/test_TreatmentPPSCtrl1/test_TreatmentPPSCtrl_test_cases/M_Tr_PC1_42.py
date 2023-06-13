from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class SET_VARIABLE_SAFETY_INTERLOCK_BLACK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_motion_enable"
    value    = True

class SET_VARIABLE_SAFETY_INTERLOCK_RED(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_motion_enable"
    value    = False

class VALIDATE_SAFETY_INTERLOCK_BLACK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_safetyintlklbl"
    expected_value = COLORS.colorDict["BLACK_8"]
    info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"

class VALIDATE_SAFETY_INTERLOCK_RED(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_safetyintlklbl"
    expected_value = COLORS.colorDict["RED_1"]
    info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"

class __M_Tr_PC1_42__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate color of label Safety Interlock in Treatment PPS Ctrl1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_SAFETY_INTERLOCK_BLACK,
                        VALIDATE_SAFETY_INTERLOCK_BLACK,
                        SET_VARIABLE_SAFETY_INTERLOCK_RED,
                        VALIDATE_SAFETY_INTERLOCK_RED,
                        ]
        self.teardown_path = []
