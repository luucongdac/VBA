from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_msg_dialog_screen import SETUP_CLICK_OK_BUTTON_MSG_DIALOG 
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_INPUT_USERNAME
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_INPUT_PASSWORD
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_CLICK_OK_LOGIN_BUTTON
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_select_session_screen import SETUP_SELECT_TREATMENT_SESSION
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_pps_ctrl2 import *


class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10   
class THRIVER_WAIT_20_SECONDS(SETUP_THRIVER_WAIT):
    time = 20   
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_TREATMENT_SESSION(SETUP_SELECT_TREATMENT_SESSION): pass
class OPEN_VIEW_PPS_CTRL2(SETUP_OPEN_VIEW_PPS_CTRL2): pass
class VALIDATE_DEFAULT_PPS_CTRL2(SETUP_VALIDATE_DEFAULT_PPS_CTRL2): pass

class __M_Tr_PC2_1__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Start MCR GUI and navigate to PPS Ctrl 2 Screen"
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
                        THRIVER_WAIT_20_SECONDS,
                        OPEN_VIEW_PPS_CTRL2,
                        VALIDATE_DEFAULT_PPS_CTRL2,
                        ]
        self.teardown_path = []
