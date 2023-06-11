from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_MAN_TUNE_BUTTON(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on Man Tune button"
    button_name = "pts_layout:pts_layout_mantune_btn"

class VALIDATE_TUNE_ISEU_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that tune_iseu.v is displayed"
    view_name = "tune_iseu"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 120
    button_pos_y = 220

class __M_PL_47__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Man Tune button(A9)" - Show view tune_iseu.v'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_MAN_TUNE_BUTTON,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_TUNE_ISEU_VIEW_IS_DISPLAYED,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []