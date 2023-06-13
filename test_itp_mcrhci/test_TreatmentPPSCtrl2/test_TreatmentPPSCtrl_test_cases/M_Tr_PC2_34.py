from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class SET_VARIABLE_RAW_FORCE_Z(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_loadcell_forcey_raw"
    value    = 10.0

class SET_VARIABLE_RAW_OFFSET_FORCE_Z(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_loadcell_forcey_raw_offset"
    value    = 10.0

class SET_VARIABLE_ENG_FORCE_Z(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_loadcell_forcez_eng"
    value    = 10.0

class SET_VARIABLE_RAW_TORQUE_Z(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_loadcell_torquey_raw"
    value    = 10.0

class SET_VARIABLE_RAW_OFFSET_TORQUE_Z(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_loadcell_torquey_raw_offset"
    value    = 10.0

class SET_VARIABLE_ENG_TORQUE_Z(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_loadcell_torquez_eng"
    value    = 10.0

class VALIDATE_RAW_FORCE_Z(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_zforceraw"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_RAW_OFFSET_FORCE_Z(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_zforcerawoffset"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_ENG_FORCE_Z(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_zforceeng"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_RAW_TORQUE_Z(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_ztorqueraw"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_RAW_OFFSET_TORQUE_Z(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_ztorquerawoffset"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_ENG_TORQUE_Z(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_ztorqueeng"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_Tr_PC2_34__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate value of label Force and Torque of Z in Treatment PPS Ctrl2 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_RAW_FORCE_Z,
                        SET_VARIABLE_RAW_OFFSET_FORCE_Z,
                        SET_VARIABLE_ENG_FORCE_Z,
                        SET_VARIABLE_RAW_TORQUE_Z,
                        SET_VARIABLE_RAW_OFFSET_TORQUE_Z,
                        SET_VARIABLE_ENG_TORQUE_Z,
                        VALIDATE_RAW_FORCE_Z,
                        VALIDATE_RAW_OFFSET_FORCE_Z,
                        VALIDATE_ENG_FORCE_Z,
                        VALIDATE_RAW_TORQUE_Z,
                        VALIDATE_RAW_OFFSET_TORQUE_Z,
                        VALIDATE_ENG_TORQUE_Z,
                        ]
        self.teardown_path = []
