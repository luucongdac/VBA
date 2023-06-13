from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class SET_VARIABLE_MOTION_MODE_NUMBER_1(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_motion_mode"
    value    = 1.0

class SET_VARIABLE_MOTION_MODE_NUMBER_0(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_motion_mode"
    value    = 0.0

class VALIDATE_MOTION_MODE_NUMBER_1(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_motionmode"
    expected_value = 1.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_MOTION_MODE_NUMBER_0(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_motionmode"
    expected_value = 0.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_Tr_PC2_41__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate label number of Motion Mode in Treatment PPS Ctrl2 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_MOTION_MODE_NUMBER_1,
                        VALIDATE_MOTION_MODE_NUMBER_1,
                        SET_VARIABLE_MOTION_MODE_NUMBER_0,
                        VALIDATE_MOTION_MODE_NUMBER_0,
                        ]
        self.teardown_path = []
