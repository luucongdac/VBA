from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_msg_dialog_screen import SETUP_CLICK_OK_BUTTON_MSG_DIALOG 
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_INPUT_USERNAME
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_INPUT_PASSWORD
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_CLICK_OK_LOGIN_BUTTON
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_select_session_screen import SETUP_SELECT_SERVICE_SESSION
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_pts_layout_screen import SETUP_CLICK_ESS_IMAGE
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_service_ess_menu import SETUP_CLICK_TO_GAUSSIAN_PIT_BUTTON_ON_SERVICE_ESS_MENU

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_SERVICE_SESSION(SETUP_SELECT_SERVICE_SESSION): pass
class CLICK_TO_ESS_LAYOUT(SETUP_CLICK_ESS_IMAGE): pass
class CLICK_TO_GAUSSIAN_PIT(SETUP_CLICK_TO_GAUSSIAN_PIT_BUTTON_ON_SERVICE_ESS_MENU): pass
class OPEN_BPM_SELECTION_VIEW(SETUP_CLICK_BUTTON_BY_NAME): 
    name = "Open the BPM Selection View"
    button_name = "mbpm:bpm_id"
    
class __M_BPM_1__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Login and Navigate to the BPM Selection View'
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
                        CLICK_TO_ESS_LAYOUT,
                        CLICK_TO_GAUSSIAN_PIT,
                        OPEN_BPM_SELECTION_VIEW,
                        #Todo: validate the bpm selection view displayed
                        ]
        self.teardown_path = []