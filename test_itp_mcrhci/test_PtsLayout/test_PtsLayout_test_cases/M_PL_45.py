from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_ACU_DB_50B60A_BUTTON(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on ACU DB 50b/60a button"
    button_name = "pts_layout:pts_layout_acu_db_50b60a_btn"

class VALIDATE_ACU_DB_TEST2_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that acu_db_test2.v is displayed"
    view_name = "acu_db_test2"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 120
    button_pos_y = 220

class __M_PL_45__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "ACU DB button" - Show view acu_db_test2.v when clicking button 50b/60a (B22)'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_ACU_DB_50B60A_BUTTON,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_ACU_DB_TEST2_VIEW_IS_DISPLAYED,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []