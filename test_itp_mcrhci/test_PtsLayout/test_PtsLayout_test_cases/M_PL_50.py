from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_msg_dialog_screen import * 
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_select_session_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10

class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_TREATMENT_SESSION(SETUP_SELECT_TREATMENT_SESSION): pass
class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_CYCLOTRON_IMAGE(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on Cyclotron image"
    button_name = "pts_layout:cyclotron_btn"

class VALIDATE_CYCLO_VIEW_IS_DISPLAYED(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Service_Cyclo_Layout(cyclo_layout.v) is displayed"
    view_name = "cyclo_layout"
    expected_result = "1"

class VALIDATE_TREATMENT_CYCLO_MENU(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    name = "Confirm that MCR_Treatment_Cyclo_menu (mcr_treatment_cyclo_menu.v) is displayed"
    view_name = "mcr_treatment_cyclo_menu"
    expected_result = "1"

class NAVIGATE_TO_PTS_LAYOUT_SCREEN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to PTS layout screen"
    button_pos_x = 120
    button_pos_y = 200
    
class __M_PL_50__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Cyclotron image (A1)" in Treatment session - Show view MCR_Service_Cyclo_Layout & Show menu MCR_Treatment_Cyclo_menu on left menu panel'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        THRIVER_WAIT_10_SECONDS,
                        CLICK_OK_BUTTON_MSG_DIALOG,
                        INPUT_USERNAME,
                        INPUT_PASSWORD,
                        CLICK_OK_LOGIN_BUTTON,
                        SELECT_TREATMENT_SESSION,
                        THRIVER_WAIT_10_SECONDS,
                        CLICK_CYCLOTRON_IMAGE,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_CYCLO_VIEW_IS_DISPLAYED,
                        VALIDATE_TREATMENT_CYCLO_MENU,
                        NAVIGATE_TO_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []