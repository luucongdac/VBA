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
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_CLICK_BUTTON_BY_POSITION
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_CLICK_BUTTON_BY_NAME
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_set_range_tr1_screen import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10   
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_TREATMENT_SESSION(SETUP_SELECT_TREATMENT_SESSION): pass
class VALIDATE_OPEN_TREATMENT_SET_RANGE_TR1(SETUP_VALIDATE_OPEN_TREATMENT_SET_RANGE_TR1): pass
class SETUP_CLICK_SET_RANGE_TR1_BTN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Click Set range tr1 in Treatment Mainmenu according to its position"
    button_pos_x = 100
    button_pos_y = 400

class __M_T_SRTR1_1__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Login and select session" - MCR start GUI and Login to Treatment Set Range Tr1'
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
                        SETUP_CLICK_SET_RANGE_TR1_BTN,
                        THRIVER_WAIT_10_SECONDS,
                        VALIDATE_OPEN_TREATMENT_SET_RANGE_TR1,
                        ]
        self.teardown_path = []