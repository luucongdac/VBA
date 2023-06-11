from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_1 import __M_T_BC_1__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_2 import __M_T_BC_2__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_3 import __M_T_BC_3__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_4 import __M_T_BC_4__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_7 import __M_T_BC_7__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_8 import __M_T_BC_8__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_9 import __M_T_BC_9__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_12 import __M_T_BC_12__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_13 import __M_T_BC_13__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_14 import __M_T_BC_14__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_17 import __M_T_BC_17__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_18 import __M_T_BC_18__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_19 import __M_T_BC_19__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_22 import __M_T_BC_22__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_23 import __M_T_BC_23__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_24 import __M_T_BC_24__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_27 import __M_T_BC_27__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_28 import __M_T_BC_28__
from procedures.thriver.test_itp_mcrhci.test_BeamControl.test_BeamControl_test_cases.M_T_BC_29 import __M_T_BC_29__
class test_BeamControlScreen(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_BeamControl"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [ 
                        __M_T_BC_1__,        
                        __M_T_BC_2__,
                        __M_T_BC_3__,
                        __M_T_BC_4__,
                        __M_T_BC_7__,
                        __M_T_BC_8__,
                        __M_T_BC_9__,
                        __M_T_BC_12__,
                        __M_T_BC_13__,
                        __M_T_BC_14__,
                        __M_T_BC_17__,
                        __M_T_BC_18__,
                        __M_T_BC_19__, 
                        __M_T_BC_22__,
                        __M_T_BC_23__,
                        __M_T_BC_24__,
                        __M_T_BC_27__,                       
                        ]
        self.teardown_path = []
        
        
        