from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_ACU_DB_60B_BUTTON(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on ACU DB 60b button"
    button_name = "pts_layout:pts_layout_acu_db_60b_btn"

class VALIDATE_ACU_DB_TEST6_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that acu_db_test6.v is displayed"
    view_name = "acu_db_test6"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 120
    button_pos_y = 220

class __M_PL_43__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "ACU DB button" - Show view acu_db_test6.v when clicking button 60b (B20)'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_ACU_DB_60B_BUTTON,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_ACU_DB_TEST6_VIEW_IS_DISPLAYED,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []