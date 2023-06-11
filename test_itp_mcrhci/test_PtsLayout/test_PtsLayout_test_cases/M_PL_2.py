from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_CYCLOTRON_IMAGE(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on Cyclotron image"
    button_name = "pts_layout:cyclotron_btn"

class VALIDATE_CYCLO_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Service_Cyclo_Layout(cyclo_layout.v) is displayed"
    view_name = "cyclo_layout"
    expected_result = "1"

class VALIDATE_SERVICE_CYCLO_MENU(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Service_Cyclo_menu (mcr_service_cyclomenu.v) is displayed"
    view_name = "mcr_service_cyclomenu"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 120
    button_pos_y = 220


class __M_PL_2__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Cyclotron image (A1) in Service session" - Show view MCR_Service_Cyclo_Layout & Show menu MCR_Service_Cyclo_menu on left menu panel'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_CYCLOTRON_IMAGE,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_CYCLO_VIEW_IS_DISPLAYED,
                        VALIDATE_SERVICE_CYCLO_MENU,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []