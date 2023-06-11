from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_loadcell_graph2 import *

class CLICK_LOADCELL_FORCE_Z_CHECKBOX_IN_LOADCELL_GRAPH_2(SETUP_CLICK_LOADCELL_FORCE_Z_LOADCELL_GRAPH_2): pass

class CLICK_PRINT_BUTTON_LOADCELL_GRAPH_2(SETUP_CLICK_PRINT_BUTTON_LOADCELL_GRAPH_2): pass

class VALIDATE_LOADCELL_FORCE_Z_CHECKBOX_IN_LOADCELL_GRAPH_2(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "pcu_room2_lc_menuvar3"
    expected_value = 0.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_T_LG2_5__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate that Loadcell Force Z is deleted in Loadcell Graph 2 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_LOADCELL_FORCE_Z_CHECKBOX_IN_LOADCELL_GRAPH_2,
                        CLICK_PRINT_BUTTON_LOADCELL_GRAPH_2,
                        VALIDATE_LOADCELL_FORCE_Z_CHECKBOX_IN_LOADCELL_GRAPH_2,
                        ]
        self.teardown_path = []
