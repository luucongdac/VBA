from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class SET_VARIABLE_RAW_FORCE_Y(SETUP_SET_VARIABLE):
    var_name = "pcu_loadcell_forcez_raw_N_A"
    value    = "N/A"

class SET_VARIABLE_RAW_OFFSET_FORCE_Y(SETUP_SET_VARIABLE):
    var_name = "pcu_loadcell_forcez_raw_offset_N_A"
    value    = "N/A"

class SET_VARIABLE_ENG_FORCE_Y(SETUP_SET_VARIABLE):
    var_name = "pcu_loadcell_forcey_eng_N_A"
    value    = "N/A"

class SET_VARIABLE_RAW_TORQUE_Y(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_torquez_raw"
    value    = 10.0

class SET_VARIABLE_RAW_OFFSET_TORQUE_Y(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_torquez_raw_offset"
    value    = 10.0

class SET_VARIABLE_ENG_TORQUE_Y(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_torquey_eng"
    value    = 10.0

class VALIDATE_RAW_FORCE_Y(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_yforceraw"
    expected_value = "N/A"
    info_type = "TMMI_MCR_TEXT_FIELD"

class VALIDATE_RAW_OFFSET_FORCE_Y(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_yforcerawoffset"
    expected_value = "N/A"
    info_type = "TMMI_MCR_TEXT_FIELD"

class VALIDATE_ENG_FORCE_Y(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_yforceeng"
    expected_value = "N/A"
    info_type = "TMMI_MCR_TEXT_FIELD"

class VALIDATE_RAW_TORQUE_Y(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_ytorqueraw"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_RAW_OFFSET_TORQUE_Y(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_ytorquerawoffset"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_ENG_TORQUE_Y(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_ytorqueeng"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_Tr_PC1_33__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate value of label Force and Torque of Y in Treatment PPS Ctrl1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_RAW_FORCE_Y,
                        SET_VARIABLE_RAW_OFFSET_FORCE_Y,
                        SET_VARIABLE_ENG_FORCE_Y,
                        SET_VARIABLE_RAW_TORQUE_Y,
                        SET_VARIABLE_RAW_OFFSET_TORQUE_Y,
                        SET_VARIABLE_ENG_TORQUE_Y,
                        VALIDATE_RAW_FORCE_Y,
                        VALIDATE_RAW_OFFSET_FORCE_Y,
                        VALIDATE_ENG_FORCE_Y,
                        VALIDATE_RAW_TORQUE_Y,
                        VALIDATE_RAW_OFFSET_TORQUE_Y,
                        VALIDATE_ENG_TORQUE_Y,
                        ]
        self.teardown_path = []
