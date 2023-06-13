from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_pps_ctrl1 import *

class SET_VARIABLE_BLIP_COLLISION_DETECTED_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_collision_detected"
    value    = True

class VALIDATE_BLIP_COLLISION_DETECTED_OK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_coldetected"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_red.sd"

class SET_VARIABLE_BLIP_COLLISION_DETECTED_NOTOK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_collision_detected"
    value    = False

class VALIDATE_BLIP_COLLISION_DETECTED_NOTOK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_coldetected"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class __M_Tr_PC1_35__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate blip of Collision Detected in Treatment PPS Ctrl1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_BLIP_COLLISION_DETECTED_OK,
                        VALIDATE_BLIP_COLLISION_DETECTED_OK,
                        SET_VARIABLE_BLIP_COLLISION_DETECTED_NOTOK,
                        VALIDATE_BLIP_COLLISION_DETECTED_NOTOK,
                        ]
        self.teardown_path = []
