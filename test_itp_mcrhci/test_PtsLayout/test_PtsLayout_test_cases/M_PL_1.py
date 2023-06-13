from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_msg_dialog_screen import * 
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_select_session_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_pts_layout_screen import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_SERVICE_SESSION(SETUP_SELECT_SERVICE_SESSION): pass
class VALIDATE_PTS_LAYOUT_SCREEN(SETUP_VALIDATE_DEFAULT_PTS_LAYOUT_SCREEN): pass
    
class __M_PL_1__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Login and select session" - MCR start GUI and Login to Service session'
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
                        SELECT_SERVICE_SESSION,
                        THRIVER_WAIT_10_SECONDS,
                        VALIDATE_PTS_LAYOUT_SCREEN
                        ]
        self.teardown_path = []