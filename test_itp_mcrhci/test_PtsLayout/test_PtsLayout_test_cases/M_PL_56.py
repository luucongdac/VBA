from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_BTS3_IMAGE(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on BTS3 image"
    button_name = "pts_layout:bts3_btn"

class VALIDATE_BTS3_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Service_BTS3_Layout (bts3_layout.v) is displayed"
    view_name = "bts3_layout"
    expected_result = "1"

class VALIDATE_TREATMENT_BTS3_MENU(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Treatment_BTS3Menu (mcr_treatment_bts3_menu.v) is displayed"
    view_name = "mcr_treatment_bts3_menu"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 125
    button_pos_y = 205

class __M_PL_56__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "BTS3 image (A7)" in Treatment session - Show view MCR_Service_BTS3_Layout view when click on BTS3 image & Show menu MCR_Treatment_BTS3Menu on left menu panel '
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [                       
                        CLICK_BTS3_IMAGE,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_BTS3_VIEW_IS_DISPLAYED,
                        VALIDATE_TREATMENT_BTS3_MENU,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []