from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_loadcell_graph1 import *

class CLICK_LOADCELL_FORCE_Z_CHECKBOX_IN_LOADCELL_GRAPH_1(SETUP_CLICK_LOADCELL_FORCE_Z_LOADCELL_GRAPH_1): pass

class CLICK_PRINT_BUTTON_LOADCELL_GRAPH_1(SETUP_CLICK_PRINT_BUTTON_LOADCELL_GRAPH_1): pass

class VALIDATE_LOADCELL_FORCE_Z_CHECKBOX_IN_LOADCELL_GRAPH_1(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "pcu_room1_lc_menuvar3"
    expected_value = 1.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class SET_VARIABLE_LOADCELL_FORCE_Z(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_loadcell_forcez_eng"
    value    = 123.21

class VALIDATE_LOADCELL_FORCE_Z_VALUE_IN_LOADCELL_GRAPH_1(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "pcu_room1_lc_graph"
    expected_value = 123.21
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_T_LG1_4__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate that Loadcell Force Z is shown in Loadcell Graph 1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_LOADCELL_FORCE_Z_CHECKBOX_IN_LOADCELL_GRAPH_1,
                        CLICK_PRINT_BUTTON_LOADCELL_GRAPH_1,
                        VALIDATE_LOADCELL_FORCE_Z_CHECKBOX_IN_LOADCELL_GRAPH_1,
                        SET_VARIABLE_LOADCELL_FORCE_Z,
                        VALIDATE_LOADCELL_FORCE_Z_VALUE_IN_LOADCELL_GRAPH_1,
                        #TODO: NEED TO HAVE A SETUP FOR VALIDATING GRAPH ATTRIBUTE
                        ]
        self.teardown_path = []
