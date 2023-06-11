from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class SET_TR1_TCU_SW_MODE(SETUP_SET_VARIABLE):
    name = "Set tr1_tcu_sw_mode to 3"
    var_name = "tr1_tcu_sw_mode"
    value = 3

class CLICK_TR1_TOLERANCE_CHECK_BUTTON(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on TR1 Tolerance Check button "
    button_name = "pts_layout:pts_layout_tr1_tolerance_check_btn"

class VALIDATE_TR1_TOLERANCE_CHECK_PBS_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that tr1_tolerance_check_pbs.v is displayed"
    view_name = "tr1_tolerance_check_pbs"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 120
    button_pos_y = 220

class __M_PL_38__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "TR1 Tolerance Check button(B5)" - Show view tr1_tolerance_check_pbs.v'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_TR1_TCU_SW_MODE,
                        CLICK_TR1_TOLERANCE_CHECK_BUTTON,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_TR1_TOLERANCE_CHECK_PBS_VIEW_IS_DISPLAYED,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []