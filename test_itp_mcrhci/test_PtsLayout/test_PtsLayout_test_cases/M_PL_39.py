from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class SET_TR2_TCU_SW_MODE(SETUP_SET_VARIABLE):
    name = "Set tr2_tcu_sw_mode to 2"
    var_name = "tr2_tcu_sw_mode"
    value = 2

class CLICK_TR2_TOLERANCE_CHECK_BUTTON(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on TR2 Tolerance Check button "
    button_name = "pts_layout:pts_layout_tr2_tolerance_check_btn"

class VALIDATE_TR2_TOLERANCE_CHECK_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that tr2_tolerance_check.v is displayed"
    view_name = "tr2_tolerance_check"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 120
    button_pos_y = 220

class __M_PL_39__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "TR2 Tolerance Check button(B9)" - Show view tr2_tolerance_check.v'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_TR2_TCU_SW_MODE,
                        CLICK_TR2_TOLERANCE_CHECK_BUTTON,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_TR2_TOLERANCE_CHECK_VIEW_IS_DISPLAYED,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []