from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_pps_ctrl1 import *

class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
    time = 5   

class SET_CLICK_BUTTON_TITLE(SETUP_CLICK_BUTTON_BY_NAME):
    button_name = "mcr_treatment_pps_ctrl1:title_button"

class VALIDATE_SHOW_TITLE_USESLOT(SETUP_VALIDATE_VALUE_OF_SLOT):
    slot_name = "view_name"
    expected_value = "pps_ctrl V1"

class __M_Tr_PC1_5__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Click and validate button title"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_CLICK_BUTTON_TITLE,
                        VALIDATE_SHOW_TITLE_USESLOT,
                        ]
        self.teardown_path = []
