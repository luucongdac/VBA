from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_pps_ctrl1 import *

class THRIVER_WAIT_3_SECONDS(SETUP_THRIVER_WAIT):
    time = 3

class SET_VARIABLE_LABEL_SETPOINT_POSITION_DEG_PITCH_VISIBLE(SETUP_SET_VARIABLE):
    var_name = "pitch_feedback_visible"
    value    = 1.0

class SET_VARIABLE_LABEL_SETPOINT_POSITION_DEG_PITCH_VALUE(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_goto_pps_pitch_degtarget"
    value    = 2.0

class VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_pitchtxt"
    expected_value = "1"
    info_type = "TMMI_MCR_IS_VISIBLE"

class VALIDATE_RECTANGLE_SETPOINT_POSITION_DEG_PITCH_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pps_ctrl1_5"
    expected_value = "1"
    info_type = "TMMI_MCR_IS_VISIBLE"

class SET_FILL_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_VALID(SETUP_INPUT_TEXTBOX_BY_NAME):
    textbox_name = "mcr_treatment_pps_ctrl1:pcu4_pitchsetpoint"
    content = "1.0"
    extension_key = '\n'

class VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_pitchtxt"
    expected_value = 1.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class SET_FILL_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_OVERMAX(SETUP_INPUT_TEXTBOX_BY_NAME):
    textbox_name = "mcr_treatment_pps_ctrl1:pcu4_pitchsetpoint"
    content = "4.0"
    extension_key = '\n'

class VALIDATE_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_OVERMAX(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "pcu4_pitchsetpoint"
    slot_name = "pitch_setpoint_text"
    expected_value = "> Max"

class SET_FILL_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_OVERMIN(SETUP_INPUT_TEXTBOX_BY_NAME):
    textbox_name = "mcr_treatment_pps_ctrl1:pcu4_pitchsetpoint"
    content = "-4.0"
    extension_key = '\n'

class VALIDATE_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_OVERMIN(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "pcu4_pitchsetpoint"
    slot_name = "pitch_setpoint_text"
    expected_value = "< Min"

class SET_FILL_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_ERROR(SETUP_INPUT_TEXTBOX_BY_NAME):
    textbox_name = "mcr_treatment_pps_ctrl1:pcu4_pitchsetpoint"
    content = "abc"
    extension_key = '\n'

class VALIDATE_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_ERROR(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "pcu4_pitchsetpoint"
    slot_name = "pitch_setpoint_text"
    expected_value = "ERROR"

class VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_pitchtxt"
    expected_value = "0"
    info_type = "TMMI_MCR_IS_VISIBLE"

class VALIDATE_RECTANGLE_SETPOINT_POSITION_DEG_PITCH_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pps_ctrl1_5"
    expected_value = "0"
    info_type = "TMMI_MCR_IS_VISIBLE"

class __M_Tr_PC1_15__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate action of textbox Setpoint Position (deg) of Pitch in Treatment PPS Ctrl1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_LABEL_SETPOINT_POSITION_DEG_PITCH_VISIBLE,
                        SET_VARIABLE_LABEL_SETPOINT_POSITION_DEG_PITCH_VALUE,
                        VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_VISIBLE,
                        VALIDATE_RECTANGLE_SETPOINT_POSITION_DEG_PITCH_VISIBLE,
                        SET_FILL_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_OVERMAX,
                        THRIVER_WAIT_3_SECONDS,
                        VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_INVISIBLE,
                        VALIDATE_RECTANGLE_SETPOINT_POSITION_DEG_PITCH_INVISIBLE,
                        VALIDATE_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_OVERMAX,
                        SET_FILL_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_OVERMIN,
                        THRIVER_WAIT_3_SECONDS,
                        VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_INVISIBLE,
                        VALIDATE_RECTANGLE_SETPOINT_POSITION_DEG_PITCH_INVISIBLE,
                        VALIDATE_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_OVERMIN,
                        SET_FILL_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_ERROR,
                        THRIVER_WAIT_3_SECONDS,
                        VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_INVISIBLE,
                        VALIDATE_RECTANGLE_SETPOINT_POSITION_DEG_PITCH_INVISIBLE,
                        VALIDATE_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_ERROR,
                        SET_FILL_TEXTBOX_SETPOINT_POSITION_DEG_PITCH_VALID,
                        THRIVER_WAIT_3_SECONDS,
                        VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_VISIBLE,
                        VALIDATE_RECTANGLE_SETPOINT_POSITION_DEG_PITCH_VISIBLE,
                        VALIDATE_LABEL_SETPOINT_POSITION_DEG_PITCH_VALUE,
                        ]
        self.teardown_path = []
