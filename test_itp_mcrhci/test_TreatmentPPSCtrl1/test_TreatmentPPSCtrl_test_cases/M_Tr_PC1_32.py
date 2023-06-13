from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class SET_VARIABLE_RAW_FORCE_X(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_forcex_raw"
    value    = 10.0

class SET_VARIABLE_RAW_OFFSET_FORCE_X(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_forcex_raw_offset"
    value    = 10.0

class SET_VARIABLE_ENG_FORCE_X(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_forcex_eng"
    value    = 10.0

class SET_VARIABLE_RAW_TORQUE_X(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_torquex_raw"
    value    = 10.0

class SET_VARIABLE_RAW_OFFSET_TORQUE_X(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_torquex_raw_offset"
    value    = 10.0

class SET_VARIABLE_ENG_TORQUE_X(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_torquex_eng"
    value    = 10.0

class VALIDATE_RAW_FORCE_X(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_xforceraw"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_RAW_OFFSET_FORCE_X(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_xforcerawoffset"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_ENG_FORCE_X(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_xforceeng"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_RAW_TORQUE_X(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_xtorqueraw"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_RAW_OFFSET_TORQUE_X(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_xtorquerawoffset"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_ENG_TORQUE_X(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_xtorqueeng"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_Tr_PC1_32__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate value of label Force and Torque of X in Treatment PPS Ctrl1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_RAW_FORCE_X,
                        SET_VARIABLE_RAW_OFFSET_FORCE_X,
                        SET_VARIABLE_ENG_FORCE_X,
                        SET_VARIABLE_RAW_TORQUE_X,
                        SET_VARIABLE_RAW_OFFSET_TORQUE_X,
                        SET_VARIABLE_ENG_TORQUE_X,
                        VALIDATE_RAW_FORCE_X,
                        VALIDATE_RAW_OFFSET_FORCE_X,
                        VALIDATE_ENG_FORCE_X,
                        VALIDATE_RAW_TORQUE_X,
                        VALIDATE_RAW_OFFSET_TORQUE_X,
                        VALIDATE_ENG_TORQUE_X,
                        ]
        self.teardown_path = []
