from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_pps_ctrl2 import *


class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
    time = 5   

class OPEN_VIEW_PPS_CTRL2(SETUP_OPEN_VIEW_PPS_CTRL2): pass

class SET_CLICK_BUTTON_PPS_FEEDBACK_GRAPH(SETUP_CLICK_BUTTON_BY_NAME):
    button_name = "mcr_treatment_pps_ctrl2:pcu4_ppsgraphbtn"

class VALIDATE_OPEN_VIEW_PPS_FEEDBACK_GRAPH(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    view_name = "mcr_treatment_pps_feedback_graph2"
    expected_result = "1"

class __M_Tr_PC2_3__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Click and validate button opening view PPS Feedback Graph"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_CLICK_BUTTON_PPS_FEEDBACK_GRAPH,
                        THRIVER_WAIT_5_SECONDS,
                        VALIDATE_OPEN_VIEW_PPS_FEEDBACK_GRAPH,
                        OPEN_VIEW_PPS_CTRL2,
                        ]
        self.teardown_path = []
