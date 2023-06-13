from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_SET_VARIABLE
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_VALIDATE_OBJECT_INFO

class THRIVER_WAIT_1_SECONDS(SETUP_THRIVER_WAIT):
    time = 1

class SET_HOME_IN_PROGRESS_X_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_xmotor_home_inprogress"
    value    = True

class SET_HOME_IN_PROGRESS_Y_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_ymotor_home_inprogress"
    value    = True

class SET_HOME_IN_PROGRESS_Z_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_zmotor_home_inprogress"
    value    = True

class SET_HOME_IN_PROGRESS_RT_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rotmotor_home_inprogress"
    value    = True

class SET_HOME_IN_PROGRESS_PCH_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitchmotor_home_inprogress"
    value    = True

class SET_HOME_IN_PROGRESS_ROLL_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rollmotor_home_inprogress"
    value    = True

class SET_HOME_IN_PROGRESS_GANTRY_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_gantry_motor_home_inprogress"
    value    = True

class SET_HOME_LIMIT_SWITCH_X_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_lateral_homels"
    value    = True

class SET_HOME_LIMIT_SWITCH_Y_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_longitudinal_homels"
    value    = True

class SET_HOME_LIMIT_SWITCH_Z_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_vertical_homels"
    value    = True

class SET_HOME_LIMIT_SWITCH_RT_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rotational_homels"
    value    = True

class SET_HOME_LIMIT_SWITCH_PCH_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitch_homels"
    value    = True

class SET_HOME_LIMIT_SWITCH_ROLL_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_roll_homels"
    value    = True

class SET_HOME_LIMIT_SWITCH_GANTRY_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_gantry_position_homels"
    value    = True

class SET_HOME_COMPLETE_X_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_xmotor_home_complete"
    value    = True

class SET_HOME_COMPLETE_Y_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_ymotor_home_complete"
    value    = True

class SET_HOME_COMPLETE_Z_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_zmotor_home_complete"
    value    = True

class SET_HOME_COMPLETE_RT_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rotmotor_home_complete"
    value    = True

class SET_HOME_COMPLETE_PCH_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitchmotor_home_complete"
    value    = True

class SET_HOME_COMPLETE_ROLL_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rollmotor_home_complete"
    value    = True

class SET_HOME_COMPLETE_GANTRY_INFO_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_gantry_motor_home_complete"
    value    = True

class SET_HOME_IN_PROGRESS_X_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_xmotor_home_inprogress"
    value    = False

class SET_HOME_IN_PROGRESS_Y_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_ymotor_home_inprogress"
    value    = False

class SET_HOME_IN_PROGRESS_Z_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_zmotor_home_inprogress"
    value    = False

class SET_HOME_IN_PROGRESS_RT_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rotmotor_home_inprogress"
    value    = False

class SET_HOME_IN_PROGRESS_PCH_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitchmotor_home_inprogress"
    value    = False

class SET_HOME_IN_PROGRESS_ROLL_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rollmotor_home_inprogress"
    value    = False

class SET_HOME_IN_PROGRESS_GANTRY_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_gantry_motor_home_inprogress"
    value    = False

class SET_HOME_LIMIT_SWITCH_X_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_lateral_homels"
    value    = False

class SET_HOME_LIMIT_SWITCH_Y_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_longitudinal_homels"
    value    = False

class SET_HOME_LIMIT_SWITCH_Z_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_vertical_homels"
    value    = False

class SET_HOME_LIMIT_SWITCH_RT_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rotational_homels"
    value    = False

class SET_HOME_LIMIT_SWITCH_PCH_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitch_homels"
    value    = False

class SET_HOME_LIMIT_SWITCH_ROLL_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_roll_homels"
    value    = False

class SET_HOME_LIMIT_SWITCH_GANTRY_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_gantry_position_homels"
    value    = False

class SET_HOME_COMPLETE_X_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_xmotor_home_complete"
    value    = False

class SET_HOME_COMPLETE_Y_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_ymotor_home_complete"
    value    = False

class SET_HOME_COMPLETE_Z_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_zmotor_home_complete"
    value    = False

class SET_HOME_COMPLETE_RT_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rotmotor_home_complete"
    value    = False

class SET_HOME_COMPLETE_PCH_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_pitchmotor_home_complete"
    value    = False

class SET_HOME_COMPLETE_ROLL_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_pps_rollmotor_home_complete"
    value    = False

class SET_HOME_COMPLETE_GANTRY_INFO_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_gantry_motor_home_complete"
    value    = False

class VALIDATE_HOME_IN_PROGRESS_X_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_X info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_xhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_IN_PROGRESS_Y_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_Y info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_yhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_IN_PROGRESS_Z_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_Z info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_zhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_IN_PROGRESS_RT_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_RT info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rothomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_IN_PROGRESS_PCH_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_PCH info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_pitchhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_IN_PROGRESS_ROLL_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_ROLL info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rollhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_IN_PROGRESS_GANTRY_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_GANTRY info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_gantryhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_X_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_X info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_xhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_Y_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_Y info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_yhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_Z_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_Z info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_zhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_RT_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_RT info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rothomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_PCH_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_PCH info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_pitchhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_ROLL_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_ROLL info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rollhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_GANTRY_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_GANTRY info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_gantryhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_COMPLETE_X_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_X info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_xhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_COMPLETE_Y_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_Y info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_yhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_COMPLETE_Z_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_Z info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_zhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_COMPLETE_RT_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_RT info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rothomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_COMPLETE_PCH_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_PCH info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_pitchhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_COMPLETE_ROLL_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_ROLL info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rollhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_COMPLETE_GANTRY_INFO_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_GANTRY info ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_gantryhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_ok.sd"

class VALIDATE_HOME_IN_PROGRESS_X_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_X info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_xhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_IN_PROGRESS_Y_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_Y info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_yhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_IN_PROGRESS_Z_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_Z info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_zhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_IN_PROGRESS_RT_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_RT info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rothomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_IN_PROGRESS_PCH_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_PCH info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_pitchhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_IN_PROGRESS_ROLL_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_ROLL info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rollhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_IN_PROGRESS_GANTRY_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_IN_PROGRESS_GANTRY info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_gantryhomein"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_X_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_X info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_xhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_Y_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_Y info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_yhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_Z_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_Z info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_zhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_RT_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_RT info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rothomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_PCH_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_PCH info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_pitchhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_ROLL_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_ROLL info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rollhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_LIMIT_SWITCH_GANTRY_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_LIMIT_SWITCH_GANTRY info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_gantryhomels"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_COMPLETE_X_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_X info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_xhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_COMPLETE_Y_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_Y info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_yhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_COMPLETE_Z_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_Z info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_zhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_COMPLETE_RT_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_RT info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rothomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_COMPLETE_PCH_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_PCH info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_pitchhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_COMPLETE_ROLL_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_ROLL info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_rollhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class VALIDATE_HOME_COMPLETE_GANTRY_INFO_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate HOME_COMPLETE_GANTRY info not ok" 
    object_name    = "mcr_treatment_pps_motion_status2:pcu5_gantryhomecomplete"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_info_notok.sd"

class __M_T_PMS2_86__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_IN_PROGRESS_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_IN_PROGRESS_X_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_X_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_IN_PROGRESS_X_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_X_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_87__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_IN_PROGRESS_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_IN_PROGRESS_Y_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_Y_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_IN_PROGRESS_Y_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_Y_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_88__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_IN_PROGRESS_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_IN_PROGRESS_Z_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_Z_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_IN_PROGRESS_Z_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_Z_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_89__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_IN_PROGRESS_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_IN_PROGRESS_RT_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_RT_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_IN_PROGRESS_RT_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_RT_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_90__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_IN_PROGRESS_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_IN_PROGRESS_PCH_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_PCH_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_IN_PROGRESS_PCH_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_PCH_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_91__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_IN_PROGRESS_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_IN_PROGRESS_ROLL_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_ROLL_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_IN_PROGRESS_ROLL_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_ROLL_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_92__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_IN_PROGRESS_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_IN_PROGRESS_GANTRY_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_GANTRY_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_IN_PROGRESS_GANTRY_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_IN_PROGRESS_GANTRY_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_93__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_LIMIT_SWITCH_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_LIMIT_SWITCH_X_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_X_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_LIMIT_SWITCH_X_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_X_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_94__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_LIMIT_SWITCH_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_LIMIT_SWITCH_Y_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_Y_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_LIMIT_SWITCH_Y_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_Y_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_95__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_LIMIT_SWITCH_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_LIMIT_SWITCH_Z_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_Z_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_LIMIT_SWITCH_Z_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_Z_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_96__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_LIMIT_SWITCH_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_LIMIT_SWITCH_RT_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_RT_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_LIMIT_SWITCH_RT_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_RT_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_97__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_LIMIT_SWITCH_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_LIMIT_SWITCH_PCH_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_PCH_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_LIMIT_SWITCH_PCH_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_PCH_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_98__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_LIMIT_SWITCH_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_LIMIT_SWITCH_ROLL_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_ROLL_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_LIMIT_SWITCH_ROLL_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_ROLL_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_99__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_LIMIT_SWITCH_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_LIMIT_SWITCH_GANTRY_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_GANTRY_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_LIMIT_SWITCH_GANTRY_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_LIMIT_SWITCH_GANTRY_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_100__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_COMPLETE_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_COMPLETE_X_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_X_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_COMPLETE_X_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_X_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_101__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_COMPLETE_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_COMPLETE_Y_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_Y_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_COMPLETE_Y_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_Y_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_102__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_COMPLETE_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_COMPLETE_Z_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_Z_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_COMPLETE_Z_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_Z_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_103__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_COMPLETE_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_COMPLETE_RT_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_RT_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_COMPLETE_RT_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_RT_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_104__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_COMPLETE_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_COMPLETE_PCH_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_PCH_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_COMPLETE_PCH_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_PCH_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_105__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_COMPLETE_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_COMPLETE_ROLL_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_ROLL_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_COMPLETE_ROLL_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_ROLL_INFO_NOT_OK,
                        ]
        self.teardown_path = []

class __M_T_PMS2_106__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate HOME_COMPLETE_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_HOME_COMPLETE_GANTRY_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_GANTRY_INFO_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_HOME_COMPLETE_GANTRY_INFO_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_HOME_COMPLETE_GANTRY_INFO_NOT_OK,
                        ]
        self.teardown_path = []