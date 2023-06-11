from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class SET_VARIABLE_FEEDBACK_POSITION_DEG_PITCH(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitch_degfeedback"
    value    = 10.0

class SET_VARIABLE_MONITORING_POSITION_DEG_PITCH(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitch_degmonitoring"
    value    = 10.0

class SET_VARIABLE_FOLLOWING_ERROR_DEG_PITCH(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitch_followingerror"
    value    = 10.0

class VALIDATE_FEEDBACK_POSITION_DEG_PITCH(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_pitchdegfbk"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_MONITORING_POSITION_DEG_PITCH(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_pitchdegmonitoringfbk"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class VALIDATE_FOLLOWING_ERROR_DEG_PITCH(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_pitchfollowingerrfbk"
    expected_value = 10.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_Tr_PC2_30__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate value of label Feedback Position, Monitoring Position and Following Error of Pitch in Treatment PPS Ctrl2 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_FEEDBACK_POSITION_DEG_PITCH,
                        SET_VARIABLE_MONITORING_POSITION_DEG_PITCH,
                        SET_VARIABLE_FOLLOWING_ERROR_DEG_PITCH,
                        VALIDATE_FEEDBACK_POSITION_DEG_PITCH,
                        VALIDATE_MONITORING_POSITION_DEG_PITCH,
                        VALIDATE_FOLLOWING_ERROR_DEG_PITCH,
                        ]
        self.teardown_path = []
