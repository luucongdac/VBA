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

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_TREATMENT_SESSION(SETUP_SELECT_TREATMENT_SESSION): pass
class SETUP_CLICK_PTS_LAYOUT(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Click Plan View in Treatment Mainmenu according to its position"
    button_pos_x = 100
    button_pos_y = 160
class SETUP_CLICK_PPS_DATA(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Open PPS Motion CTRL"
    button_name = "pts_layout:pts_layout_tr2_pps_data_btn"
class SETUP_CLICK_PPS_MOTION_STATUS(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Open PPS Motion Status"
    button_name = "mcr_treatment_pps_ctrl2:pcu4_motbtn"

class __M_T_PMS2_1__(ClinicalIntegrationTestProcedure):
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
                        SETUP_CLICK_PTS_LAYOUT,
                        SETUP_CLICK_PPS_DATA,
                        SETUP_CLICK_PPS_MOTION_STATUS,
                        ]
        self.teardown_path = []