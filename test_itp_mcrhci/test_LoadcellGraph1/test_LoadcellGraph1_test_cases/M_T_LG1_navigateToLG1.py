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
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_loadcell_graph1 import SETUP_VALIDATE_OPEN_LOADCELL_GRAPH_1
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_loadcell_graph1 import SETUP_UNCHECK_ALL_CHECKBOX_WHEN_INIT_LOADCELL_GRAPH_1

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10   
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_TREATMENT_SESSION(SETUP_SELECT_TREATMENT_SESSION): pass

class SETUP_CLICK_PLAN_VIEW_IN_MAIN_MENU(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Click Plan View in Treatment Main Menu according to its position"
    button_pos_x = 100
    button_pos_y = 160

class SETUP_CLICK_TR1_PPS_DATA_BTN(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click TR1 PPS Data button in ptslayout screen according to its name"
    button_name = "pts_layout:pts_layout_tr1_pps_data_btn"

class SETUP_CLICK_LOADCELL_GRAPH_1_BTN(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click Loadcell Graph button in PPS Ctrl 1 screen according to its position"
    button_name = "mcr_treatment_pps_ctrl1:pcu4_loadcellgrpbtn"

class VALIDATE_LOADCELL_GRAPH_1_WHEN_OPENING(SETUP_VALIDATE_OPEN_LOADCELL_GRAPH_1): pass

class UNCHECK_ALL_CHECKBOX_WHEN_INIT(SETUP_UNCHECK_ALL_CHECKBOX_WHEN_INIT_LOADCELL_GRAPH_1): pass

class __M_T_LG1_1__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Start MCR GUI and navigate to Loadcell Graph 1 Screen"
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
                        SETUP_CLICK_PLAN_VIEW_IN_MAIN_MENU,
                        SETUP_CLICK_TR1_PPS_DATA_BTN,
                        SETUP_CLICK_LOADCELL_GRAPH_1_BTN,
                        VALIDATE_LOADCELL_GRAPH_1_WHEN_OPENING,
                        UNCHECK_ALL_CHECKBOX_WHEN_INIT
                        ]
        self.teardown_path = []
