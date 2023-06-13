from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_ESS_IMAGE(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on ESS image"
    button_name = "pts_layout:ess_btn"

class VALIDATE_ESS_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Service_ESS_Layout (ess_layout.v) is displayed"
    view_name = "ess_layout"
    expected_result = "1"

class VALIDATE_SERVICE_ESS_MENU(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Service_Ess_menu (mcr_service_essmenu.v) is displayed"
    view_name = "mcr_service_essmenu"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 110
    button_pos_y = 200

class __M_PL_3__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "ESS image(A2) in Service session" - Show view MCR_Service_ESS_Layout & Show menu MCR_Service_ESS_Menu on left menu panel'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [                       
                        CLICK_ESS_IMAGE,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_ESS_VIEW_IS_DISPLAYED,
                        VALIDATE_SERVICE_ESS_MENU,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []