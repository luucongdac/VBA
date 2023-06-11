from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_loadcell_graph2 import *

class CLICK_LOADCELL_TORQUE_X_CHECKBOX_IN_LOADCELL_GRAPH_2(SETUP_CLICK_LOADCELL_TORQUE_X_LOADCELL_GRAPH_2): pass

class CLICK_PRINT_BUTTON_LOADCELL_GRAPH_2(SETUP_CLICK_PRINT_BUTTON_LOADCELL_GRAPH_2): pass

class VALIDATE_LOADCELL_TORQUE_X_CHECKBOX_IN_LOADCELL_GRAPH_2(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "pcu_room2_lc_menuvar4"
    expected_value = 1.0
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class SET_VARIABLE_LOADCELL_TORQUE_X(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_loadcell_torquex_eng"
    value    = 123.21

class VALIDATE_LOADCELL_TORQUE_X_VALUE_IN_LOADCELL_GRAPH_2(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "pcu_room2_lc_graph"
    expected_value = 123.21
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"

class __M_T_LG2_6__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate that Loadcell Torque X is shown in Loadcell Graph 2 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_LOADCELL_TORQUE_X_CHECKBOX_IN_LOADCELL_GRAPH_2,
                        CLICK_PRINT_BUTTON_LOADCELL_GRAPH_2,
                        VALIDATE_LOADCELL_TORQUE_X_CHECKBOX_IN_LOADCELL_GRAPH_2,
                        SET_VARIABLE_LOADCELL_TORQUE_X,
                        VALIDATE_LOADCELL_TORQUE_X_VALUE_IN_LOADCELL_GRAPH_2,
                        #TODO: NEED TO HAVE A SETUP FOR VALIDATING GRAPH ATTRIBUTE
                        ]
        self.teardown_path = []
