from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10

class SET_VARIABLE_LABEL_SETPOINT_POSITION_CM_X_VISIBLE(SETUP_SET_VARIABLE):
    var_name = "lat_feedback_visible"
    value    = 1.0

class SET_VARIABLE_LABEL_SETPOINT_POSITION_CM_X_VALUE(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_goto_pps_lateral_cmtarget"
    value    = 2.0

class VALIDATE_LABEL_SETPOINT_POSITION_CM_X_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_lattxt"
    expected_value = "1"
    info_type = "TMMI_MCR_IS_VISIBLE"

class VALIDATE_RECTANGLE_SETPOINT_POSITION_CM_X_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pps_ctrl2_1"
    expected_value = "1"
    info_type = "TMMI_MCR_IS_VISIBLE"

class VALIDATE_LABEL_SETPOINT_POSITION_CM_X_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_lattxt"
    expected_value = 2.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class SET_CLICK_LABEL_SETPOINT_POSITION_CM_X(SETUP_CLICK_BUTTON_BY_NAME):
    button_name = "mcr_treatment_pps_ctrl2:pcu4_lattxt"

class SET_VARIABLE_LABEL_SETPOINT_POSITION_CM_X_INVISIBLE(SETUP_SET_VARIABLE):
    var_name = "lat_feedback_visible"
    value    = 0.0

class VALIDATE_LABEL_SETPOINT_POSITION_CM_X_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_lattxt"
    expected_value = "0"
    info_type = "TMMI_MCR_IS_VISIBLE"

class VALIDATE_RECTANGLE_SETPOINT_POSITION_CM_X_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pps_ctrl2_1"
    expected_value = "0"
    info_type = "TMMI_MCR_IS_VISIBLE"

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class __M_Tr_PC2_6__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate value, visibility of label Setpoint Position (cm) of X in Treatment PPS Ctrl2 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_LABEL_SETPOINT_POSITION_CM_X_INVISIBLE,
                        VALIDATE_LABEL_SETPOINT_POSITION_CM_X_INVISIBLE,
                        VALIDATE_RECTANGLE_SETPOINT_POSITION_CM_X_INVISIBLE,
                        SET_VARIABLE_LABEL_SETPOINT_POSITION_CM_X_VISIBLE,
                        SET_VARIABLE_LABEL_SETPOINT_POSITION_CM_X_VALUE,
                        VALIDATE_LABEL_SETPOINT_POSITION_CM_X_VISIBLE,
                        VALIDATE_RECTANGLE_SETPOINT_POSITION_CM_X_VISIBLE,
                        VALIDATE_LABEL_SETPOINT_POSITION_CM_X_VALUE,
                        SET_CLICK_LABEL_SETPOINT_POSITION_CM_X,
                        VALIDATE_LABEL_SETPOINT_POSITION_CM_X_INVISIBLE,
                        VALIDATE_RECTANGLE_SETPOINT_POSITION_CM_X_INVISIBLE,
                        THRIVER_WAIT_1_SECOND,
                        ]
        self.teardown_path = []
