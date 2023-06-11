from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_pps_ctrl1 import *

class SET_VARIABLE_CHECKMARK_CCW_END_OF_TRAVEL_Z_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_negative_endlimit"
    value    = True

class VALIDATE_CHECKMARK_CCW_END_OF_TRAVEL_Z_OK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_znel"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class SET_VARIABLE_CHECKMARK_CCW_END_OF_TRAVEL_Z_NOTOK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_negative_endlimit"
    value    = False

class VALIDATE_CHECKMARK_CCW_END_OF_TRAVEL_Z_NOTOK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_znel"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class SET_VARIABLE_CHECKMARK_HOME_LIMIT_SWITCH_Z_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_vertical_homels"
    value    = True

class VALIDATE_CHECKMARK_HOME_LIMIT_SWITCH_Z_OK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_zhomels"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class SET_VARIABLE_CHECKMARK_HOME_LIMIT_SWITCH_Z_NOTOK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_vertical_homels"
    value    = False

class VALIDATE_CHECKMARK_HOME_LIMIT_SWITCH_Z_NOTOK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_zhomels"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class SET_VARIABLE_CHECKMARK_CW_END_OF_TRAVEL_Z_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_positive_endlimit"
    value    = True

class VALIDATE_CHECKMARK_CW_END_OF_TRAVEL_Z_OK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_zpel"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class SET_VARIABLE_CHECKMARK_CW_END_OF_TRAVEL_Z_NOTOK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_positive_endlimit"
    value    = False

class VALIDATE_CHECKMARK_CW_END_OF_TRAVEL_Z_NOTOK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_zpel"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class SET_VARIABLE_CHECKMARK_PPS_MOTOR_DRIVER_HEALTH_STATUS_Z_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_activated"
    value    = True

class VALIDATE_CHECKMARK_PPS_MOTOR_DRIVER_HEALTH_STATUS_Z_OK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_zactivated"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class SET_VARIABLE_CHECKMARK_PPS_MOTOR_DRIVER_HEALTH_STATUS_Z_NOTOK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_activated"
    value    = False

class VALIDATE_CHECKMARK_PPS_MOTOR_DRIVER_HEALTH_STATUS_Z_NOTOK(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_zactivated"
    info_type = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class __M_Tr_PC1_22__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate checkmark of Safety Interlock Z in Treatment PPS Ctrl1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_CHECKMARK_CCW_END_OF_TRAVEL_Z_OK,
                        VALIDATE_CHECKMARK_CCW_END_OF_TRAVEL_Z_OK,
                        SET_VARIABLE_CHECKMARK_CCW_END_OF_TRAVEL_Z_NOTOK,
                        VALIDATE_CHECKMARK_CCW_END_OF_TRAVEL_Z_NOTOK,
                        SET_VARIABLE_CHECKMARK_HOME_LIMIT_SWITCH_Z_OK,
                        VALIDATE_CHECKMARK_HOME_LIMIT_SWITCH_Z_OK,
                        SET_VARIABLE_CHECKMARK_HOME_LIMIT_SWITCH_Z_NOTOK,
                        VALIDATE_CHECKMARK_HOME_LIMIT_SWITCH_Z_NOTOK,
                        SET_VARIABLE_CHECKMARK_CW_END_OF_TRAVEL_Z_OK,
                        VALIDATE_CHECKMARK_CW_END_OF_TRAVEL_Z_OK,
                        SET_VARIABLE_CHECKMARK_CW_END_OF_TRAVEL_Z_NOTOK,
                        VALIDATE_CHECKMARK_CW_END_OF_TRAVEL_Z_NOTOK,
                        SET_VARIABLE_CHECKMARK_PPS_MOTOR_DRIVER_HEALTH_STATUS_Z_OK,
                        VALIDATE_CHECKMARK_PPS_MOTOR_DRIVER_HEALTH_STATUS_Z_OK,
                        SET_VARIABLE_CHECKMARK_PPS_MOTOR_DRIVER_HEALTH_STATUS_Z_NOTOK,
                        VALIDATE_CHECKMARK_PPS_MOTOR_DRIVER_HEALTH_STATUS_Z_NOTOK,
                        ]
        self.teardown_path = []
