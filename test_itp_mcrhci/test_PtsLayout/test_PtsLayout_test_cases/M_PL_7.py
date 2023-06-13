from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_BTS2_IMAGE(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on BTS2 image"
    button_name = "pts_layout:bts2_btn"

class VALIDATE_BTS2_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Service_BTS2_Layout (bts2_layout.v) is displayed"
    view_name = "bts2_layout"
    expected_result = "1"

class VALIDATE_SERVICE_BTS2_MENU(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Service_Bts2_menu (mcr_service_bts2menu.v) is displayed"
    view_name = "mcr_service_bts2menu"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 120
    button_pos_y = 200

class __M_PL_7__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "BTS2 image (A6) in Service session" - Show view MCR_Service_BTS2_Layout view  & Show menu MCR_Service_BTS2Menu on left menu panel'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_BTS2_IMAGE,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_BTS2_VIEW_IS_DISPLAYED,
                        VALIDATE_SERVICE_BTS2_MENU,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []