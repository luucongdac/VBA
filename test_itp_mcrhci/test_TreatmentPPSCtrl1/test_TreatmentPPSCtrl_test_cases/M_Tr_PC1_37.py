from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10

class SET_VARIABLE_SPEED_LEVEL_LOW_SPEED(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_sw_high_speed_level"
    value    = False

class SET_VARIABLE_SPEED_LEVEL_HIGH_SPEED(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_sw_high_speed_level"
    value    = True

class VALIDATE_SPEED_LEVEL_LOW_SPEED(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_speedlevel"
    expected_value = "0"
    info_type = "TMMI_MCR_OBJECT_GET_BOOLVALUE"

class VALIDATE_SPEED_LEVEL_HIGH_SPEED(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_speedlevel"
    expected_value = "1"
    info_type = "TMMI_MCR_OBJECT_GET_BOOLVALUE"

class __M_Tr_PC1_37__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate value of label Speed Level in Treatment PPS Ctrl1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VARIABLE_SPEED_LEVEL_HIGH_SPEED,
                        VALIDATE_SPEED_LEVEL_HIGH_SPEED,
                        SET_VARIABLE_SPEED_LEVEL_LOW_SPEED,
                        VALIDATE_SPEED_LEVEL_LOW_SPEED,
                        ]
        self.teardown_path = []
