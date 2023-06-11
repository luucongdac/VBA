from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_loadcell_graph1 import *

class CLICK_LOADCELL_TORQUE_Y_CHECKBOX_IN_LOADCELL_GRAPH_1(SETUP_CLICK_LOADCELL_TORQUE_Y_LOADCELL_GRAPH_1): pass

class CLICK_PRINT_BUTTON_LOADCELL_GRAPH_1(SETUP_CLICK_PRINT_BUTTON_LOADCELL_GRAPH_1): pass

class VALIDATE_LOADCELL_TORQUE_Y_CHECKBOX_IN_LOADCELL_GRAPH_1(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "pcu_room1_lc_menuvar5"
    expected_value = 0.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_T_LG1_9__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate that Loadcell Torque Y is deleted in Loadcell Graph 1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_LOADCELL_TORQUE_Y_CHECKBOX_IN_LOADCELL_GRAPH_1,
                        CLICK_PRINT_BUTTON_LOADCELL_GRAPH_1,
                        VALIDATE_LOADCELL_TORQUE_Y_CHECKBOX_IN_LOADCELL_GRAPH_1,
                        ]
        self.teardown_path = []
