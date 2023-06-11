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
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_beam_control_screen import SETUP_CLICK_BEAM_CONTROL
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_beam_control_screen import SETUP_VALIDATE_BEAM_CONTROl_SCREEN
class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_TREATMENT_SESSION(SETUP_SELECT_TREATMENT_SESSION): pass
class CLICK_BEAM_CONTROL(SETUP_CLICK_BEAM_CONTROL): pass
class VALIDATE_BEAM_CONTROL_SCREEN(SETUP_VALIDATE_BEAM_CONTROl_SCREEN): pass
    
class __M_T_BC_1__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Login and select session" - MCR start GUI and Login to Treatment session'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        THRIVER_WAIT_10_SECONDS,
                        CLICK_OK_BUTTON_MSG_DIALOG,
                        INPUT_USERNAME,
                        INPUT_PASSWORD,
                        CLICK_OK_LOGIN_BUTTON,
                        SELECT_TREATMENT_SESSION,
                        THRIVER_WAIT_10_SECONDS,
                        CLICK_BEAM_CONTROL,
                        VALIDATE_BEAM_CONTROL_SCREEN
                        ]
        self.teardown_path = []