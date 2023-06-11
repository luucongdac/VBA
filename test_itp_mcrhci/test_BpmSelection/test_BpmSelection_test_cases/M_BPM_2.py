from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_bpm_selection_view import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10
class THRIVER_WAIT_1_SECONDS(SETUP_THRIVER_WAIT):
    time = 1    
class OPEN_BPM_SELECTION_VIEW(SETUP_CLICK_BUTTON_BY_NAME): 
    name = "Open the BPM Selection View"
    button_name = "mbpm:bpm_id"
class SELECT_AND_VALIDATE_BPM1_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM1 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM1 and it will be sent to varie."
    position_X = 605
    position_Y = 225
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM1"
class SELECT_AND_VALIDATE_BPM2_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM2 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM2 and it will be sent to varie."
    position_X = 605  
    position_Y = 260
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM2"
class SELECT_AND_VALIDATE_BPM3_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM3 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM3 and it will be sent to varie."
    position_X = 605
    position_Y = 295
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM3"
class SELECT_AND_VALIDATE_BPM4_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM4 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM4 and it will be sent to varie."
    position_X = 605
    position_Y = 330
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM4"
class SELECT_AND_VALIDATE_BPM13_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM13 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM13 and it will be sent to varie."
    position_X = 605
    position_Y = 365
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM13"
class SELECT_AND_VALIDATE_BPM5M1_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM5M1 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM5M1 and it will be sent to varie."
    position_X = 605
    position_Y = 400
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM5M1"
class SELECT_AND_VALIDATE_BPM7G1_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM7G1 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM7G1 and it will be sent to varie."
    position_X = 605
    position_Y = 435
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM7G1"
class SELECT_AND_VALIDATE_BPM8G1_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM8G1 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM8G1 and it will be sent to varie."
    position_X = 605
    position_Y = 470
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM8G1"
class SELECT_AND_VALIDATE_BPM9G1_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM9G1 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM9G1 and it will be sent to varie."
    position_X = 710
    position_Y = 225
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM9G1"
class SELECT_AND_VALIDATE_BPM10_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM10 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM10 and it will be sent to varie."
    position_X = 710
    position_Y = 260
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM10"
class SELECT_AND_VALIDATE_BPM11_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM11 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM11 and it will be sent to varie."
    position_X = 710
    position_Y = 295
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM11"
class SELECT_AND_VALIDATE_BPM12_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM12 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM12 and it will be sent to varie."
    position_X = 710
    position_Y = 330
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM12"
class SELECT_AND_VALIDATE_BPM14_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM14 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM14 and it will be sent to varie."
    position_X = 710
    position_Y = 365
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM14"
class SELECT_AND_VALIDATE_BPM5M2_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM5M2 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM5M2 and it will be sent to varie."
    position_X = 710
    position_Y = 400
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM5M2"
class SELECT_AND_VALIDATE_BPM7G2_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM7G2 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM7G2 and it will be sent to varie."
    position_X = 710
    position_Y = 435
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM7G2"
class SELECT_AND_VALIDATE_BPM8G2_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM8G2 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM8G2 and it will be sent to varie."
    position_X = 710
    position_Y = 470
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM8G2"
class SELECT_AND_VALIDATE_BPM9G2_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPM9G2 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPM9G2 and it will be sent to varie."
    position_X = 810
    position_Y = 225
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPM9G2"
class SELECT_AND_VALIDATE_BPMC1_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPMC1 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPMC1 and it will be sent to varie."
    position_X = 810
    position_Y = 260
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPMC1"
class SELECT_AND_VALIDATE_BPMC2_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPMC2 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPMC2 and it will be sent to varie."
    position_X = 810
    position_Y = 295
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPMC2"
class SELECT_AND_VALIDATE_BPME1_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPME1 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPME1 and it will be sent to varie."
    position_X = 810
    position_Y = 330
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPME1"
class SELECT_AND_VALIDATE_BPME2_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPME2 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPME2 and it will be sent to varie."
    position_X = 810
    position_Y = 365
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPME2"
class SELECT_AND_VALIDATE_BPME3_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPME3 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPME3 and it will be sent to varie."
    position_X = 810
    position_Y = 400
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPME3"
class SELECT_AND_VALIDATE_BPMS1_CHECKBOX(SETUP_SELECT_AND_VALIDATE_CHECKBOX):
    name = "Select BPMS1 checkbox and validate that the value of mcr_mcrhci_current_selected_bpm is BPMS1 and it will be sent to varie."
    position_X = 810
    position_Y = 435
    variable_name = "mcr_mcrhci_current_selected_bpm"
    expected_value = "BPMS1"
    
class __M_BPM_2__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Select And Validate For Checkbox"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM1_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM2_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM3_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM4_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM13_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM5M1_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM7G1_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM8G1_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM9G1_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM10_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM11_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM12_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM14_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM5M2_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM7G2_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM8G2_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPM9G2_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPMC1_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPMC2_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPME1_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPME2_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPME3_CHECKBOX,
                        OPEN_BPM_SELECTION_VIEW,
                        THRIVER_WAIT_1_SECONDS,
                        SELECT_AND_VALIDATE_BPMS1_CHECKBOX,                        
                        ]
        self.teardown_path = []