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
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_select_session_screen import SETUP_SELECT_SERVICE_SESSION
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10   
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_SERVICE_SESSION(SETUP_SELECT_SERVICE_SESSION): pass
class SETUP_CLICK_CYCLOTRON_IMAGE(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click cyclotron in ptslayout screen according to its name"
    button_name = "pts_layout:cyclotron"

class SETUP_CLICK_RADIAL_PROBE_BTN(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Click radial probe button in cyclo menu according to its position"
    button_pos_x = 100
    button_pos_y = 310

class __M_S_RP_1__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Start MCR GUI and navigate to Radial Probe Screen"
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
                        SETUP_CLICK_CYCLOTRON_IMAGE,
                        SETUP_CLICK_RADIAL_PROBE_BTN,
                        ]
        self.teardown_path = []